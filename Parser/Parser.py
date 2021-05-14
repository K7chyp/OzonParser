from OzonStartPage import ParseOzonStartPage
from OzonStartPage import OZON_START_URL
from BaseClassPage import OzonPageParser

hrefs = ParseOzonStartPage().hrefs_to_products_at_page
for href in hrefs:
    information: dict = OzonPageParser(
        OZON_START_URL + href[1:]
    ).common_information_about_page
