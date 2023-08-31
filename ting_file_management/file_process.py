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
    sys.stdout.write(f"{dict}")
    return dict


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    path_file = instance.dequeue()
    return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if not 0 <= position < len(instance.data):
        return sys.stderr.write("Posição inválida")
    document = instance.search(position)
    with open(document, "r") as file:
        data = file.read().split('\n')
        dict = {
          "nome_do_arquivo": f"{document}",
          "qtd_linhas": len(data),
          "linhas_do_arquivo": data,
         }
    sys.stdout.write(f"{dict}")
