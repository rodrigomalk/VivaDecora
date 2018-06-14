
import requests
from bs4 import BeautifulSoup

class GitHubScrapper(object):

    def get_links(self, url):
        html_tree = self.get_tree(url)
        for element in html_tree.find_all(self.filter):
            yield element.attrs.get('href')

    def filter(self, tag):
        return tag.name == 'a' and tag.attrs.get('class', '') == ['js-navigation-open'] and not tag.attrs.get('rel')

    def get_link_info(self, url):
        html_tree = self.get_tree(url)
        return html_tree.find(class_='file-info').text

    def get_tree(self, url):
        content = requests.get(url).content
        return BeautifulSoup(content, 'html.parser')
