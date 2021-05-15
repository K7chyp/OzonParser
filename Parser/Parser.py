from OzonStartPage import ParseOzonStartPage
from OzonStartPage import OZON_START_URL
from BaseClassPage import OzonPageParser
from time import sleep


def recursive_parser() -> dict:
    hrefs = ParseOzonStartPage().hrefs_to_products_at_page
    output: list = []
    for href in hrefs:
        sleep(1)
        information: dict = OzonPageParser(
            OZON_START_URL + href[1:]
        ).common_information_about_page
        output.append(information)
    return hrefs