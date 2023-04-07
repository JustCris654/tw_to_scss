#!/usr/bin/env python3

import sys
import io
import json

media_queries = {
    "sm": "@media (min-width: 640px) {$}",
    "md": "@media (min-width: 768px) {$}",
    "lg": "@media (min-width: 1024px) {$}",
    "xl": "@media (min-width: 1280px) {$}",
    "2xl": "@media (min-width: 1536px) {$}",
}

states = {
    "hover": ":hover {$}",
    "focus": ":focus {$}",
}


def convert_line_and_write(line: str, twtoscss_dict: dict, out: io.StringIO):
    stripped_line = line.strip()
    if not line or line.isspace() or stripped_line[0] == "." or stripped_line[0] == "}":
        out.write(line)
        out.write("\n")
        return

    tw_classes: [str] = stripped_line.split(" ")
    for tw_class in tw_classes:
        # check if its a media query or state
        # i could've checked splitted lenght but this if
        # seems more readable to me
        if ":" in tw_class:
            splitted = tw_class.split(":")
            if splitted[0] in media_queries:
                scss_to_write = (
                    media_queries[splitted[0]].replace(
                        "$", f"\n  {twtoscss_dict[splitted[1]]}\n"
                    )
                    + "\n"
                )
            elif splitted[0] in states:
                scss_to_write = (
                    "&"
                    + states[splitted[0]].replace(
                        "$", f"\n  {twtoscss_dict[splitted[1]]}\n"
                    )
                    + "\n"
                )
            print(scss_to_write)
            out.write(scss_to_write)

        if tw_class in twtoscss_dict:
            scss_to_write = f"{twtoscss_dict[tw_class]}\n"
            print(scss_to_write)
            out.write(scss_to_write)
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
