from textcrunch import TextCruncher
from siteparser import PageParser

PAGE_URL = 'https://docs.djangoproject.com/en/4.0/intro/tutorial01/'


def create_file_words(page_url):
    page_parser = PageParser(page_url)
    text = page_parser.get_page_text()

    tc = TextCruncher(text)
    words = tc.crunch_to_words()
    with open('page1words.txt', 'w') as file:
        file.write('\n'.join(words))



