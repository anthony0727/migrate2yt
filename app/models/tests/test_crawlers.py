import unittest

from ..crawlers import *

import selenium

class TestCrawlers(unittest.TestCase):
    def test_get_a_row(self):
        chrome = selenium.webdriver.Chrome()
        chrome.get()

    def test2(self):
        pass
