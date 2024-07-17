#!/usr/bin/python3
import sys
import random
from datetime import datetime
import time

def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_log_entry():
    ip = generate_ip()
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]")
    status = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(100, 5000)
    return f"{ip} - {timestamp} \"GET /projects/260 HTTP/1.1\" {status} {file_size}\n"

def main():
    try:
        for _ in range(10000):
            log_entry = generate_log_entry()
            sys.stdout.write(log_entry)
            sys.stdout.flush()
            time.sleep(random.uniform(0.1, 0.3))
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
