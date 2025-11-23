import time
import math
import nsum
import matplotlib.pyplot as plt


def test_correctness(runs, method):
    for i in range(runs):
        input_list = nsum.get_nsum_list(15, 10)
        print('Input:', input_list)
        match method:
            case 'brute-force':
                print('Output Brute-Force:', nsum.threesum_brute(input_list))
            case 'pointers':
                print('Output Pointers:', nsum.threesum_pointers(input_list))
            case 'caching':
                print('Output Caching:', nsum.threesum_caching(input_list))
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
        plt.title(f'{method}: 3-Sum Execution Time ({runs_count} Separate Runs)')
        plt.legend(loc='best')
        plt.show()
    return sizes_array, duration_array



def repeated_runs(runs_count, method, start, stop, step):
    average_sizes = []
    average_duration = []
    sizes_array, duration_array = separate_runs(
        runs_count, method, start, stop, step
        )
    for i in range(len(sizes_array[0])):
        sum = 0
        for j in range(len(sizes_array)):
            sum += sizes_array[j][i]
        average_sizes.append(sum//len(sizes_array))
    for i in range(len(duration_array[0])):
        sum = 0
        for j in range(len(duration_array)):
            sum += duration_array[j][i]
        average_duration.append(round(sum/len(duration_array), 3))
    plt.plot(
            average_sizes,
            average_duration,
            marker='x',
            linestyle='none'
            )
    plt.xlabel(f'list sizes in range {start} to {stop}')
    plt.ylabel(f'Average of {len(sizes_array)} run times with random lists')
    plt.title(f'{method}: 3-Sum Execution Time (Repeated Runs)')
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

    return m, k


def log_log_with_linear_regression(average_sizes, average_duration, method):
    log_sizes = [math.log(s) for s in average_sizes]
    log_duration = [math.log(t) for t in average_duration]
    m, k = lin_reg(log_sizes, log_duration)
    print(f"{method} - Estimated time complexity coefficient k = {k:.3f}")
    plt.scatter(log_sizes, log_duration, marker='x', label='log-log data')
    fit_vals = [m + k * x for x in log_sizes]
    pairs = [[log_sizes[i], fit_vals[i]] for i in range(len(log_sizes))]
    pairs.sort(key=lambda x: x[0])
    xs_fit = [p[0] for p in pairs]
    ys_fit = [p[1] for p in pairs]
    plt.plot(xs_fit, ys_fit, linestyle='-', label=f'Linear fit (k={k:.3f})')

    plt.xlabel('Logarithm of list sizes')
    plt.ylabel('Logarithm of time duration')
    plt.title(f'Figure 2b: Log-Log Plot with Linear Regression Fit k={k:.3f}')
    plt.show()

# Brute-Force Testing
# Test correctness brute-force
#test_correctness(3, 'brute-force')

# Experiment brute-force
#for sz in range(300, 1050, 50):
    #print(f'{sz} - {get_time_duration(sz, 'brute-force')}')

#separate_runs(3, 'brute-force', 300, 1050, 50, True)
avg_szs, avg_duration = repeated_runs(3, 'brute-force', 300, 1050, 50)
#log_log_with_linear_regression(avg_szs, avg_duration, 'Brute-Force')

# Pointers Testing
# Test correctness three pointers
#test_correctness(3, 'pointers')

# Experiment pointers
#for sz in range(5000, 29000, 1600):
    #print(f'{sz} - {get_time_duration(sz, 'pointers')}')

p_avg_szs, p_avg_duration = repeated_runs(3, 'pointers', 5000, 29000, 1600)
#log_log_with_linear_regression(p_avg_szs, p_avg_duration, 'Pointers')

# Caching Testing
# Test correctness caching
#test_correctness(3, 'caching')

# Experiment caching
#for sz in range(2500, 13750, 750):
    #print(f'{sz} - {get_time_duration(sz, 'caching')}')

c_avg_szs, c_avg_duration = repeated_runs(3, 'caching', 2500, 13750, 750)
#log_log_with_linear_regression(c_avg_szs, c_avg_duration, 'Caching')


# Brute-Force vs Pointers vs Caching
plt.plot(
    avg_szs,
    avg_duration,
    marker='+',
    linestyle='none',
    label='brute-force'
    )
plt.plot(
    p_avg_szs,
    p_avg_duration,
    marker='x',
    linestyle='none',
    label='pointers'
    )
plt.plot(
    c_avg_szs,
    c_avg_duration,
    marker='*',
    linestyle='none',
    label='caching'
    )
plt.xlabel('list sizes')
plt.ylabel('Average run times with random lists')
plt.title('Brute-Force vs Pointers vs Caching 3-Sum Average Execution Time')
plt.legend(loc='best')
plt.show()
