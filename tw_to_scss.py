#!/usr/bin/env python3

import sys
import io
import json


def convert_line_and_write(line: str, twtoscss_dict: dict, out: io.StringIO):
    stripped_line = line.strip()
    if not line or line.isspace() or stripped_line[0] == "." or stripped_line[0] == "}":
        out.write(line)
        out.write("\n")
        return

    tw_classes = stripped_line.split(" ")
    for tw_class in tw_classes:
        if tw_class in twtoscss_dict:
            print(twtoscss_dict[tw_class])
            out.write(f"{twtoscss_dict[tw_class]}\n")
        else:
            # TODO: implement not tailwind class
            pass


def twjson_to_dict(file_name: str):
    with open(file_name) as json_dict:
        data = json.load(json_dict)
        return data


def main():
    file_name = sys.argv[1]

    try:
        scss_file = open(file_name, "r+")
    except IOError:
        print(f"Cannot open this file: {file_name}")

    scss_lines = scss_file.read().split("\n")

    twtoscss_dict = twjson_to_dict("tw_to_scss.json")

    # go to start of file and delete all file content
    # scss_file.seek(0)
    # scss_file.truncate()
    out_file = open("out.scss", "w")

    for line in scss_lines:
        convert_line_and_write(line, twtoscss_dict, out_file)
        continue

    scss_file.close()


if __name__ == "__main__":
    main()
