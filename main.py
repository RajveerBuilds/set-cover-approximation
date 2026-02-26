import itertools
import random
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Reproducibility
random.seed(42)
np.random.seed(42)

def generate_instance(universe_size, num_sets, max_set_size):
    universe = set(range(universe_size))
    sets = []
    for _ in range(num_sets):
        size = random.randint(1, max_set_size)
        subset = set(random.sample(list(universe), size))
        sets.append(subset)
    return universe, sets

def greedy_set_cover(universe, sets):
    uncovered = set(universe)
    chosen = []

    while uncovered:
        best_set = max(sets, key=lambda s: len(s & uncovered))
        if len(best_set & uncovered) == 0:
            break  # no progress possible, avoid infinite loop
        chosen.append(best_set)
        uncovered -= best_set

    return chosen

def brute_force_bounded(universe, sets, max_combinations=15000):
    checked = 0
    n = len(sets)
    for r in range(1, n + 1):
        for combo in itertools.combinations(range(n), r):
            checked += 1
            if checked > max_combinations:
                return None  # give up if too expensive
            covered = set()
            for idx in combo:
                covered |= sets[idx]
            if covered == universe:
                return [sets[i] for i in combo]
    return None

def run_experiment(max_n):
    sizes = list(range(5, max_n + 1))
    greedy_sizes = []
    brute_sizes = []
    greedy_times = []
    brute_times = []

    for n in sizes:
        print(f"Running n={n} ...")
        universe_size = n
        num_sets = n
        max_set_size = max(2, n // 2)

        universe, sets = generate_instance(universe_size, num_sets, max_set_size)

        start = time.time()
        greedy_solution = greedy_set_cover(universe, sets)
        greedy_times.append(time.time() - start)
        greedy_sizes.append(len(greedy_solution))

        if n <= 6:
            start = time.time()
            brute_solution = brute_force_bounded(universe, sets, max_combinations=5000)
            brute_times.append(time.time() - start)
            brute_sizes.append(len(brute_solution) if brute_solution else None)
        else:
            brute_times.append(None)
            brute_sizes.append(None)

    return sizes, greedy_sizes, brute_sizes, greedy_times, brute_times

def plot_results(sizes, greedy_sizes, brute_sizes, greedy_times, brute_times):
    plt.figure()
    plt.plot(sizes, greedy_sizes, label="Greedy solution size")
    plt.plot(sizes, [b if b is not None else np.nan for b in brute_sizes], label="Bounded brute-force (optimal when available)")
    plt.xlabel("Problem size")
    plt.ylabel("Number of sets selected")
    plt.title("Solution quality: Greedy vs Optimal (bounded brute-force)")
    plt.legend()
    plt.savefig("solution_quality.png")
    plt.close()

    plt.figure()
    plt.plot(sizes, greedy_times, label="Greedy runtime")
    plt.plot(sizes, [t if t is not None else np.nan for t in brute_times], label="Bounded brute-force runtime")
    plt.xlabel("Problem size")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime: Greedy vs Optimal (bounded brute-force)")
    plt.legend()
    plt.savefig("runtime_comparison.png")
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set Cover: Greedy Approximation vs Bounded Brute Force")
    parser.add_argument("--max_n", type=int, default=12, help="Max problem size to test")
    args = parser.parse_args()

    sizes, greedy_sizes, brute_sizes, greedy_times, brute_times = run_experiment(args.max_n)
    plot_results(sizes, greedy_sizes, brute_sizes, greedy_times, brute_times)