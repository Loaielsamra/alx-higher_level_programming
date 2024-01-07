#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}

    resp = requests.post("http://0.0.0.0:5000/search_user", params=data)
    content = resp.json()

    try:
        if content != {}:
            print("[{}] {}".format(content.get("id"), content.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
