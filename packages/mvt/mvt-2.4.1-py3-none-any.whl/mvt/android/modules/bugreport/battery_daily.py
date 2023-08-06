# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional, Union

from mvt.android.parsers import parse_dumpsys_battery_daily

from .base import BugReportModule


class BatteryDaily(BugReportModule):
    """This module extracts records from battery daily updates."""

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

    def serialize(self, record: dict) -> Union[dict, list]:
        return {
            "timestamp": record["from"],
            "module": self.__class__.__name__,
            "event": "battery_daily",
            "data": f"Recorded update of package {record['package_name']} "
            f"with vers {record['vers']}",
        }

    def check_indicators(self) -> None:
        if not self.indicators:
            return

        for result in self.results:
            ioc = self.indicators.check_app_id(result["package_name"])
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

        lines = []
        in_batterystats = False
        in_daily = False
        for line in content.decode(errors="ignore").splitlines():
            if line.strip() == "DUMP OF SERVICE batterystats:":
                in_batterystats = True
                continue

            if not in_batterystats:
                continue

            if line.strip() == "Daily stats:":
                lines.append(line)
                in_daily = True
                continue

            if not in_daily:
                continue

            if line.strip() == "":
                break

            lines.append(line)

        self.results = parse_dumpsys_battery_daily("\n".join(lines))

        self.log.info("Extracted a total of %d battery daily stats", len(self.results))
