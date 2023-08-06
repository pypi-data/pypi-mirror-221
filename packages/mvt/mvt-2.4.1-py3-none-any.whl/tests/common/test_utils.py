# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2022 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
import os

from mvt.common.utils import (
    convert_datetime_to_iso,
    convert_mactime_to_iso,
    convert_unix_to_iso,
    convert_unix_to_utc_datetime,
    generate_hashes_from_path,
    get_sha256_from_file_path,
)

from ..utils import get_artifact_folder

TEST_DATE_EPOCH = 1626566400
TEST_DATE_ISO = "2021-07-18 00:00:00.000000"
TEST_DATE_MAC = TEST_DATE_EPOCH - 978307200


class TestDateConversions:
    def test_convert_unix_to_iso(self):
        assert convert_unix_to_iso(TEST_DATE_EPOCH) == TEST_DATE_ISO

    def test_convert_mactime_to_iso(self):
        assert convert_mactime_to_iso(TEST_DATE_MAC) == TEST_DATE_ISO

    def test_convert_unix_to_utc_datetime(self):
        converted = convert_unix_to_utc_datetime(TEST_DATE_EPOCH)
        assert converted.year == 2021
        assert converted.month == 7
        assert converted.day == 18

    def test_convert_datetime_to_iso(self):
        converted = convert_unix_to_utc_datetime(TEST_DATE_EPOCH)
        assert convert_datetime_to_iso(converted) == TEST_DATE_ISO


class TestHashes:
    def test_hash_from_file(self):
        path = os.path.join(get_artifact_folder(), "androidqf", "backup.ab")
        sha256 = get_sha256_from_file_path(path)
        assert (
            sha256 == "f0e32fe8a7fd5ac0e2de19636d123c0072e979396986139ba2bc49ec385dc325"
        )

    def test_hash_from_folder(self):
        path = os.path.join(get_artifact_folder(), "androidqf")
        hashes = list(generate_hashes_from_path(path, logging))
        assert len(hashes) == 5
        # Sort the files to have reliable order for tests.
        hashes = sorted(hashes, key=lambda x: x["file_path"])
        assert hashes[0]["file_path"] == os.path.join(path, "backup.ab")
        assert (
            hashes[0]["sha256"]
            == "f0e32fe8a7fd5ac0e2de19636d123c0072e979396986139ba2bc49ec385dc325"
        )
        assert hashes[1]["file_path"] == os.path.join(path, "dumpsys.txt")
        assert (
            hashes[1]["sha256"]
            == "bac858001784657a43c7cfa771fd1fc4a49428eb6b7c458a1ebf2fdeef78dd86"
        )
