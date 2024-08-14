#!/usr/bin/env python3
'''parsing HTTP request logs'''
import sys
import signal

total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    '''Print the collected statistics.'''
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def process_line(line):
    '''Process a single line to extract metrics.'''
    global total_file_size, line_count

    try:
        parts = line.split()
        ip, date, request, status_code, file_size = parts[0], parts[3]
        + ' ' + parts[4], parts[5] + ' ' + parts[6] + ' '
        + parts[7], parts[-2], parts[-1]

        if request == '"GET /projects/260 HTTP/1.1"' and
        status_code.isdigit() and file_size.isdigit():
            total_file_size += int(file_size)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except Exception:
        pass


def signal_handler(sig, frame):
    '''Handle keyboard interruption (CTRL + C).'''
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    process_line(line.strip())

print_stats()
