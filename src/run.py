#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True

import argparse
import datetime
from importlib import import_module
import traceback

parser = argparse.ArgumentParser(
    description="""
    Runs Advent of Code solutions. Takes input from stdin.
    """)

parser.add_argument(
    'year',
    metavar='YEAR',
    type=int,
    help='the year of the solution to run')
parser.add_argument(
    'day',
    metavar='DAY',
    type=int,
    help='the day of the solution to run')

args = parser.parse_args()

today = datetime.datetime.now()

blob = None
try:
    blob = sys.stdin.read()
except:
    print('no input')
    exit(1)

fns = ['p1', 'p2']
module_str = f'sln.{args.year}_{args.day:02}'
module = None
try:
    module = import_module(module_str)
except:
    print(f'failed to import module: "{module_str}"')
    print(traceback.format_exc())
    exit(1)

for fn in fns:
    attr = None
    try:
        attr = getattr(module,fn)
        print(f'{fn} : {attr(blob)}')
    except:
        print(f'failed to run {fn}')
        print(traceback.format_exc())
