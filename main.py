
from datetime import datetime
from scrape.project_files import ProjectFiles
from scrape.git_hub_scrapper import GitHubScrapper
from scrape.file import file_opened
DOMAIN = 'https://github.com'

def main():

    print('[INICIO.{_date:%Y/%m/%d %H:%M:%S}]'.format(_date=datetime.now()))

    for project in file_opened('repositories.txt'):

        print('[{projeto}]'.format(projeto=project))

        project_files = ProjectFiles(project, domain = DOMAIN, scrapper = GitHubScrapper)
        files = list(reversed(list(project_files.list_files())))
        result = dict()
        all_lines = 0
        all_bytes = 0

        for project_file in files:
            if not project_file.is_folder():
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

        print('Extensão')

        for extension in result:
            lines = result[extension]['lines']
            _bytes = round(result[extension]['bytes'], 2)
            lines_percent = round(100 * lines / all_lines, 2)
            bytes_percent = round(100 * _bytes / all_bytes, 2)
            print('{extension}: linhas={lines} ({lines_percent}%)  bytes={bytes} ({bytes_percent}%)'.format(
                extension=extension,
                lines=lines,
                lines_percent=lines_percent,
                bytes=_bytes,
                bytes_percent=bytes_percent
            ))

        print('\nArvore de diretórios:')

        for project_file in files:
            print('\t' * project_file.get_depth() + project_file.get_name())

    print('[FIM.{_date:%Y/%m/%d %H:%M:%S}]'.format(_date=datetime.now()))

if '__main__' == __name__:
    main()