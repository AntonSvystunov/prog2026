from .utils import _init_matrix


def _damerau_sub_cost(source: str, target: str) -> int:
    return 1 if source != target else 0


def damerau(source: str, target: str) -> int:
    n = len(source)
    m = len(target)

    D = _init_matrix(n + 1, m + 1)

    D[0][0] = 0

    for i in range(1, n + 1):
        D[i][0] = i
    for j in range(1, m + 1):
        D[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = _damerau_sub_cost(source[i - 1], target[j - 1])
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + cost,
            )

            if (
                i > 1
                and j > 1
                and source[i - 1] == target[j - 2]
                and source[i - 2] == target[j - 1]
            ):
                D[i][j] = min(D[i][j], D[i - 2][j - 2] + 1)

    return D[-1][-1]
