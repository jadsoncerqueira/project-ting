def find_word_in_lines(word, file):
    ocorrencias = []

    for idx, line in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            ocorrencias.append(
                {
                    "linha": idx + 1,
                    "conteudo": line
                }
            )

    return ocorrencias


def get_word_occurrences_in_files(word, instance, type):
    search = {
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }

    all_word_searched = []

    # O(n²)
    for index in range(0, len(instance)):
        file = instance.search(index)
        search["arquivo"] = file["nome_do_arquivo"]
        if type == 'exists':
            search["ocorrencias"] = [
                {"linha": line["linha"]}
                for line in find_word_in_lines(word, file)
            ]
        elif type == 'search':
            search["ocorrencias"] = find_word_in_lines(word, file)

        if len(search["ocorrencias"]) > 0:
            all_word_searched.append(search)

    return all_word_searched


def exists_word(word, instance):
    return get_word_occurrences_in_files(
        word=word, instance=instance, type='exists'
    )


def search_by_word(word, instance):
    return get_word_occurrences_in_files(
        word=word, instance=instance, type='search'
    )
