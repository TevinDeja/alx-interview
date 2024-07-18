#!/usr/bin/python3
import sys
import re
from collections import defaultdict


def parse_log_line(line):
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def process_logs():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line.strip())
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == '__main__':
    process_logs()
