#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return int(match.group(3)), int(match.group(4))
    return None, None

def main():
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in valid_codes:
                    status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
