#!/usr/bin/env python

from argparse_plus import api

def parse_args(argv=None):
    parser = api.ArgumentParser()

    parser.add_argument("--value", help="a value")
    options = parser.parse_args(argv)
    return options.__dict__

def main(value):
    print("HELLO", value)

if __name__ == "__main__":
    main(**parse_args())
