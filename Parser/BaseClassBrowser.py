import os
from bs4 import BeautifulSoup
from selenium import webdriver

PROXY = "188.166.125.206:37161"


class BaseClassPageSettings:
    def __init__(self, url):
        self.url = url
        self.set_browser()
        self.get_html()
        self.soup = BeautifulSoup(self.html, "lxml")

    def set_browser(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("--proxy-server=%s" % PROXY)
        self.browser = webdriver.Chrome(
            str(os.path.dirname(os.path.realpath(__file__)))
            + "/SeleniumFiles/chromedriver",
            options=self.options,
        )

    def get_html(self) -> None:
        self.browser.get(self.url)
        self.html: list = self.browser.page_source
