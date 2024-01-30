#!/usr/bin/python3
""" does something"""

if __name__ == "__main__":
    import sys
    import requests

    resp = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]))

    content = resp.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                content[i].get("sha"),
                content[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
