from file import*
from project_files import*
from git_hub_scrapper import*
from pprint import pprint

domain = 'https://github.com'

def main():
    for project in file_opened('repositories.txt'):
        project_files = ProjectFiles(project, domain = domain, scrapper = GitHubScrapper)
        result = {}

        for project_file in project_files.list_files():
            if project_file.extension not in result:
                result[project_file.extension] = {
                    'lines': 0,
                    'bytes': 0.0
                }
            result[project_file.extension]['lines'] += project_file.get_lines()
            result[project_file.extension]['bytes'] += project_file.get_bytes()
        pprint(result)

main()
