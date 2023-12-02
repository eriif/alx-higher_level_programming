#!/usr/bin/python3
"""
a function that Uses the GitHub API to display
GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
- Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    uth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
