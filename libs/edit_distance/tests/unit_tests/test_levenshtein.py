from edit_distance.levenshtein import levenshtein
import pytest


@pytest.mark.parametrize(
    "word1, word2, expected_score",
    [
        ("kitten", "sitting", 5),
        ("flaw", "lawn", 2),
        ("intention", "execution", 8),
        ("", "", 0),
        ("a", "", 1),
        ("", "a", 1),
    ],
)
def test_levenshtein_returns_correct_scores(
    word1: str, word2: str, expected_score: int
):
    assert levenshtein(word1, word2) == expected_score
