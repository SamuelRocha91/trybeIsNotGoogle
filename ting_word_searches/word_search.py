

def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_search = []
    for i in range(len(instance.data)):
        with open(instance.data[i], "r") as file:
            lines = file.read().split('\n')
            dict = {
              "nome_do_arquivo": f"{instance.data[i]}",
              "qtd_linhas": len(lines),
              "linhas_do_arquivo": lines,
             }
            new_dict = search_in_lines(dict, word)
            word_search.append(new_dict)
    if len(word_search) == 1 and not word_search[0]["ocorrencias"]:
        return []
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


def search_in_lines(file, word):
    occurrences = []
    for i in range(len(file["linhas_do_arquivo"])):
        if word in file["linhas_do_arquivo"][i].lower():
            occurrences.append({"linha": i + 1})
    return {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": occurrences,
    }
