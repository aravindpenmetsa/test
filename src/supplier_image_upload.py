#!/usr/bin/env python3

import os
import sys
import requests

# This is a one time script, so not adding UTs.

url = "http://localhost/upload/"
dir_path = sys.argv[1]
for file in os.listdir(dir_path):
    if not file.endswith('.jpeg'):
        continue
    absolute_path = os.path.join(dir_path, file)
    with open(absolute_path, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
    print("Posted")
