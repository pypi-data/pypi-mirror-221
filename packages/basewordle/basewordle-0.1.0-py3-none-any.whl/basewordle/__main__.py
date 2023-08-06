"""CLI for base-wordle.

With no options, base-wordle reads raw data from stdin and writes
encoded data to stdout.

"""
import argparse
import sys

from .code import decode, encode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        action="store_true",
        help="Decode incoming data",
    )
    parser.add_argument(
        "--pad-digits",
        type=int,
        default=0,
        help="A more efficient encoding that embeds some digits too.",
    )
    parser.add_argument("--input-file", "-i")
    parser.add_argument("--output-file", "-o")
    args = parser.parse_args()

    if args.d:
        reader = sys.stdin  # decode string/text
        if args.input_file:
            reader = open(args.input_file)
        writer = sys.stdout.buffer
        if args.output_file:
            writer = open(args.output_file, "wb")

        for line in reader.readlines():
            writer.write(decode(line.rstrip()))

    else:
        reader = sys.stdin.buffer  # encode binary data
        if args.input_file:
            reader = open(args.input_file, "rb")
        writer = sys.stdout
        if args.output_file:
            writer = open(args.output_file, "w")

        print(encode(reader.read(), pad_digits=args.pad_digits), file=writer)


if __name__ == "__main__":
    main()
