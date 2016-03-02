from sys import stderr
import urllib2
from urlparse import urljoin

from bs4 import BeautifulSoup

page = 'http://disney.wikia.com/wiki/Descendants'


def main():
    print list(hero_info())


def hero_info():
    markup = urllib2.urlopen(page).read()
    doc = BeautifulSoup(markup,  "lxml")
    
    hd = doc.find(id="The_Descendants").parent
    # print hd
    character_list = hd.find_next_sibling("ul")
    for link in character_list.find_all('a'):
        # print link
        there = urljoin(page, link.get('href'))
        # print there
        try:
            src = character_image(there)
        except Exception as ex:
            print >>stderr, "TODO: fix the bug!", ex

        yield there, src  # TODO: talk about generators


def character_image(addr):
    markup = urllib2.urlopen(addr).read()
    doc = BeautifulSoup(markup, "lxml")
    img = doc.select('img.pi-image-thumbnail')[0]
    return img.get('src')



if __name__ == '__main__':
    main()
