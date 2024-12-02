#!/usr/bin/python3

import argparse
import datetime
import os
import requests

COOKIE_ENV_VAR='AOC_COOKIE'

parser = argparse.ArgumentParser(
    description="""
    Get advent of code test data for the set day.
    Pulls for current day if it is December 1-24, unless otherwise specified.
    A session cookie for your account must be given via environment variable
    '${}' or argument.
    """.format(COOKIE_ENV_VAR))

parser.add_argument(
    '-c',
    '--cookie',
    metavar='COOKIE',
    type=str,
    help='advent of code user session token')
parser.add_argument(
    '-d',
    '--day',
    metavar='DAY',
    type=int,
    help='day to pull data from')
parser.add_argument(
    '-y',
    '--year',
    metavar='YEAR',
    type=int,
    help='year to pull data from')

args = parser.parse_args()

today = datetime.datetime.now()
date_year = args.year if args.year else today.year
date_day = args.day if args.day else today.day
date = datetime.datetime(date_year, 12, date_day)
cookie = args.cookie if args.cookie else os.environ.get('AOC_COOKIE')

if (not cookie):
    print('session cookie required to run')
    exit(1)
if (not date_day in range(1,26)):
    print('day range must be inclusively between 1 and 24')
    exit(1)
if (not date_year in range(2015, today.year+1)):
    print('year must be between 2015 and {}'.format(today.year))
    exit(1)
if (date > today):
    print('date cannot be in future')
    exit(1)

url = 'https://adventofcode.com/{}/day/{}/input'.format(date_year, date_day)
req = requests.get(url, headers={'cookie':'session={}'.format(cookie)})

print(req.text, end='')
