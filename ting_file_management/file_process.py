from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None
    fi = txt_importer(path_file)
    d = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(fi),
        "linhas_do_arquivo": (fi)
    }
    instance.enqueue(d)
    sys.stdout.write(str(d))
    return d


def remove(instance):
    if not instance or instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')
    file_to_delete = instance.dequeue()
    file_path = file_to_delete['nome_do_arquivo']
    sys.stdout.write(f'Arquivo {file_path} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        d = instance.search(position)
        sys.stdout.write(str(d))
        return str(d)
    except IndexError:
        sys.stderr.write('Posição inválida')
