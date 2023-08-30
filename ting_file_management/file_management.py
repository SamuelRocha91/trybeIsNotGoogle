import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        with open(path_file, "r") as file:
            if '.txt' not in path_file:
                sys.stderr.write("Formato inválido")
            document = file.read().split('\n')
            return document
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
