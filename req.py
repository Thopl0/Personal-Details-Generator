import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}


def get_html(url):
    r = requests.get(url, headers=headers)
    
    soup = bs(r.text, "html.parser")

    return soup

if __name__ == "__main__":
    get_html()