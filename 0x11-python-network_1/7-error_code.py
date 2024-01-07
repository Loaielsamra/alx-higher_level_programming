#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the response.
if the HTTP status code is greater than or equal to 400, prints the value of the
HTTP status code"""

if __name__ == "__main__":
    import sys
    import requests

    resp = requests.get(sys.argv[1])
    if (resp.ok):
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
