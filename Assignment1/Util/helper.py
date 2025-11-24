import time
import math
import matplotlib.pyplot as plt
from Lecture2 import nsum
from Lecture3 import sort_algorithms as sa


def test_correctness(runs, method, size=15, width=10):
    for i in range(runs):
        input_list = nsum.get_nsum_list(size, width)
        print('Input:', input_list)
        match method:
            case 'brute-force':
                print('Output Brute-Force:', nsum.threesum_brute(input_list))
            case 'pointers':
                print('Output Pointers:', nsum.threesum_pointers(input_list))
            case 'caching':
                print('Output Caching:', nsum.threesum_caching(input_list))
            case 'selection':
                print('Output Selection:', sa.selection_sort(input_list))
            case 'bubble':
                print('Output Bubble:', sa.bubble_sort(input_list))
            case 'insertion':
                print('Output Insertion:', sa.insertion_sort(input_list))
            case 'merge':
                print('Output Merge:', sa.merge_sort(input_list))
            case 'quick':
                print('Output Quick:', sa.quick_sort(input_list))
            case 'improved_quick':
                print('Output Improved Quick:',
                      sa.improved_quick_sort(input_list))
            case _:
                print('Invalid Method')
        print()


def get_time_duration(sz, method):
    lst = nsum.get_nsum_list(sz, 10)
    before = time.time()
    match method:
        case 'brute-force':
            nsum.threesum_brute(lst)
        case 'pointers':
            nsum.threesum_pointers(lst)
        case 'caching':
            nsum.threesum_caching(lst)
        case 'selection':
            sa.selection_sort(lst)
        case 'bubble':
            sa.bubble_sort(lst)
        case 'insertion':
            sa.insertion_sort(lst)
        case 'merge':
            sa.merge_sort(lst)
        case 'quick':
            sa.quick_sort(lst)
        case 'improved_quick':
            sa.improved_quick_sort(lst)
        case _:
            print('Invalid Method')
    duration = time.time() - before
    return round(duration, 3)


def separate_runs(runs_count, method, start, stop, step, show_graph=False):
    duration_array = []
    sizes_array = []
    markers = ['+', 'x', '*', 'o', 's', '^', '>', '<', 'D' 'd']
    for i in range(runs_count):
        sizes = []
        duration = []
        for sz in range(start, stop, step):
            sizes.append(sz)
            duration.append(get_time_duration(sz, method))
        duration_array.append(duration)
        sizes_array.append(sizes)
        if show_graph:
            plt.plot(
                sizes,
                duration,
                marker=markers[i % 10],
                linestyle='none',
                label=f'Run {i+1}'
                )
    if show_graph:
        plt.xlabel(f'list sizes in range {start} to {stop}')
        plt.ylabel('run times with random lists')
        plt.title(f'{method}: Execution Time ({runs_count} Separate Runs)')
        plt.legend(loc='best')
        plt.show()
    return sizes_array, duration_array


def repeated_runs(runs_count, method, start, stop, step, show_graph=False):
    average_sizes = []
    average_duration = []
    sizes_array, duration_array = separate_runs(
        runs_count, method, start, stop, step
        )
    # Calculate average in sizes array
    for i in range(len(sizes_array[0])):
        sum = 0
        for j in range(len(sizes_array)):
            sum += sizes_array[j][i]
        average_sizes.append(sum//len(sizes_array))
    # Calculate average in time array
    for i in range(len(duration_array[0])):
        sum = 0
        for j in range(len(duration_array)):
            sum += duration_array[j][i]
        average_duration.append(round(sum/len(duration_array), 3))
    if show_graph:
        plt.plot(
                average_sizes,
                average_duration,
                marker='x',
                linestyle='none'
                )
        plt.xlabel(f'list sizes in range {start} to {stop}')
        plt.ylabel(
            f'Average of {len(sizes_array)} run times with random lists'
            )
        plt.title(f'{method}: Execution Time (Repeated Runs)')
        plt.show()
    return average_sizes, average_duration


def lin_reg(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(xi * xi for xi in x)

    # slope
    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

    # intercept
    m = (sum_y - k * sum_x) / n

    return round(m, 3), round(k, 3)


def log_log_with_linear_regression(
        average_sizes,
        average_duration,
        method,
        show_graph=False
        ):
    log_sizes = [math.log(s) for s in average_sizes]
    log_duration = [math.log(t) for t in average_duration]
    m, k = lin_reg(log_sizes, log_duration)
    if show_graph:
        print(f"{method} - Estimated time complexity coefficient k = {k:.3f}")
        plt.scatter(log_sizes, log_duration, marker='x', label='log-log data')
    fit_vals = [m + k * x for x in log_sizes]
    pairs = [[log_sizes[i], fit_vals[i]] for i in range(len(log_sizes))]
    pairs.sort(key=lambda x: x[0])
    xs_fit = [p[0] for p in pairs]
    ys_fit = [p[1] for p in pairs]
    if show_graph:
        plt.plot(
            xs_fit, ys_fit,
            linestyle='-',
            label=f'Linear fit (k={k:.3f})'
            )

        plt.xlabel('Logarithm of list sizes')
        plt.ylabel('Logarithm of time duration')
        plt.title(f'Log-Log Plot with Linear Regression Fit k={k:.3f}')
        plt.show()
    return log_sizes, log_duration, m, k
