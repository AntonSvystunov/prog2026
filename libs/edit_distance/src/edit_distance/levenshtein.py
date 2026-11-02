from .utils import _init_matrix

def del_cost(source: str) -> int:
    return 1


def ins_cost(source: str) -> int:
    return 1


def sub_cost(source: str, target: str) -> int:
    return 2 if source != target else 0


def levenshtein(source: str, target: str) -> int:
    n = len(source)
    m = len(target)

    D = _init_matrix(n + 1, m + 1)

    D[0][0] = 0

    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + del_cost(source[i - 1])

    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + ins_cost(target[j - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(
                D[i - 1][j] + del_cost(source[i - 1]),
                D[i - 1][j - 1] + sub_cost(source[i - 1], target[j - 1]),
                D[i][j - 1] + ins_cost(target[j - 1]),
            )

    return D[-1][-1]