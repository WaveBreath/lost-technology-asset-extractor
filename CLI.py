# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:53:58 2018

@author: yiyuezhuo
"""

import argparse
import decoder

parser = argparse.ArgumentParser(description='Lost technology asset decoder')
parser.add_argument('source_dir')
parser.add_argument('dest_dir')
parser.add_argument('-s','--silent', help="Print nothing when processing",
                    action='store_const', const=True, default=False)

args = parser.parse_args()

decoder.decode_map(args.source_dir, args.dest_dir, verbose = not args.silent)