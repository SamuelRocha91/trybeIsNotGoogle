import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if f"{path_file}" in instance.data:
        return
    instance.enqueue(f"{path_file}")
    with open(path_file, "r") as file:
        document = file.read().split('\n')
        dict = {
          "nome_do_arquivo": f"{path_file}",
          "qtd_linhas": len(document),
          "linhas_do_arquivo": document,
         }
    return sys.stdout.write(f"{dict}")


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    path_file = instance.dequeue()
    return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
