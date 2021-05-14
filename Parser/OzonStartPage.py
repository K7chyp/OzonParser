from BaseClassBrowser import BaseClassPageSettings

OZON_START_URL = "https://www.ozon.ru/"


def get_all_product_hrefs_from_page(soup):
    return [
        part_of_page.get("href")
        for part_of_page in soup.find_all("a")
        if "/product/" in str(part_of_page.get("href"))
    ]


class ParseOzonStartPage(BaseClassPageSettings):
    def __init__(self):
        super().__init__(OZON_START_URL)
        self.hrefs_to_products_at_page = get_all_product_hrefs_from_page(self.soup)
        self.browser.close()