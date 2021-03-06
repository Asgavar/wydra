#!/usr/bin/env python3.6

import argparse
import datetime

import requests

import config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--what', required=True)
    parser.add_argument('--cost', type=float, required=True)
    parser.add_argument('--where', required=True)
    parser.add_argument(
        '--when', type=lambda d: datetime.datetime.strptime(d, '%d-%m-%Y'),
        required=True
    )
    args = parser.parse_args()
    r = requests.post(config.post_endpoint, data={
        'what': args.what, 'cost': args.cost, 'when': args.when,
        'where': args.where}, auth=('', config.passphrase)
    )
    print(r.text)
