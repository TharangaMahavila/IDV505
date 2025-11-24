import matplotlib.pyplot as plt
from Util import helper

# Brute-Force Testing
# Test correctness brute-force
helper.test_correctness(3, 'brute-force')

# Experiment brute-force
for sz in range(300, 1050, 50):
    print(f'{sz} - {helper.get_time_duration(sz, 'brute-force')}')

helper.separate_runs(3, 'brute-force', 300, 1050, 50, True)
avg_szs, avg_duration = helper.repeated_runs(
    3,
    'brute-force',
    300,
    1050,
    50,
    True
    )
helper.log_log_with_linear_regression(
    avg_szs,
    avg_duration,
    'Brute-Force',
    True
    )

# Pointers Testing
# Test correctness three pointers
helper.test_correctness(3, 'pointers')

# Experiment pointers
for sz in range(5000, 29000, 1600):
    print(f'{sz} - {helper.get_time_duration(sz, 'pointers')}')

helper.separate_runs(3, 'pointers', 5000, 29000, 1600, True)
p_avg_szs, p_avg_duration = helper.repeated_runs(
    3,
    'pointers',
    5000,
    29000,
    1600,
    True
    )
helper.log_log_with_linear_regression(
    p_avg_szs,
    p_avg_duration,
    'Pointers',
    True
    )

# Caching Testing
# Test correctness caching
helper.test_correctness(3, 'caching')

# Experiment caching
for sz in range(2500, 13750, 750):
    print(f'{sz} - {helper.get_time_duration(sz, 'caching')}')

helper.separate_runs(3, 'caching', 2500, 13750, 750, True)
c_avg_szs, c_avg_duration = helper.repeated_runs(
    3,
    'caching',
    2500,
    13750,
    750,
    True
    )
helper.log_log_with_linear_regression(
    c_avg_szs,
    c_avg_duration,
    'Caching',
    True
    )


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
