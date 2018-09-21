import fileinput
import json
import re
import urllib.request as request
import sys


for line in fileinput.input():
    try:
        if "doi={" in line.replace(' ', '').lower():
            doi = re.search('{(.+)}', line).group(1)
            data = json.load(request.urlopen('http://shortdoi.org/%s?format=json' % doi))
            print('\tdoi = {%s},' % data['ShortDOI'])
        else:
            print(line, end='')
    except Exception as err:
        print(err, file=sys.stderr)
        print(line, end='')
