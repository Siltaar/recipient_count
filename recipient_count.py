#!/usr/bin/python3
# coding: utf-8
# author : Simon Descarpentries, 2017-03
# licence: GPLv3

import sys, io
from email.parser import HeaderParser

in_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
hdr_parser = HeaderParser()
eml = hdr_parser.parse(in_stream)
recipient_count = len(eml.get('Bcc', '').split(','))
recipient_count += len(eml.get('Cc', '').split(','))
recipient_count += len(eml.get('To', '').split(','))
print(recipient_count)

