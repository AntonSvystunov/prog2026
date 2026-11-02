

def build_vocab(corpus: list[str]) -> set[str]:
    result = set()

    for word in corpus:
        result = result.union(list(word))

    return result