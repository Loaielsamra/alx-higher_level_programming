#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib import error

    try:
        with request.urlopen(sys.argv[1]) as content:
            content = content.read()
            print(content.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
