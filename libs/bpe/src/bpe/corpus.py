import re

def build_corpus(text: str) -> list[str]:
    words = []

    for sentence in re.split(r'(?<=[.!?])\s+', text):
        for i, word in enumerate(sentence.split()):
            if i == 0:
                words.append(word)
            else:
                words.append(" " + word)

    return words

def prepare_corpus(words: list[str]) -> list[list[str]]:
    return [list(word) for word in words]


def get_most_frequent_adjacent_token_pair(corpus: list[list[str]], vocabulary: set[str]) -> tuple[str, str] | None:
    frequency_pairs = {}

    for word in corpus:
        for i in range(len(word) - 1):
            pair = (word[i], word[i + 1]) # AB  A - i B - i+1
            if pair[0] in vocabulary and pair[1] in vocabulary:
                frequency_pairs[pair] = frequency_pairs.get(pair, 0) + 1

    if not frequency_pairs:
        return None

    return max(frequency_pairs, key=frequency_pairs.get)

def update_corpus(corpus: list[list[str]], pair: tuple[str, str]) -> list[list[str]]:
    new_corpus = []
    merged_token = "".join(pair)
    for word in corpus:
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                new_word.append(merged_token)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_corpus.append(new_word)
    return new_corpus