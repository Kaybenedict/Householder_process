# -*- coding: utf-8 -*-
"""fm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pcL2R5YPVLQ1Wu1FPsc-NDZ-s5MHOUC2
"""

import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
from numpy.linalg import norm
A = scipy.array([[0.2479639, 0.1224457, -0.0419480, -0.1930236, -0.2828155 ], [0.4738950, 0.2340117, -0.0801688, -0.3688962, -0.5405016 ],
                 [0.6577185, 0.3247845, -0.1112661, -0.5119907, -0.7501618 ], [0.7831008, 0.3866989, -0.1324771, -0.6095926, -0.8931668  ],
                 [ 0.8389012,  0.4142534, -0.1419169, -0.6530296, -0.9568099], [0.8201616,  0.4049997, -0.1387467, -0.6384420, -0.9354365 ],
                 [ 0.7285469,  0.3597600, -0.1232483, -0.5671260, -0.8309453 ], [0.5721977,  0.2825540, -0.0967987, -0.4454184, -0.6526210 ],
                 [0.3650062,  0.1802418, -0.0617481, -0.2841334, -0.4163084], [0.1253823,  0.0619144, -0.0212109, -0.0976019, -0.1430050]])
Q, R = scipy.linalg.qr(A)

print("A:")
pprint.pprint(A)

print("Q:")
pprint.pprint(Q)

print("R:")
pprint.pprint(R)

from math import sqrt
from pprint import pprint
import scipy

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    # Converts N into a list of tuples of columns
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
    """Take the transpose of a matrix."""
    n = len(M)
    return [[ M[i][j] for i in range(n)] for j in range(n)]

def norm(x):
    """Return the Euclidean norm of the vector x."""
    return sqrt(sum([x_i**2 for x_i in x]))

def Q_i(Q_min, i, j, k):
    """Construct the Q_t matrix by left-top padding the matrix Q
    with elements from the identity matrix."""
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def householder(A):
    def cmp(a, b):
      return (a > b) - (a < b)
    xrange=range
    """Performs a Householder Reflections based QR Decomposition of the
    matrix A. The function returns Q, an orthogonal matrix and R, an
    upper triangular matrix such that A = QR."""
    n = len(A)

    # Set R equal to A, and create Q as a zero matrix of the same size
    R = A
    Q = [[0.0] * n for i in xrange(n)]

    # The Householder procedure
    for k in range(n-1):  # We don't perform the procedure on a 1x1 matrix, so we reduce the index by 1
        # Create identity matrix of same size as A
        I = [[float(i == j) for i in xrange(n)] for j in xrange(n)]

        # Create the vectors x, e and the scalar alpha
        # Python does not have a sgn function, so we use cmp instead
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = -cmp(x[0],0) * norm(x)

        # Using anonymous functions, we create u and v
        u = map(lambda p,q: p + alpha * q, x, e)
        norm_u = norm(u)
        v = map(lambda p: p/norm_u, u)

        # Create the Q minor matrix
        Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in xrange(n-k)] for j in xrange(n-k) ]

        # "Pad out" the Q minor matrix with elements from the identity
        Q_t = [[ Q_i(Q_min,i,j,k) for i in xrange(n)] for j in xrange(n)]

        # If this is the first run through, right multiply by A,
        # else right multiply by Q
        if k == 0:
            Q = Q_t
            R = mult_matrix(Q_t,A)
        else:
            Q = mult_matrix(Q_t,Q)
            R = mult_matrix(Q_t,R)

    # Since Q is defined as the product of transposes of Q_t,
    # we need to take the transpose upon returning it
    return trans_matrix(Q), R

A = scipy.array([[0.2479639, 0.1224457, -0.0419480, -0.1930236, -0.2828155 ], [0.4738950, 0.2340117, -0.0801688, -0.3688962, -0.5405016 ],
                 [0.6577185, 0.3247845, -0.1112661, -0.5119907, -0.7501618 ], [0.7831008, 0.3866989, -0.1324771, -0.6095926, -0.8931668  ],
                 [ 0.8389012,  0.4142534, -0.1419169, -0.6530296, -0.9568099], [0.8201616,  0.4049997, -0.1387467, -0.6384420, -0.9354365 ],
                 [ 0.7285469,  0.3597600, -0.1232483, -0.5671260, -0.8309453 ], [0.5721977,  0.2825540, -0.0967987, -0.4454184, -0.6526210 ],
                 [0.3650062,  0.1802418, -0.0617481, -0.2841334, -0.4163084], [0.1253823,  0.0619144, -0.0212109, -0.0976019, -0.1430050]])
Q, R = householder(A)

print("A:")
pprint(A)

print("Q:")
pprint(Q)

print ("R:")
pprint(R)

from math import sqrt
from pprint import pprint
import scipy
import numpy as np

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    # Converts N into a list of tuples of columns
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
    """Take the transpose of a matrix."""
    n = len(M)
    return [[ M[i][j] for i in range(n)] for j in range(n)]

def norm(x):
    """Return the Euclidean norm of the vector x."""
    return sqrt(sum([x_i**2 for x_i in x]))

def Q_i(Q_min, i, j, k):
    """Construct the Q_t matrix by left-top padding the matrix Q
    with elements from the identity matrix."""
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def householder(A):
    def cmp(a, b):
      a=a.astype(np.float64).astype(np.bool)
      b=b
      return a-b
    xrange=range
    """Performs a Householder Reflections based QR Decomposition of the
    matrix A. The function returns Q, an orthogonal matrix and R, an
    upper triangular matrix such that A = QR."""
    n = len(A)

    # Set R equal to A, and create Q as a zero matrix of the same size
    R = A
    Q = [[0.0] * n for i in xrange(n)]

    # The Householder procedure
    for k in range(n-1):  # We don't perform the procedure on a 1x1 matrix, so we reduce the index by 1
        # Create identity matrix of same size as A
        I = [[float(i == j) for i in xrange(n)] for j in xrange(n)]

        # Create the vectors x, e and the scalar alpha
        # Python does not have a sgn function, so we use cmp instead
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = -cmp(x[0],0) * norm(x)

        # Using anonymous functions, we create u and v
        u = map(lambda p,q: p + alpha * q, x, e)
        norm_u = norm(u)
        new=[]
        v = list(map(lambda p: p/norm_u, u))

        # Create the Q minor matrix
        Q_min = [ [float(i==j) - 2.0 * 1 * 1 for i in xrange(n-k)] for j in xrange(n-k) ]

        # "Pad out" the Q minor matrix with elements from the identity
        Q_t = [[ Q_i(Q_min,i,j,k) for i in xrange(n)] for j in xrange(n)]

        # If this is the first run through, right multiply by A,
        # else right multiply by Q
        if k == 0:
            Q = Q_t
            R = mult_matrix(Q_t,A)
        else:
            Q = mult_matrix(Q_t,Q)
            R = mult_matrix(Q_t,R)

    # Since Q is defined as the product of transposes of Q_t,
    # we need to take the transpose upon returning it
    return trans_matrix(Q), R

A = scipy.array([[0.2479639, 0.1224457, -0.0419480, -0.1930236, -0.2828155 ], [0.4738950, 0.2340117, -0.0801688, -0.3688962, -0.5405016 ],
                 [0.6577185, 0.3247845, -0.1112661, -0.5119907, -0.7501618 ], [0.7831008, 0.3866989, -0.1324771, -0.6095926, -0.8931668  ],
                 [ 0.8389012,  0.4142534, -0.1419169, -0.6530296, -0.9568099], [0.8201616,  0.4049997, -0.1387467, -0.6384420, -0.9354365 ],
                 [ 0.7285469,  0.3597600, -0.1232483, -0.5671260, -0.8309453 ], [0.5721977,  0.2825540, -0.0967987, -0.4454184, -0.6526210 ],
                 [0.3650062,  0.1802418, -0.0617481, -0.2841334, -0.4163084], [0.1253823,  0.0619144, -0.0212109, -0.0976019, -0.1430050]])
Q, R = householder(A)

print("A:")
pprint(A)

print("Q:")
pprint(Q)

print ("R:")
pprint(R)