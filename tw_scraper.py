#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

urls = [
    "https://tailwindcss.com/docs/aspect-ratio",
    "https://tailwindcss.com/docs/columns",
    "https://tailwindcss.com/docs/break-after",
    "https://tailwindcss.com/docs/break-before",
    "https://tailwindcss.com/docs/break-inside",
    "https://tailwindcss.com/docs/box-decoration-break",
    "https://tailwindcss.com/docs/box-sizing",
    "https://tailwindcss.com/docs/display",
    "https://tailwindcss.com/docs/float",
    "https://tailwindcss.com/docs/clear",
    "https://tailwindcss.com/docs/isolation",
    "https://tailwindcss.com/docs/object-fit",
    "https://tailwindcss.com/docs/object-position",
    "https://tailwindcss.com/docs/overflow",
    "https://tailwindcss.com/docs/overscroll-behavior",
    "https://tailwindcss.com/docs/position",
    "https://tailwindcss.com/docs/top-right-bottom-left",
    "https://tailwindcss.com/docs/visibility",
    "https://tailwindcss.com/docs/z-index",
    "https://tailwindcss.com/docs/flex-basis",
    "https://tailwindcss.com/docs/flex-direction",
    "https://tailwindcss.com/docs/flex-wrap",
    "https://tailwindcss.com/docs/flex",
    "https://tailwindcss.com/docs/flex-grow",
    "https://tailwindcss.com/docs/flex-shrink",
    "https://tailwindcss.com/docs/order",
    "https://tailwindcss.com/docs/grid-template-columns",
    "https://tailwindcss.com/docs/grid-column",
    "https://tailwindcss.com/docs/grid-template-rows",
    "https://tailwindcss.com/docs/grid-row",
    "https://tailwindcss.com/docs/grid-auto-flow",
    "https://tailwindcss.com/docs/grid-auto-columns",
    "https://tailwindcss.com/docs/grid-auto-rows",
    "https://tailwindcss.com/docs/gap",
    "https://tailwindcss.com/docs/justify-content",
    "https://tailwindcss.com/docs/justify-items",
    "https://tailwindcss.com/docs/justify-self",
    "https://tailwindcss.com/docs/align-content",
    "https://tailwindcss.com/docs/align-items",
    "https://tailwindcss.com/docs/align-self",
    "https://tailwindcss.com/docs/place-content",
    "https://tailwindcss.com/docs/place-items",
    "https://tailwindcss.com/docs/place-self",
    "https://tailwindcss.com/docs/padding",
    "https://tailwindcss.com/docs/margin",
    "https://tailwindcss.com/docs/space",
    "https://tailwindcss.com/docs/width",
    "https://tailwindcss.com/docs/min-width",
    "https://tailwindcss.com/docs/max-width",
    "https://tailwindcss.com/docs/height",
    "https://tailwindcss.com/docs/min-height",
    "https://tailwindcss.com/docs/max-height",
    "https://tailwindcss.com/docs/font-family",
    "https://tailwindcss.com/docs/font-size",
    "https://tailwindcss.com/docs/font-smoothing",
    "https://tailwindcss.com/docs/font-style",
    "https://tailwindcss.com/docs/font-weight",
    "https://tailwindcss.com/docs/font-variant-numeric",
    "https://tailwindcss.com/docs/letter-spacing",
    "https://tailwindcss.com/docs/line-clamp",
    "https://tailwindcss.com/docs/line-height",
    "https://tailwindcss.com/docs/list-style-image",
    "https://tailwindcss.com/docs/list-style-position",
    "https://tailwindcss.com/docs/list-style-type",
    "https://tailwindcss.com/docs/text-align",
    "https://tailwindcss.com/docs/text-color",
    "https://tailwindcss.com/docs/text-decoration",
    "https://tailwindcss.com/docs/text-decoration-color",
    "https://tailwindcss.com/docs/text-decoration-style",
    "https://tailwindcss.com/docs/text-decoration-thickness",
    "https://tailwindcss.com/docs/text-underline-offset",
    "https://tailwindcss.com/docs/text-transform",
    "https://tailwindcss.com/docs/text-overflow",
    "https://tailwindcss.com/docs/text-indent",
    "https://tailwindcss.com/docs/vertical-align",
    "https://tailwindcss.com/docs/whitespace",
    "https://tailwindcss.com/docs/word-break",
    "https://tailwindcss.com/docs/hyphens",
    "https://tailwindcss.com/docs/content",
    "https://tailwindcss.com/docs/background-attachment",
    "https://tailwindcss.com/docs/background-clip",
    "https://tailwindcss.com/docs/background-color",
    "https://tailwindcss.com/docs/background-origin",
    "https://tailwindcss.com/docs/background-position",
    "https://tailwindcss.com/docs/background-repeat",
    "https://tailwindcss.com/docs/background-size",
    "https://tailwindcss.com/docs/background-image",
    "https://tailwindcss.com/docs/gradient-color-stops",
    "https://tailwindcss.com/docs/border-radius",
    "https://tailwindcss.com/docs/border-width",
    "https://tailwindcss.com/docs/border-color",
    "https://tailwindcss.com/docs/border-style",
    "https://tailwindcss.com/docs/divide-width",
    "https://tailwindcss.com/docs/divide-color",
    "https://tailwindcss.com/docs/divide-style",
    "https://tailwindcss.com/docs/outline-width",
    "https://tailwindcss.com/docs/outline-color",
    "https://tailwindcss.com/docs/outline-style",
    "https://tailwindcss.com/docs/outline-offset",
    "https://tailwindcss.com/docs/ring-width",
    "https://tailwindcss.com/docs/ring-color",
    "https://tailwindcss.com/docs/ring-offset-width",
    "https://tailwindcss.com/docs/ring-offset-color",
    "https://tailwindcss.com/docs/box-shadow",
    "https://tailwindcss.com/docs/box-shadow-color",
    "https://tailwindcss.com/docs/opacity",
    "https://tailwindcss.com/docs/mix-blend-mode",
    "https://tailwindcss.com/docs/background-blend-mode",
    "https://tailwindcss.com/docs/blur",
    "https://tailwindcss.com/docs/brightness",
    "https://tailwindcss.com/docs/contrast",
    "https://tailwindcss.com/docs/drop-shadow",
    "https://tailwindcss.com/docs/grayscale",
    "https://tailwindcss.com/docs/hue-rotate",
    "https://tailwindcss.com/docs/invert",
    "https://tailwindcss.com/docs/saturate",
    "https://tailwindcss.com/docs/sepia",
    "https://tailwindcss.com/docs/backdrop-blur",
    "https://tailwindcss.com/docs/backdrop-brightness",
    "https://tailwindcss.com/docs/backdrop-contrast",
    "https://tailwindcss.com/docs/backdrop-grayscale",
    "https://tailwindcss.com/docs/backdrop-hue-rotate",
    "https://tailwindcss.com/docs/backdrop-invert",
    "https://tailwindcss.com/docs/backdrop-opacity",
    "https://tailwindcss.com/docs/backdrop-saturate",
    "https://tailwindcss.com/docs/backdrop-sepia",
    "https://tailwindcss.com/docs/border-collapse",
    "https://tailwindcss.com/docs/border-spacing",
    "https://tailwindcss.com/docs/table-layout",
    "https://tailwindcss.com/docs/caption-side",
    "https://tailwindcss.com/docs/transition-property",
    "https://tailwindcss.com/docs/transition-duration",
    "https://tailwindcss.com/docs/transition-timing-function",
    "https://tailwindcss.com/docs/transition-delay",
    "https://tailwindcss.com/docs/animation",
    "https://tailwindcss.com/docs/scale",
    "https://tailwindcss.com/docs/rotate",
    "https://tailwindcss.com/docs/translate",
    "https://tailwindcss.com/docs/skew",
    "https://tailwindcss.com/docs/transform-origin",
    "https://tailwindcss.com/docs/accent-color",
    "https://tailwindcss.com/docs/appearance",
    "https://tailwindcss.com/docs/cursor",
    "https://tailwindcss.com/docs/caret-color",
    "https://tailwindcss.com/docs/pointer-events",
    "https://tailwindcss.com/docs/resize",
    "https://tailwindcss.com/docs/scroll-behavior",
    "https://tailwindcss.com/docs/scroll-margin",
    "https://tailwindcss.com/docs/scroll-padding",
    "https://tailwindcss.com/docs/scroll-snap-align",
    "https://tailwindcss.com/docs/scroll-snap-stop",
    "https://tailwindcss.com/docs/scroll-snap-type",
    "https://tailwindcss.com/docs/touch-action",
    "https://tailwindcss.com/docs/user-select",
    "https://tailwindcss.com/docs/will-change",
    "https://tailwindcss.com/docs/fill",
    "https://tailwindcss.com/docs/stroke",
    "https://tailwindcss.com/docs/stroke-width",
    "https://tailwindcss.com/docs/screen-readers",
]


def extract_classes(urls, file):
    file.write("{\n")
    is_first = True
    for url in urls:
        res = requests.get(url)

        soup = BeautifulSoup(res.text, "html.parser")

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
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    nav = soup.find(id="nav")
    lis = nav.contents[1].find_all("li", class_="mt-12 lg:mt-8")

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
                file.write(f'https://tailwindcss.com{el["href"]}\n')


def main():
    action = sys.argv[1]

    if action == "links":
        with open("links.txt", "w") as file:
            fetch_tw_links(file)
    elif action == "json":
        with open("tw_to_scss.json", "w") as file:
            extract_classes(urls, file)
    else:
        print(
            f"Usage:\n{sys.argv[0]} [links|json]\n-  links: Generate links to fetch tailwind classes from\n-  json: Generate json from tailwind documentation fetched from generated links"
        )


if __name__ == "__main__":
    main()
