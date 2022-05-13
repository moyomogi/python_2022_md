#!/usr/bin/python3
# Usage:
#   python3 mathjax.py book_src/session-1.md
import os
import glob
import re
import sys

is_local = os.path.isfile("input.md")

# Enumerate all Markdown files in book_src.
for file in glob.glob("book_src/*.md"):
    # Read file.
    with open(file, "r") as f:
        cur_lines = f.readlines()
        new_lines = []
        test_lines = []
        for line in cur_lines:
            if re.match(r".+\$([^\$]+)\$.+", line):
                line = re.sub(r"\$([^\$]+)\$", r"\\\\( \1 \\\\)", line)
                test_lines.append(line)
            # Append to new_lines.
            new_lines.append(line)
    print("- file:", file, file=sys.stderr)
    print("  test_lines:", test_lines, file=sys.stderr)
    if not is_local:
        # Write file.
        with open(file, "w") as f:
            # Write new_lines to file
            f.writelines(new_lines)
