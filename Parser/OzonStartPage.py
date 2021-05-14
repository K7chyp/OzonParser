from BaseClassBrowser import BaseClassPageSettings

OZON_START_URL = "https://www.ozon.ru/"


class ParseOzonStartPage(BaseClassPageSettings):
    def __init__(self):
        super().__init__(OZON_START_URL)
        self.get_all_hrefs()
        self.browser.close()

    def get_all_hrefs(self):
        self.hrefs_to_products_at_main_page = [
            part_of_page.get("href")
            for part_of_page in self.soup.find_all("a")
            if "/product/" in str(part_of_page.get("href"))
        ]
