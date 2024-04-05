def read_file(file_path):
    with open(file_path, "r") as file:
        return set(file.readlines())


def write_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)
