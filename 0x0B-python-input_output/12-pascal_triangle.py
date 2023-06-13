#!/usr/bin/python3
"""Defining Pascals triangle"""


def pascal_triangle(n):
    """returns list of lists of ints representing pascal's triangle
    """
    resultList = []

    if n <= 0:
        return []

    for i in range(n):
        if len(resultList) == 0 or len(resultList) == 1:
            resultList.append([1] * (len(resultList) + 1))
            continue
        tempList = [1, 1]
        for i in range(len(resultList[-1]) - 1):
            tempList.insert(i + 1, resultList[-1][i] + resultList[-1][i + 1])
        resultList.append(tempList)
    return resultList
