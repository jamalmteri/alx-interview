#!/usr/bin/python3
import sys
import signal

# Define a dictionary to store the counts of each status code
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Initialize total file size
total_file_size = 0

def print_statistics():
    global total_file_size
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

# Function to handle Ctrl+C
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    line = line.strip()

    # Split the line into components using space as a delimiter
    parts = line.split()

    # Check if the line has the expected format
    if len(parts) == 7 and parts[5].isdigit() and parts[6].isdigit():
        status_code = int(parts[5])
        file_size = int(parts[6])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Check if it's time to print statistics
        if line_count % 10 == 0:
            print_statistics()
