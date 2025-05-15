"""
Livre: A Simple Markup Language
Expected usage: python livre.py file.lv
"""

import argparse
import os
import sys


def parse_file(file_content: str, file_type: str) -> str:
    """Parses the file"""
    return file_content


def parse_args() -> argparse.Namespace:
    """Parse CLI args"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("input_filepath", help="Input file path")
    parser.add_argument("output_filetype", nargs="?", choices=["html", "md"], default="html", help="Input file type (default: 'html')")
    parser.add_argument("output_filepath", nargs="?", help="Output file path (optional)")
    args = parser.parse_args()

    if args.output_filepath is None:
        # If filepath is `foo/bar/baz.lv`, then the line below returns `baz`
        basename: str = os.path.splitext(os.path.basename(args.input_filepath))[0]
        args.output_filepath = f"basename.{args.output_filetype}" # Add extension based on requested filetype

    return args


def main() -> None:
    """Handles command line arguments"""
    args: argparse.Namespace = parse_args()

    with open(args.input_filepath, "r") as input:
        with open(args.output_filepath, "w") as output:
            output.write(parse_file(input.read(), args.output_filetype))


if __name__ == "__main__":
    main()
