
def file_opened(file_path):
    with open(file_path) as file:
        return file.read().splitlines()
