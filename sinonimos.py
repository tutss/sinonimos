#!/usr/bin/env python3

import bs4
import requests
import sys

CLASS = "class"

word_to_search = sys.argv[1]
url = "https://www.sinonimos.com.br/" + word_to_search

request_html = requests.get(url)
soup = bs4.BeautifulSoup(request_html.text, "html.parser")

meaning_and_words = dict()

wrappers = soup.findAll("div", {CLASS: "s-wrapper"})
for wrapper in wrappers:
    related_words = []
    
    meaning = wrapper.find_next("div", {CLASS: "sentido"})
    synonms = wrapper.findAll("a", {CLASS: "sinonimo"})
    for synon in synonms:
        related_words.append(synon.get_text())
    
    meaning_and_words[meaning.get_text()[:-1]] = related_words

print("====== Palavras relacionadas ======")
for mean in meaning_and_words.keys():
    print("{}:".format(mean))
    words = meaning_and_words[mean]
    for word in words:
        print(" ----> {}".format(word))


