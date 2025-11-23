import os


def count_lines(path, depth):
    if not os.path.exists(path):
        return print('Path does not exist')
    total = print_files(path, depth, 0)
    print('Total python code lines -', total)


def print_files(dir_path, depth, cur_position):
    if cur_position >= depth:
        return 0
    all = os.listdir(dir_path)
    count = 0
    for name in all:
        if not name.startswith('.'):
            full_path = os.path.join(dir_path, name)
            if os.path.isdir(full_path):
                count += print_files(full_path, depth, cur_position+1)
            else:
                if name.endswith('.py'):
                    lines = count_py_lines(full_path)
                    count += lines
                print(name,
                      ('- lines '+str(lines)) if name.endswith('.py') else '')
    return count


def count_py_lines(path):
    with open(path, 'r') as f:
        return sum(1 for line in f if line.strip())


count_lines('/Users/tharangamahavila/Documents', 4)
