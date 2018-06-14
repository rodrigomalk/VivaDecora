
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
                self.deepening_list(file, 1)
        return self.files_ordened

    def deepening_list(self, parent, depth):
        for file in self.files:
            name = ''
            cont = depth
            if file.parent == parent:
                while cont > 0:
                    name += '    '
                    cont -= 1
                name += '|_...' + file.get_name()
                self.files_ordened.append(name)
                if file.is_folder():
                    depth += 1
                    self.files.remove(file)
                    self.deepening_list(file, depth)

    def print_tree(self):
        self.list()
        pprint(self.files_ordened)
