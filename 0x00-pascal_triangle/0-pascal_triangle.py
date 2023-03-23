#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    A function that returns a list of lists of integers 
    representing the Pascal's triangle
    """
    if n<=0:
        return []
    for i in range(n):
        num = 1
        print(num, end=" ")

        for j in range(i):
            num = num * (i - j) // (j + 1)
            print(num, end=" ")
    print()
