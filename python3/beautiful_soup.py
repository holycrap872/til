#!/usr/bin/python3
import argparse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def pull_runs(html_path : str) -> None:
    r = requests.get(html_path)
    soup = BeautifulSoup(r.text, 'html.parser')

    for a in soup.find_all('a'):
        print("Clicking on {} goes to {}".format(a.get_text(), a.get('href')))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", help="Path to html file",
                        type=str, required=True)
    args = parser.parse_args()

    pull_runs(args.html)

