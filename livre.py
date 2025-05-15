"""
Livre: A Simple Markup Language
Expected usage: python livre.py file.lv
"""

import argparse
import sys


def parse():
    """Parses the file"""
    print("Hello Livre")


def parse_args() -> argparse.Namespace:
    """Parse CLI args"""
    parser: argparse.Namespace = argparse.ArgumentParser()
    parser.add_argument("input_filepath", help="Input file path")
    parser.add_argument("output_filetype", help="Output file type", default="html")
    parser.add_argument("output_filepath", help="Output file path")
    return parser.parse_args()


def main() -> None:
    """Handles command line arguments"""
    args: argparse.Namespace = parse_args()

    filename = sys.argv[1] # second argument is the file to parse

    with open(filename, "r") as file:
        parse(file.read())


if __name__ == "__main__":
    main()
