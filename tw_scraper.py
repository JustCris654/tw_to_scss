#!/usr/bin/env python3

import sys
import json
import requests
from bs4 import BeautifulSoup


def extract_classes(urls, file):
    file.write("{\n")
    is_first = True
    for url in urls:
        print(f"Fetching url: {url}...")
        res = requests.get(url)

        soup = BeautifulSoup(res.text, "html.parser")

        header_title = soup.header.div.div.text
        print(f"Extracting content of {header_title}...")

        for row in soup.tbody:
            # add comma and new line to all lines except for the last one
            if is_first:
                is_first = False
            else:
                file.write(",\n")
            tw_class = row.contents[0].text
            scss_class = row.contents[1].text
            scss_class = scss_class.strip().replace("\n", " ").replace('"', "'")
            file.write(f'    "{tw_class}": "{scss_class}"')

    file.write("\n}\n")
    file.close()


def fetch_tw_links(file):
    url = "https://tailwindcss.com/docs/installation"
    print(f"Fetching tailwind links from url: {url}...")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    nav = soup.find(id="nav")
    lis = nav.contents[1].find_all("li", class_="mt-12 lg:mt-8")

    print("Generating JSON array with all links...")

    file.write('{\n  "links": [\n')
    is_first = True

    write_to_file = False
    for li in lis:
        title_text = li.h5.text

        if title_text == "Layout":
            write_to_file = True
        elif title_text == "Official Plugins":
            write_to_file = False

        links = li.find_all("a")
        for el in links:
            if write_to_file:
                if el.text == "Container":
                    continue
                if is_first:
                    is_first = False
                else:
                    file.write(",\n")
                file.write(f'    "https://tailwindcss.com{el["href"]}"')

    file.write("\n  ]\n}")


def get_links_from_json(file_name):
    with open(file_name, "r") as links_json:
        data = json.load(links_json)
        return data["links"]


def main():
    action = sys.argv[1]
    links_file_name = "links.json"

    if action == "links":
        with open(links_file_name, "w") as file:
            fetch_tw_links(file)
    elif action == "json":
        urls = get_links_from_json(links_file_name)
        with open("tw_to_scss.json", "w") as file:
            extract_classes(urls, file)
    elif action == "links-and-json":
        # scrape links
        with open(links_file_name, "w") as file:
            fetch_tw_links(file)

        # scrape tw to css classes and generate json
        urls = get_links_from_json(links_file_name)
        with open("tw_to_scss.json", "w") as file:
            extract_classes(urls, file)
    else:
        print(
            f"Usage:\n{sys.argv[0]} [links|json]\n-  links: Generate links to fetch tailwind classes from\n-  json: Generate json from tailwind documentation fetched from generated links"
        )


if __name__ == "__main__":
    main()
