import numpy as np
from time import time


def f(x):
    x2 = x * x
    return np.cos(x2) * np.exp(-x2 / 2) / np.sqrt((2 * np.pi))


def methode(arg):
    # Gauss-Legendre three-point formula
    a, b, n, s = arg

    wi = (b - a) / n
    xi = np.linspace(a, b, n + 1)
    mid = (xi[:-1] + xi[1:]) * 0.5

    p = (wi * np.sqrt(3)) / (2 * np.sqrt(5))  # p for points

    return (wi / 18) * np.sum(5 * f(mid - p) + 8 * f(mid) + 5 * f(mid + p))


def pool_liste(arg, np_cpu):
    A, B, N, seed = arg
    pool_N = N // np_cpu
    rest = N % np_cpu
    pr = np.linspace(A, B, np_cpu + 1)  # pool range
    liste = [(pr[i], pr[i + 1], pool_N, seed + i) for i in range(np_cpu)]
    liste.append((pr[np_cpu - 1], pr[np_cpu], pool_N + rest, seed + np_cpu))
    return liste


if __name__ == "__main__":
    import multiprocessing as mp

    N = 10**7
    A = -np.sqrt(np.pi / 2)
    B = np.sqrt(np.pi / 2)
    seed = int(time())

    arg = (A, B, N, seed)

    tmp = time()
    print(methode((arg)))
    print(time() - tmp, "without parallelization")

    liste = pool_liste(arg, mp.cpu_count())

    tmp = time()
    with mp.Pool(processes=mp.cpu_count()) as pool:
        print(sum(pool.imap(methode, liste)))
    print(time() - tmp, "with parallelization")
