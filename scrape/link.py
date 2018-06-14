
import re


class Link (object):

    def __init__(self, url, parent=None, scrapper=None):
        self.url = url
        self.parent = parent
        self.scrapper = scrapper
        self.info = None
        self.files = []

    def is_folder(self):
        return '/tree' in self.url

    def get_lines(self):
        lines = re.search(r'(.+)lines', self.get_info())
        return int(lines.group(1).strip()) if lines else 0

    def get_bytes(self):
        _bytes = re.search(r'\)\s*(\d+\.*\d*)', self.get_info())
        return float(_bytes.group(1).strip()) if _bytes else 0

    def get_info(self):
        if self.info is None:
            self.info = self.scrapper.get_link_info(self.url)
        return self.info

    def get_depth(self):
        parent = self.parent
        depth = 0
        while parent is not None:
            parent = parent.parent
            depth += 1
        return depth

    def get_name(self):
        return self.url.split('/')[-1]

    def get_extension(self):
        extension = self.url.split('.')[-1]
        if extension.find('/') > 0:
            extension = 'others'
        return extension
