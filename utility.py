from typing import List, Tuple, Optional, Dict, \
    Callable, Any
import time
import csv
import random
import numpy as np
import math

def measure(f: Callable[[], Any]) -> float:
    start: float = time.time()
    f()
    end: float = time.time()
    return end - start


def benchmark(f: Callable, args: List[List[int]],
              N: int) -> np.ndarray:
    m: int = len(args)
    M: np.ndarray = np.zeros((m, N))
    for i in range(len(args)):
        print(i)
        arg: List[int] = args[i]
        for j in range(N):
            M[i, j] = measure(lambda: f(arg, 0, len(arg) - 1))
    means = np.mean(M, axis=1).reshape(m, 1)
    stdevs = np.std(M, axis=1, ddof=1).reshape(m, 1)
    return np.stack([means, stdevs])


def generate_input(n: int) -> List[int]:
    return [i for i in range(1, n + 1)]


def write_csv(ns: List[int], res: np.ndarray,
              filename: str):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for i in range(len(ns)):
            writer.writerow([ns[i]] + res[:, i].tolist())
        f.close()


def write_latex_tabular(ns: List[int],
                        res: np.ndarray,
                        filename: str):
    with open(filename, 'w') as f:
        f.write(r'\begin {tabular}{rrr}' + '\n')
        f.write(r'$n$ & Average & Standard deviation')
        f.write(r'\\ \hline ' + '\n')
        for i in range(len(ns)):
            fields = [str(ns[i]),
                      '{:.6f}'.format(res[0, i, 0]),
                      '{:.6f}'.format(res[1, i, 0])]
            f.write(' & '.join(fields) + r'\\ ' + '\n')
        f.write(r'\end{tabular}' + '\n')
        f.close()


def generate_input(n: int) -> List[int]:
    return [i for i in range(1, n + 1)]


def generate_negative_input(n: int) -> List[int]:
    return [i for i in range(0, -n, -1)]


def generate_equal_input(n: int) -> List[int]:
    return [n for i in range(1, n + 1)]


def generate_random_input(n: int) -> List[int]:
    list = []
    for i in range(n):
        random_int = random.randint(1, int(math.sqrt(n)))
        list.append(random_int)
    return list
