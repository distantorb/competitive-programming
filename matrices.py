"""
Inputs are in the following form: the first line contains a single integer, n.
It is followed by 3n lines each containing n integers separated by spaces, coding
the values contained in three n x n matrices. A, B, C given row by row. The goal
is to test if the product A times B is equal to the matrix C. A direct approach 
by matrix multiplication would have a completely O(n3), however, a probabilistic
solution exists in O(n2), which consists in randomly choosing a vector x and 
testing whether A(Bx) = Cx. This is the Frievalds test (1979). What is the 
probability that the algorithmm ontputs equality even if AB =/ C? (mathemtical
notation expected). Whenever the computations are made modulo d, the probability
of error is at most 1/d. This error probability can be made arbitrarily small
by repeating the test several times. The following code has an error probability
bounded above by 10-6.
"""

from random import randint
from sys import stdin

def readint():
    return int(stdin.readline())

def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []

    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M

def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for n in range(n)) for i in range(n)]   

def frievalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, X)) == mult(C, x)

if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)

    print(frievalds(A, B, C))





