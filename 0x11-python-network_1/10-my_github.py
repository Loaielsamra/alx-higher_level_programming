#!/usr/bin/python3
"""takes GitHub credentials (username and password)
and uses the GitHub API to display id"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = requests.get('https://api.github.com/user', auth=auth)
    print(resp.json().get("id"))
