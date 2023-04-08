#!/usr/bin/env python3

import sys
import io
import json

DEFAULT_DICT_FILE_NAME = "tw_to_scss.json"
DEFAULT_OUT_FILT_NAME = "out.scss"

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


def convert_media_query(
    splitted_class: [str], twtoscss_dict: dict, media_queries: dict
):
    return (
        media_queries[splitted_class[0]].replace(
            "$", f"\n  {twtoscss_dict[splitted_class[1]]}\n"
        )
        + "\n"
    )


def convert_state(splitted_class: [str], twtoscss_dict: dict, states: dict):
    return (
        "&"
        + states[splitted_class[0]].replace(
            "$", f"\n  {twtoscss_dict[splitted_class[1]]}\n"
        )
        + "\n"
    )


# detect if class is using media queries or states and convert
# accordingly
def convert_derived_state(
    tw_class: str,
    twtoscss_dict: dict,
    media_queries: dict,
    states: dict,
    out: io.StringIO,
):
    splitted = tw_class.split(":")
    if splitted[0] in media_queries:
        scss_to_write = convert_media_query(splitted, twtoscss_dict, media_queries)
    elif splitted[0] in states:
        scss_to_write = convert_state(splitted, twtoscss_dict, states)
    print(scss_to_write)
    out.write(scss_to_write)


# convert simple tw class to scss
def convert_tw_class(tw_class: str, twtoscss_dict: dict, out: io.StringIO):
    scss_to_write = f"{twtoscss_dict[tw_class]}\n"
    print(scss_to_write)
    out.write(scss_to_write)


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
            convert_derived_state(tw_class, twtoscss_dict, media_queries, states, out)
        elif tw_class in twtoscss_dict:
            convert_tw_class(tw_class, twtoscss_dict, out)
        else:
            # TODO: implement not tailwind class
            pass


def twjson_to_dict(file_name: str):
    with open(file_name) as json_dict:
        data = json.load(json_dict)
        return data


def convert_tw_file_to_scss(in_file_name: str, dict_file_name: str, out_file_name: str):
    try:
        scss_file = open(in_file_name, "r+")
    except IOError:
        print(f"Cannot open this file: {in_file_name}")
        exit(-1)

    scss_lines = scss_file.read().split("\n")

    twtoscss_dict = twjson_to_dict(dict_file_name)

    with open(out_file_name, "w") as out_file:
        for line in scss_lines:
            convert_line_and_write(line, twtoscss_dict, out_file)


def main():
    file_name = sys.argv[1]

    convert_tw_file_to_scss(file_name, DEFAULT_DICT_FILE_NAME, DEFAULT_OUT_FILT_NAME)


if __name__ == "__main__":
    main()
