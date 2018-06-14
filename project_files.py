
from link import*
from pprint import pprint

class ProjectFiles(object):

    def __init__(self, url, domain = None, scrapper = None):

        if not url.startswith('/'):
            url = "/" + url
        self.url = url
        self.domain = domain
        self.scrapper = scrapper()
        self.files = []
        self.files_ordened = []

    def list_files(self, url = None, parent = None):
        if url is None:
            url = self.url

        for link in self.scrapper.get_links(self.domain + url):
            link_file = Link(self.domain + link, parent, scrapper = self.scrapper)
            self.files.append(link_file)
            if link_file.is_folder():
                yield from self.list_files (link, parent = link_file)
            else:
                yield link_file

    def list(self):
        for file in self.files:
            file.get_depth()
            if file.is_folder():
                self.files_ordened.append(file.get_name())
                self.files.remove(file)
                self.deepening_list(file)
        return self.files_ordened

    def deepening_list(self, parent):
        for file in self.files:
            if file.parent == parent:
                self.files_ordened.append(file.get_name())
                self.files.remove(file)
                if file.is_folder():
                    self.files_ordened.append(file.get_name())
                    self.files.remove(file)
                    self.deepening_list(file)

    def print_tree(self):
        self.list()
        pprint(self.files_ordened)
