from BaseClassBrowser import BaseClassPageSettings

class OzonPageParser(BaseClassPageSettings):
    def __init__(self, url): 
        self.url = url
        super().__init__(self.url)
        self.browser.close()
    