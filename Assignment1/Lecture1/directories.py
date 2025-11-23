import os


def print_files(dir_path):
    if not os.path.exists(dir_path):
        return print('Path does not exist')
    all = os.listdir(dir_path)
    for name in all:
        if not name.startswith('.'):
            full_path = os.path.join(dir_path, name)
            if os.path.isdir(full_path):
                print_files(full_path)
            else:
                print(name)


print_files('/Users/tharangamahavila/Documents')
