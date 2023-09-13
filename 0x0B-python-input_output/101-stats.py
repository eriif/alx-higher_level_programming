#!/usr/bin/python3

import sys
import signal
from collections import defaultdict

# Initialize variables to keep track of metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# Function to print statistics
def print_statistics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

# Handle keyboard interruption (CTRL + C) to print statistics
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            status_code_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C) to print statistics
    print_statistics()
