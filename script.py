def read_file(file_path):
    with open(file_path, "r") as file:
        return set(file.readlines())


def write_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


def process_files(first_file_path, second_file_path):
    file1 = read_file(first_file_path)
    file2 = read_file(second_file_path)

    diff_lines = file1.symmetric_difference(file2)
    same_lines = file1.intersection(file2)

    write_file('diff.txt', sorted(diff_lines))
    write_file('same.txt', sorted(same_lines))

