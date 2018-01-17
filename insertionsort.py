#!/usr/bin/python
import sys
import argparse

parser = argparse.ArgumentParser(description="Process some intergers.",prog="insertsort")
args = parser.parse_args()
print(args.ints)
