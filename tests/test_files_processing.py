import os
import pytest
from script import read_file, write_file, process_files


@pytest.fixture
def setup_files(request):
    file1_path = "test_file1.txt"
    file2_path = "test_file2.txt"

    with open(file1_path, 'w') as file:
        file.write(request.param[0])

    with open(file2_path, 'w') as file:
        file.write(request.param[1])

    yield file1_path, file2_path

    os.remove(file1_path)
    os.remove(file2_path)

