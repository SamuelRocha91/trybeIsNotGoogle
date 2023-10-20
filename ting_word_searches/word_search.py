

def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_search = []
    for i in range(len(instance.data)):
        word_search.append(search_in_lines(instance, word, i, False))
    if len(word_search) == 1 and not word_search[0]["ocorrencias"]:
        return []
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    word_search = []
    for i in range(len(instance.data)):
        word_search.append(search_in_lines(instance, word, i, True))
    if len(word_search) == 1 and not word_search[0]["ocorrencias"]:
        return []
    return word_search


def search_in_lines(file, word, i, bool):
    with open(file.data[i], "r") as document:
        lines = document.read().split('\n')
        dict = {
              "nome_do_arquivo": f"{file.data[0]}",
              "linhas_do_arquivo": lines,
            }
    occurrences = []
    for j in range(len(dict["linhas_do_arquivo"])):
        if word in dict["linhas_do_arquivo"][j].lower() and bool:
            occurrences.append({"linha": j + 1, "conteudo":
                                dict["linhas_do_arquivo"][j]})
        elif word in dict["linhas_do_arquivo"][j].lower():
            occurrences.append({"linha": j + 1})
    return {
        "palavra": word,
        "arquivo": dict["nome_do_arquivo"],
        "ocorrencias": occurrences,
    }
