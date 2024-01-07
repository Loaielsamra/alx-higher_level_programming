#!/usr/bin/python3
"""takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    data = {"email": sys.argv[2]}
    resp = responses.post(sys.argv[1], params=data)
    print(resp.text)
