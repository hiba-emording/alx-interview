#!/usr/bin/python3
'''A script for parsing and processing HTTP request logs.'''

import re


def extract_input(input_line):
    '''Extracts sections of a line from an HTTP request log.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: A dictionary containing the status code and file size.
    '''
    pattern = (
        r'(?P<ip>\S+)\s*'
        r'-\s*\[(?P<date>[^\]]+)\]\s*'
        r'"(?P<request>[^"]+)"\s*'
        r'(?P<status_code>\d{3})\s*'
        r'(?P<file_size>\d+)'
    )
    match = re.fullmatch(pattern, input_line.strip())
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return {
        'status_code': '0',
        'file_size': 0
    }


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size processed.
        status_codes_stats (dict): The counts of each status code encountered.
    '''
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current counts of status codes.

    Returns:
        int: The updated total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser to read input and compute statistics.'''
    line_count = 0
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in
                          [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        while True:
            line = input()
            total_file_size = update_metrics(line,
                                             total_file_size,
                                             status_codes_stats
                                             )
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
