import os
import pytest
from package.script import process_files


@pytest.fixture
def setup_files():
    output_dir = "output"
    result_dir_path_same = os.path.join(output_dir, "same.txt")
    result_dir_path_diff = os.path.join(output_dir, "diff.txt")

    result_path_same = "same.txt"
    result_path_diff = "diff.txt"

    file1_content = "line1\nline2\nline3\n"
    file2_content = "line2\nline3\nline4\n"
    file1_path = "test_file1.txt"
    file2_path = "test_file2.txt"

    with open(file1_path, 'w') as file:
        file.write(file1_content)

    with open(file2_path, 'w') as file:
        file.write(file2_content)

    yield file1_path, file2_path

    os.remove(file1_path)
    os.remove(file2_path)
    if os.path.exists(result_path_same):
        os.remove(result_path_same)
    if os.path.exists(result_path_diff):
        os.remove(result_path_diff)
    if os.path.exists(result_dir_path_same):
        os.remove(result_dir_path_same)
    if os.path.exists(result_dir_path_diff):
        os.remove(result_dir_path_diff)
    if os.path.exists(output_dir) and not os.listdir(output_dir):
        os.rmdir(output_dir)


def test_process_files_no_output_dir(setup_files):
    file1_path, file2_path = setup_files
    process_files(file1_path, file2_path)

    assert os.path.exists('diff.txt')
    assert os.path.exists('same.txt')

    with open('diff.txt', 'r') as file:
        diff_content = file.read().splitlines()
    assert diff_content == ["line1", "line4"]

    with open('same.txt', 'r') as file:
        same_content = file.read().splitlines()
    assert same_content == ["line2", "line3"]


def test_process_files_output_dir(setup_files):
    file1_path, file2_path = setup_files
    output_dir = "output"
    process_files(file1_path, file2_path, output_dir_path=output_dir)

    assert os.path.exists(os.path.join(output_dir, 'diff.txt'))
    assert os.path.exists(os.path.join(output_dir, 'same.txt'))

    with open(os.path.join(output_dir, 'diff.txt'), 'r') as file:
        diff_content = file.read().splitlines()
    assert diff_content == ["line1", "line4"]

    with open(os.path.join(output_dir, 'same.txt'), 'r') as file:
        same_content = file.read().splitlines()
    assert same_content == ["line2", "line3"]


def test_process_files_empty_files(setup_files):
    file1_path, file2_path = setup_files
    with open(file1_path, 'w') as file:
        file.write('')
    with open(file2_path, 'w') as file:
        file.write('')

    process_files(file1_path, file2_path)

    assert os.path.exists('diff.txt')
    assert os.path.exists('same.txt')

    with open('diff.txt', 'r') as file:
        diff_content = file.read().splitlines()
    assert diff_content == []

    with open('same.txt', 'r') as file:
        same_content = file.read().splitlines()
    assert same_content == []
