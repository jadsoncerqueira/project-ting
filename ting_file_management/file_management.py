import sys


def txt_importer(path_file):
    ext = ".txt"
    if ext not in path_file:
        return sys.stderr.write("Formato inválido")
    try:
        with open(path_file) as file:
            d = file.readlines()
            lis = []
            for linha in d:
                lis.append(linha.rstrip("\n"))
            return lis
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
