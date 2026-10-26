import pytest
from bpe.corpus import build_corpus

@pytest.fixture
def example_text() -> str:
    return """This is a test text. Words are separated with whitespaces. No special characters."""

def test_build_corpus_returns_words_with_white_space(example_text):
    """
    All words except the first one in sentences should start with a white space.
    """
    words = build_corpus(example_text)

    assert words, "The corpus should not be empty"
    assert len(words) == 13  # "This", " is", " a", " test", " text.", "Words", " are", " separated", " with", " whitespaces.", "No", " special", " characters."
    for i, word in enumerate(words):
        if i == 0 or words[i-1].endswith("."):
            assert not word.startswith(" ")
        else:
            assert word.startswith(" ")