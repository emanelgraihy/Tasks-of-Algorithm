import time
import random
import matplotlib.pyplot as plt

def insertion_sort_instrumented(arr):
    comparisons = 0
    shifts = 0
    a = arr.copy()
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons, shifts

sizes = [100, 500, 1000, 2000, 3500, 5000]
times_sorted, times_reversed, times_random = [], [], []

print(f"{'n':<6} | {'Sorted (s)':<12} | {'Random (s)':<12} | {'Reversed (s)':<12} | {'Comparisons (Rand)':<18}")
print("-" * 70)

for n in sizes:
    arr_sorted = list(range(n))
    arr_reversed = list(range(n, 0, -1))
    arr_random = [random.randint(1, 10000) for _ in range(n)]

    t0 = time.perf_counter()
    insertion_sort_instrumented(arr_sorted)
    t_sort = time.perf_counter() - t0
    times_sorted.append(t_sort)

    t0 = time.perf_counter()
    comp_rand, _ = insertion_sort_instrumented(arr_random)
    t_rand = time.perf_counter() - t0
    times_random.append(t_rand)

    t0 = time.perf_counter()
    insertion_sort_instrumented(arr_reversed)
    t_rev = time.perf_counter() - t0
    times_reversed.append(t_rev)

    print(f"{n:<6} | {t_sort:<12.6f} | {t_rand:<12.6f} | {t_rev:<12.6f} | {comp_rand:<18}")

plt.figure(figsize=(10, 6))
plt.plot(sizes, times_sorted, 'g-o', label='Sorted Input ~ O(n)')
plt.plot(sizes, times_random, 'b-s', label='Random Input ~ O(n²)')
plt.plot(sizes, times_reversed, 'r-^', label='Reverse-Sorted Input ~ O(n²)')

plt.title('Empirical Analysis of Insertion Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()