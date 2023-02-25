from bs4 import BeautifulSoup
import requests
import time
import xml.etree.ElementTree as ET



def g(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(func.__name__, time.perf_counter() - start)
        return res

    return inner


# class “one-row”


class parsing_part:
    def __init__(self):
        self.urls_list = []
        self.__inisialization()

    def __inisialization(self):
        files = {"main_page.aspx": "https://rss.jpost.com/rss/rssfeedsfrontpage.aspx"}
        for file, url in files.items():
            with open(file, 'w', encoding='UTF-8') as inf:
                inf.write(requests.get(url).text)
    @g
    def get_links(self, file, page_type="home page"):
        tree = ET.parse(file)
        root = tree.getroot()
        for neighbor in root.iter('link'):
            self.urls_list.append((neighbor.text, page_type))
    def database_sending(self):
        print(self.urls_list)
#0.6857387000000001