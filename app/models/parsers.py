import requests
import unittest
from bs4 import BeautifulSoup
import re
from bs4 import BeautifulSoup


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    # print(soup)
    for link in soup.findAll('a', attrs={'href': re.compile("^https?://.*(youtu)")}):
        links.append(link.get('href'))

    return links

# class ImageParser:
#     """The summary line for a class docstring should fit on one line.
#
#     If the class has public attributes, they may be documented here
#     in an ``Attributes`` section and follow the same formatting as a
#     function's ``Args`` section. Alternatively, attributes may be documented
#     inline with the attribute's declaration (see __init__ method below).
#
#     Properties created with the ``@property`` decorator should be documented
#     in the property's getter method.
#
#     Attributes:
#         attr1 (str): Description of `attr1`.
#         attr2 (:obj:`int`, optional): Description of `attr2`.
#
#     """
#     pass
#
#
# class TextParser:
#     """
#         This class parses refined data into youtube data api param(singer, song, etc)
#
#
#     Attributes:
#         attr1 (str): Description of `attr1`.
#         attr2 (:obj:`int`, optional): Description of `attr2`.
#
#     """
#
#     def __init__(self, raw_data=None):
#         self.raw_data = raw_data
#
#
# class LinkParser:
#     """
#         This class is web scrapper.
#         It scraps all youtube links from input link's html(one or more).
#         And then pass scrapped texts to TextParser class.
#
#         Attributes:
#             attr1 (str): Description of `attr1`.
#             attr2 (:obj:`int`, optional): Description of `attr2`.
#
#     """
#     pass
