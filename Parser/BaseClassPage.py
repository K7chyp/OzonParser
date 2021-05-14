from BaseClassBrowser import BaseClassPageSettings
from OzonStartPage import get_all_product_hrefs_from_page
from re import findall


class OzonPageParser(BaseClassPageSettings):
    def __init__(self, url):
        self.url = url
        super().__init__(self.url)
        self.common_information_about_page = {}
        self.get_common_information_about_page()
        self.get_hrefs()
        self.browser.close()

    def soup_finder(self, first_tag: str, class_: dict) -> str:
        return self.soup.find(first_tag, class_).text

    def find_digits(self, str_: str) -> str:
        return "".join(findall(r"\d+", str_))

    def get_common_information_about_page(self):
        for name, tag_name, class_name in zip(
            ["header", "tag"],
            ["h1", "dd"],
            [
                {"class": "b3a8"},
                {"class": "db5"},
            ],
        ):
            self.common_information_about_page[name] = self.soup_finder(
                tag_name, class_name
            )

        self.common_information_about_page["price"] = self.find_digits(
            self.soup.find("span", {"class": "c2h5 c2h6"}).text
        )
        self.common_information_about_page["raiting"] = self.find_digits(
            [
                page_content
                for page_content in self.soup.find_all("div", {"class": "kxa6"})
            ][6].text
        )
        self.common_information_about_page["text_information"] = self.soup.find(
            "div", {"class": "b0v2"}
        )
        self.common_information_about_page["href"] = self.url
    
    def get_hrefs(self): 
        self.hrefs_to_products_at_page = get_all_product_hrefs_from_page(self.soup)
