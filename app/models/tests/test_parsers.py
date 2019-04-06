import unittest
from bs4 import BeautifulSoup
import re
import requests
from ..parsers import *


class TestParsers(unittest.TestCase):
    def test_get_links(self):
        links = get_links('https://us12.campaign-archive.com/?u=b8884d9c803717ac5a17fbdaa&id=721a0e477e')
        tcase = ["https://youtu.be/p50k_kklM7g",
                 "https://youtu.be/V5YOhcAof8I",
                 "https://youtu.be/vPG02avSFmQ",
                 "https://www.youtube.com/watch?v=g1kDd6yBQZ4",
                 "https://www.youtube.com/watch?v=bs5ZOcU6Bnw"]

        self.assertListEqual(links, tcase, "link parsed wrong")

    def test_text_extraction(self):
        pass
