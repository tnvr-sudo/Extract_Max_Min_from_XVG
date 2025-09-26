import re
import os
import sys

# Check if at least one file name is provided
if len(sys.argv) < 2:
    print("Usage: python extract_numb.py <filename1.xvg> [filename2.xvg ...]")
    sys.exit(1)

# Loop through all provided filenames
for file_name in sys.argv[1:]:
    if not os.path.exists(file_name):
        print(f"File {file_name} not found. Skipping.")
        continue

    time_values = []
    numb_values = []

    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith(('@', '#')) or not line.strip():
                continue
            parts = re.split(r'\s+', line.strip())
            if len(parts) >= 2:
                try:
                    time = float(parts[0])
                    numb = float(parts[1])
                    time_values.append(time)
                    numb_values.append(numb)
                except ValueError:
                    continue  # skip malformed lines

    if numb_values:
        min_numb = min(numb_values)
        max_numb = max(numb_values)
        avg_numb = sum(numb_values) / len(numb_values)
        print(f"\nFile: {file_name}")
        print(f"  Data points: {len(numb_values)}")
        print(f"  Minimum numb: {min_numb}")
        print(f"  Maximum numb: {max_numb}")
        print(f"  Average numb: {avg_numb}")
    else:
        print(f"File {file_name} contains no valid data.")

