from secondQuicksort import *
from firstQuicksort import *
from utility import *

import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(200000)

experiment = 'Permutation'

if experiment == 'Permutation':
    # Permutation
    max_i: int = 20
    N: int = 10
    start: float = time.time()
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_input(n) for n in ns]
    for sublist in args:
        random.shuffle(sublist)
    res_quicksort = benchmark(quick_sort_add_sent, args, N)
    res_quick_yar = benchmark(sort_func, args, N)
    end: float = time.time()
elif experiment == 'Reversed':
    # Reversed list
    max_i: int = 14
    N: int = 10
    start: float = time.time()
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_input(n) for n in ns]
    for sublist in args:
        sublist.reverse()
    res_quicksort = benchmark(quick_sort_add_sent, args, N)
    res_quick_yar = benchmark(sort_func, args, N)
    end: float = time.time()
elif experiment == 'Negative':
    # Negative list
    max_i: int = 14
    N: int = 10
    start: float = time.time()
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_negative_input(n) for n in ns]
    res_quicksort = benchmark(quick_sort_add_sent, args, N)
    res_quick_yar = benchmark(sort_func, args, N)
    end: float = time.time()
elif experiment == 'Equal':
    # Equal list
    max_i: int = 16
    N: int = 10
    start: float = time.time()
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_equal_input(n) for n in ns]
    res_quicksort = benchmark(quick_sort_add_sent, args, N)
    res_quick_yar = benchmark(sort_func, args, N)
    end: float = time.time()
else:
    # Random
    max_i: int = 20
    N: int = 10
    start: float = time.time()
    ns = [int(30 * 1.41 ** i) for i in range(max_i)]
    args = [generate_random_input(n) for n in ns]
    res_quicksort = benchmark(quick_sort_add_sent, args, N)
    res_quick_yar = benchmark(sort_func, args, N)

write_latex_tabular(ns, res_quicksort, f'quicksort_tabular_{experiment}.tex')
write_latex_tabular(ns, res_quick_yar, f'quicksort_Yaroslavskiy_tabular_{experiment}.tex')

fig = plt.figure()
ax = fig.gca()
ax.errorbar(ns, res_quicksort[0, :].reshape(len(ns)), res_quicksort[1, :].reshape(len(ns)), capsize=3.0, marker='o')
ax.errorbar(ns, res_quick_yar[0, :].reshape(len(ns)), res_quick_yar[1, :].reshape(len(ns)), capsize=3.0, marker='o')
ax.set_xlabel('Number of elements $n$')
ax.set_ylabel('Time (s)')
ax.set_yscale('log')
ax.legend(['Quicksort algorithm', 'Quicksort Yaroslavskiy algorithm'])
plt.savefig(f'plot_cubic_vs_hashmap_{experiment}.pdf')
plt.show()
