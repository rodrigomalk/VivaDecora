
import re

class Link (object):

    def __init__(self, url, parent = None, scrapper = None):
        self.url = url
        self.parent = parent
        self.scrapper = scrapper
        self.extension = self.url.split('.')[-1]
        self.info = None

    def is_folder(self):
        return '/tree' in self.url

    def get_lines(self):
        lines = re.search(r'(.+)lines', self.get_info())
        return int(lines.group(1).strip()) if lines else 0

    def get_bytes(self):
        lines = re.search(r'(\d+\.*\d*)', self.get_info())
        return float(lines.group(1).strip()) if lines else 0

    def get_info(self):
        if self.info is None:
            self.info = self.scrapper.get_link_info(self.url)
        return self.info
