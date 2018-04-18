# -*- coding: utf-8 -*-
from collections import deque


def solution(A, K):
    if len(A) == 0:
        return A

    if K >= len(A):
        K %= len(A)

    return A[-K:] + A[:-K]


def solution2(A, K):
    items = deque(A)
    items.rotate(K)

    return list(items)


if __name__ == "__main__":
    A = [3, 8, 9, 7, 6]
    K = 7
    print(solution(A, K))
    print(solution2(A, K))
