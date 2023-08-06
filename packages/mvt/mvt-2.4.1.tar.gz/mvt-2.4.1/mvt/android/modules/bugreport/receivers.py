# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.parsers import parse_dumpsys_receiver_resolver_table

from .base import BugReportModule

INTENT_NEW_OUTGOING_SMS = "android.provider.Telephony.NEW_OUTGOING_SMS"
INTENT_SMS_RECEIVED = "android.provider.Telephony.SMS_RECEIVED"
INTENT_DATA_SMS_RECEIVED = "android.intent.action.DATA_SMS_RECEIVED"
INTENT_PHONE_STATE = "android.intent.action.PHONE_STATE"
INTENT_NEW_OUTGOING_CALL = "android.intent.action.NEW_OUTGOING_CALL"


class Receivers(BugReportModule):
    """This module extracts details on receivers for risky activities."""

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

        self.results = results if results else {}

    def check_indicators(self) -> None:
        if not self.indicators:
            return

        for intent, receivers in self.results.items():
            for receiver in receivers:
                if intent == INTENT_NEW_OUTGOING_SMS:
                    self.log.info(
                        'Found a receiver to intercept outgoing SMS messages: "%s"',
                        receiver["receiver"],
                    )
                elif intent == INTENT_SMS_RECEIVED:
                    self.log.info(
                        'Found a receiver to intercept incoming SMS messages: "%s"',
                        receiver["receiver"],
                    )
                elif intent == INTENT_DATA_SMS_RECEIVED:
                    self.log.info(
                        'Found a receiver to intercept incoming data SMS message: "%s"',
                        receiver["receiver"],
                    )
                elif intent == INTENT_PHONE_STATE:
                    self.log.info(
                        "Found a receiver monitoring "
                        'telephony state/incoming calls: "%s"',
                        receiver["receiver"],
                    )
                elif intent == INTENT_NEW_OUTGOING_CALL:
                    self.log.info(
                        'Found a receiver monitoring outgoing calls: "%s"',
                        receiver["receiver"],
                    )

                ioc = self.indicators.check_app_id(receiver["package_name"])
                if ioc:
                    receiver["matched_indicator"] = ioc
                    self.detected.append({intent: receiver})
                    continue

    def run(self) -> None:
        content = self._get_dumpstate_file()
        if not content:
            self.log.error(
                "Unable to find dumpstate file. "
                "Did you provide a valid bug report archive?"
            )
            return

        in_receivers = False
        lines = []
        for line in content.decode(errors="ignore").splitlines():
            if line.strip() == "DUMP OF SERVICE package:":
                in_receivers = True
                continue

            if not in_receivers:
                continue

            if line.strip().startswith(
                "------------------------------------------------------------------------------"
            ):  # pylint: disable=line-too-long
                break

            lines.append(line)

        self.results = parse_dumpsys_receiver_resolver_table("\n".join(lines))

        self.log.info("Extracted receivers for %d intents", len(self.results))
