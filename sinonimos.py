#!/usr/bin/env python3

import bs4
import requests
import sys

CLASS = "class"

word_to_search = sys.argv[1]
url = "https://www.sinonimos.com.br/" + word_to_search

request_html = requests.get(url)
soup = bs4.BeautifulSoup(request_html.text, "html.parser")

related_words = []

wrappers = soup.findAll("div", {CLASS: "s-wrapper"})
for wrapper in wrappers:
    synonms = wrapper.findAll("a", {CLASS: "sinonimo"})
    for synon in synonms:
        related_words.append(synon.get_text())

print("Related words:")
for word in related_words:
    print("  --> ", word)


