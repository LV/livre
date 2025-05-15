"""
Livre: A Simple Markup Language, compiled to HTML
Expected usage: python livre.py file.lv output.html
"""

import argparse
import os
import sys


def parse_file(file_content: str, file_type: str) -> str:
    """Parses the file"""
    output_buffer: str = ""
    for line in file_content.splitlines():
        parse_line(line)
    return file_content


def parse_args() -> argparse.Namespace:
    """Parse CLI args"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("input_filepath", help="Input file path")
    parser.add_argument("output_filepath", nargs="?", help="Output file path (optional)")
    args = parser.parse_args()

    if args.output_filepath is None:
        # If input filepath is `foo/bar/baz.lv`, then this code below returns `baz.html`
        basename: str = os.path.splitext(os.path.basename(args.input_filepath))[0]
        args.output_filepath = f"{basename}.html"

    return args


def main() -> None:
    """Handles command line arguments"""
    args: argparse.Namespace = parse_args()

    with open(args.input_filepath, "r") as input:
        with open(args.output_filepath, "w") as output:
            output.write(parse_file(input.read(), args.output_filetype))


if __name__ == "__main__":
    main()
