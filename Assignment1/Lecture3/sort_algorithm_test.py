import time
import matplotlib.pyplot as plt
from Util import helper
from Lecture3 import sort_algorithms as sa


def compare_algorithm(runs, start, stop, step):
    s_size, s_duration = helper.repeated_runs(
        runs,
        'selection',
        start,
        stop,
        step
        )
    b_size, b_duration = helper.repeated_runs(
        runs,
        'bubble',
        start,
        stop,
        step
        )
    i_size, i_duration = helper.repeated_runs(
        runs,
        'insertion',
        start,
        stop,
        step
        )
    plt.plot(
        s_size,
        s_duration,
        marker='+',
        linestyle='none',
        label='selection'
        )
    plt.plot(
        b_size,
        b_duration,
        marker='x',
        linestyle='none',
        label='bubble'
        )
    plt.plot(
        i_size,
        i_duration,
        marker='*',
        linestyle='none',
        label='insertion'
        )
    plt.xlabel(f'list sizes in range {start} to {stop}')
    plt.ylabel(f'Average run times of {runs} runs with random lists')
    plt.title('Running times for sorting algorithms')
    plt.legend(loc='best')
    plt.show()

    s_sizes, s_dur, sm, sk = helper.log_log_with_linear_regression(
        s_size,
        s_duration,
        'selection'
        )
    b_sizes, b_dur, bm, bk = helper.log_log_with_linear_regression(
        b_size,
        b_duration,
        'bubble'
        )
    i_sizes, i_dur, im, ik = helper.log_log_with_linear_regression(
        i_size,
        i_duration,
        'insertion'
        )

    plt.scatter(s_sizes, s_dur, marker='x', label=f'selection k={sk}')
    plt.scatter(b_sizes, b_dur, marker='*', label=f'bubble k={bk}')
    plt.scatter(i_sizes, i_dur, marker='+', label=f'insertion k={ik}')

    plt.xlabel(f'log of list sizes in range {start} to {stop}')
    plt.ylabel('Log of sorting times')
    plt.title('Log Log plots for sorting algorithms')
    plt.legend(loc='best')
    plt.show()


def merge_vs_quick(runs, start, stop, step):
    m_size, m_duration = helper.repeated_runs(
        runs,
        'merge',
        start,
        stop,
        step
        )
    q_size, q_duration = helper.repeated_runs(
        runs,
        'quick',
        start,
        stop,
        step
        )
    plt.plot(
        m_size,
        m_duration,
        marker='+',
        linestyle='none',
        label='merge'
        )
    plt.plot(
        q_size,
        q_duration,
        marker='x',
        linestyle='none',
        label='quick'
        )
    plt.xlabel(f'list sizes in range {start} to {stop}')
    plt.ylabel(f'Average run times of {runs} runs with random lists')
    plt.title('Running times for merge and quick sorting algorithms')
    plt.legend(loc='best')
    plt.show()


#compare_algorithm(3, 2000, 10000, 1000)
#merge_vs_quick(5, 10000, 30000, 1000)

# experiment improved quick sort
def test_quick_sort(array, method):
    before = time.time()
    match method:
        case 'ordinary':
            sa.quick_sort(array)
        case 'improved':
            sa.improved_quick_sort(array)
    duration = time.time() - before
    print(f'{method} quick sort time {duration}')


# Cannot test more than 1000 because of the maximum recursion depth
input1 = [x for x in range(995)]
test_quick_sort(input1, 'ordinary')
test_quick_sort(input1, 'improved')

print('')
input2 = [x for x in range(995, 0, -1)]
test_quick_sort(input2, 'ordinary')
test_quick_sort(input2, 'improved')
