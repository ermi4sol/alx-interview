#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

def print_metrics():
    """Prints the collected metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def handle_interrupt(signum, frame):
    """Handles the keyboard interrupt (CTRL + C) to print metrics."""
    print_metrics()
    sys.exit(0)

# Register signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Skip lines that don't match the expected format
        if len(parts) < 7:
            continue

        # Extract the file size and status code
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
            total_file_size += file_size

            if status_code in status_code_count:
                status_code_count[status_code] += 1
        except ValueError:
            continue  # Ignore lines with invalid integers

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
