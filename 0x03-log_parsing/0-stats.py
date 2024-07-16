#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    """Prints the statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            ip, _, _, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]

            if not file_size.isdigit():
                continue

            total_size += int(file_size)
            status_code = int(status_code)

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
