import requests
from bs4 import BeautifulSoup


class PageParser:
    def __init__(self, page_url):
        self.page_url = page_url

    def _get_page_html(self) -> str:
        html = requests.get(self.page_url)
        return html.text.strip()

    def get_page_text(self) -> str:
        soup = BeautifulSoup(self._get_page_html(), 'lxml')
        return soup.text
