
from scrape.link import Link


class ProjectFiles(object):

    def __init__(self, url, domain = None, scrapper = None):

        if not url.startswith('/'):
            url = "/" + url
        self.url = url
        self.domain = domain
        self.scrapper = scrapper()
        self.files = []

    def list_files(self, url = None, parent = None):
        if url is None:
            url = self.url

        for link in self.scrapper.get_links(self.domain + url):
            link_file = Link(self.domain + link, parent, scrapper = self.scrapper)
            self.files.append(link_file)
            if link_file.is_folder():
                yield from self.list_files (link, parent = link_file)
            yield link_file