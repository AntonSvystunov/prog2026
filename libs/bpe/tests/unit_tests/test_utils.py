from bpe.utils import build_vocab

def test_build_vocab_returns_vocab():
    corpus = [
        "ABC",
        "BCD",
        "ABDBABDB",
        "ABDFBDBAA"
    ]

    vocab = build_vocab(corpus)

    assert len(vocab) == 5

