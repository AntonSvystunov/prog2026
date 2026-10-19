from .base import Algorithm

from .damerau import damerau


def similarity(source: str, target: str, algorithm: Algorithm | None = None) -> float:
    if algorithm is None:
        algorithm = damerau

    return 1 - algorithm(source, target) / max(len(source), len(target))
