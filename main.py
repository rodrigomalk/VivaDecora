from pprint import pprint
from datetime import datetime
from project_files import *
from git_hub_scrapper import *
from file import *
DOMAIN = 'https://github.com'

def main():

    print('[INICIO.{_date:%Y/%m/%d %H:%M:%S}]'.format(_date=datetime.now()))

    for project in file_opened('repositories.txt'):

        print('[{projeto}]'.format(projeto=project))

        project_files = ProjectFiles(project, domain = DOMAIN, scrapper = GitHubScrapper)
        files = list(project_files.list_files())
        result = dict()
        all_lines = 0
        all_bytes = 0

        for project_file in files:
            if project_file.extension not in result:
                result[project_file.extension] = {
                    'lines': 0,
                    'lines_percent': 0.0,
                    'bytes': 0.0,
                    'bytes_percent': 0.0
                }
            all_lines += project_file.get_lines()
            all_bytes += project_file.get_bytes()
            result[project_file.extension]['lines'] += project_file.get_lines()
            result[project_file.extension]['bytes'] += project_file.get_bytes()
        for project_file in files:
            result[project_file.extension]['lines_percent'] = '(' + str(round(100 * result[project_file.extension]['lines'] / all_lines, 2)) + '%)'
            result[project_file.extension]['bytes_percent'] = '(' + str(round(100 * result[project_file.extension]['bytes'] / all_bytes, 2)) + '%)'
        pprint(result)
        project_files.print_tree()

    print('[FIM.{_date:%Y/%m/%d %H:%M:%S}]'.format(_date=datetime.now()))

if '__main__' == __name__:
    main()
