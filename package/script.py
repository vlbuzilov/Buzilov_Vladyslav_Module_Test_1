import os


def read_file(file_path):
    with open(file_path, "r") as file:
        return set(file.readlines())


def write_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)


def process_files(first_file_path, second_file_path, output_dir_path=""):
    file1 = read_file(first_file_path)
    file2 = read_file(second_file_path)

    diff_lines = file1.symmetric_difference(file2)
    same_lines = file1.intersection(file2)

    if output_dir_path:
        diff_output_path = os.path.join(output_dir_path, "diff.txt")
        same_output_path = os.path.join(output_dir_path, "same.txt")

        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)
    else:
        diff_output_path = "diff.txt"
        same_output_path = "same.txt"

    write_file(diff_output_path, sorted(diff_lines))
    write_file(same_output_path, sorted(same_lines))


if __name__ == "__main__":
    file1_path = os.path.join("files", "file1.txt")
    file2_path = os.path.join("files", "file2.txt")
    process_files(file1_path, file2_path)
