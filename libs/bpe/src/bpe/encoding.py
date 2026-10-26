from bpe.corpus import build_corpus, prepare_corpus, get_most_frequent_adjacent_token_pair, update_corpus
from bpe.utils import build_vocab

def train_bpe(input_corpus: str | list[str], num_merges: int) -> set[str]:
    """
    Trains BPE encoding on the given text for a specified number of merges.
    Return the set of learned BPE tokens.
    """
    if isinstance(input_corpus, str):
        words = build_corpus(input_corpus)
    else:
        words = input_corpus
    corpus = prepare_corpus(words)
    vocabulary = build_vocab(words)

    for _ in range(num_merges):
        pair = get_most_frequent_adjacent_token_pair(corpus, vocabulary)
        if not pair:
            break
        corpus = update_corpus(corpus, pair)
        merged_token = "".join(pair)
        vocabulary.add(merged_token)

    return vocabulary
