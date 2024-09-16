import argparse
import sys


def setup():
    parser = argparse.ArgumentParser(description="this is the first cli project")
    parser.add_argument('--all', action="store_true", help="display all data")
    parser.add_argument('--city', type=str, help="Get name of the city")
    return parser


parser = setup()
args = parser.parse_args()
print(sys.argv)