import fileinput
import json
import re
import urllib.request as request
import sys


for line in fileinput.input():
    try:
        if "doi={" in re.sub("\s+", "", line).lower():
            doi = re.search("{(.+)}", line).group(1)
            data = json.load(request.urlopen("http://shortdoi.org/%s?format=json" % doi))
            print(line.replace(doi, data["ShortDOI"]), end="")
        else:
            print(line, end="")
    except Exception as err:
        print(err, file=sys.stderr)
        print(line, end="")
