#!/usr/bin/env python
import time

from package.oss.cov_json import get_json_report
from package.oss.init import initialization
from package.tool.summarize_jsons import summarize_jsons


def report_coverage() -> None:
    start_time = time.time()
    (options, test_list, interested_folders) = initialization()
    # run cpp tests
    get_json_report(test_list, options)
    # collect coverage data from json profiles
    if options.need_summary:
        summarize_jsons(test_list, interested_folders, [""], start_time)


if __name__ == "__main__":
    report_coverage()
