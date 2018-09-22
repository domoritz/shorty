import fileinput
import json
import re
import urllib.request as request
import sys

regex_doi = r"doi\s?=\s?[{\"']([^}\"']+)[}\"']"
regex_url = r"url\s?=\s?[{\"'](https?://doi\.org/([\w\.]+/[^}/\"']+))/?[}\"']"


for line in fileinput.input():
    try:
        search_doi = re.search(regex_doi, re.sub("\s+", "", line), re.IGNORECASE)
        search_url = re.search(regex_url, re.sub("\s+", "", line), re.IGNORECASE)
        doi = (
            (search_doi and search_doi.group(1)) or
            (search_url and search_url.group(2))
        )

        if doi:
            short_doi = data["shortDOI"][3:] if search_url else data["shortDOI"]
            data = json.load(request.urlopen("http://shortdoi.org/%s?format=json" % doi))
            print(line.replace(doi, short_doi, end="")
        else:
            print(line, end="")
    except Exception as err:
        print(err, file=sys.stderr)
        print(line, end="")
