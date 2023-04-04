#!/usr/bin/env python3

import sys
import io


def convert_line_and_write(line: str, out: io.StringIO):
    stripped_line = line.strip()
    if not line or line.isspace() or stripped_line[0] == "." or stripped_line[0] == "}":
        out.write(line)
        out.write("\n")
        return

    classes = stripped_line.split(" ")
    2


def main():
    file_name = sys.argv[1]

    try:
        scss_file = open(file_name, "r+")
    except IOError:
        print(f"Cannot open this file: {file_name}")

    scss_lines = scss_file.read().split("\n")

    # go to start of file and delete all file content
    # scss_file.seek(0)
    # scss_file.truncate()
    out_file = open("out.scss", "w")

    for line in scss_lines:
        convert_line_and_write(line, out_file)
        continue

    scss_file.close()


if __name__ == "__main__":
    main()

    # for line in scss_file:
    #     if line.isspace():
    #         continue

    #     line = line.strip()
    #     if line[0] == "." or line[0] == "}":
    #         continue
    #     else:
    #         print(line)
