# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.parsers import parse_dumpsys_dbinfo

from .base import BugReportModule


class DBInfo(BugReportModule):
    """This module extracts records from battery daily updates."""

    slug = "dbinfo"

    def __init__(
        self,
        file_path: Optional[str] = None,
        target_path: Optional[str] = None,
        results_path: Optional[str] = None,
        module_options: Optional[dict] = None,
        log: logging.Logger = logging.getLogger(__name__),
        results: Optional[list] = None,
    ) -> None:
        super().__init__(
            file_path=file_path,
            target_path=target_path,
            results_path=results_path,
            module_options=module_options,
            log=log,
            results=results,
        )

    def check_indicators(self) -> None:
        if not self.indicators:
            return

        for result in self.results:
            path = result.get("path", "")
            for part in path.split("/"):
                ioc = self.indicators.check_app_id(part)
                if ioc:
                    result["matched_indicator"] = ioc
                    self.detected.append(result)
                    continue

    def run(self) -> None:
        content = self._get_dumpstate_file()
        if not content:
            self.log.error(
                "Unable to find dumpstate file. "
                "Did you provide a valid bug report archive?"
            )
            return

        in_dbinfo = False
        lines = []
        for line in content.decode(errors="ignore").splitlines():
            if line.strip() == "DUMP OF SERVICE dbinfo:":
                in_dbinfo = True
                continue

            if not in_dbinfo:
                continue

            if line.strip().startswith(
                "------------------------------------------------------------------------------"
            ):  # pylint: disable=line-too-long
                break

            lines.append(line)

        self.results = parse_dumpsys_dbinfo("\n".join(lines))

        self.log.info(
            "Extracted a total of %d database connection pool records",
            len(self.results),
        )
