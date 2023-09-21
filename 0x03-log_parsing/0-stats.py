import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines with incorrect format

        # Extract relevant information
        status_code = int(parts[5])
        file_size = int(parts[6])

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_code_counts.keys()):
                if status_code_counts[code] > 0:
                    print("{}: {}".format(code, status_code_counts[code]))

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass

# Print the final statistics
print("File size: {}".format(total_file_size))
for code in sorted(status_code_counts.keys()):
    if status_code_counts[code] > 0:
        print("{}: {}".format(code, status_code_counts[code]))
