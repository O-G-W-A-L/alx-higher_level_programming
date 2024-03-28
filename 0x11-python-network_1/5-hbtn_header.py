#!/usr/bin/python3
"""
displaying the value of the variable X-Request-Id
of a request to a given url
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
