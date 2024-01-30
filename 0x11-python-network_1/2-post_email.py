#!/usr/bin/python3
"""that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    import sys

    values = {"email": sys.argv[2]}
    data = parse.urlencode(values).encode('ascii')

    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as resp:
        body = resp.read()
        print(body.decode('utf-8'))
