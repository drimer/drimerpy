import logging
import os
import uuid

import pytest

from drimerpy.debugging import enable_logging_to_file, disable_logging_to_file


@pytest.fixture
def temp_file_content():
    return 'Existing line'


@pytest.fixture
def temp_file_path(request, temp_file_content):
    path = '/tmp/{}'.format(uuid.uuid4())

    with open(path, 'w') as f:
        f.write(temp_file_content)

    def finaliser():
        os.remove(path)

    request.addfinalizer(finaliser)

    return path


@pytest.fixture
def nonexistent_filepath():
    while True:
        path = '/tmp/{}'.format(uuid.uuid4())
        if not os.path.exists(path):
            return path


def test_enable_logging_to_non_existing_file():
    first_line = 'One apple'
    second_line = 'Two bananas'
    filepath = '/tmp/{}'.format(uuid.uuid4())

    logger = logging.getLogger('non_existing_file')
    logger.warning(first_line)

    enable_logging_to_file(filepath)

    logger.warning(second_line)

    with open(filepath, 'r') as f:
        content = ''.join(f.readlines())

    assert second_line in content


def test_enable_logging_to_existing_file(temp_file_path, temp_file_content):
    first_line = 'One apple'
    second_line = 'Two bananas'

    logger = logging.getLogger('existing_file')
    logger.warning(first_line)

    enable_logging_to_file(temp_file_path)

    logger.warning(second_line)

    with open(temp_file_path, 'r') as f:
        content = ''.join(f.readlines())

    assert temp_file_content in content
    assert second_line in content


def test_disable_logging_to_file(nonexistent_filepath):
    enable_logging_to_file(nonexistent_filepath)

    logged_line = 'Green banana'
    logger = logging.getLogger('disable_lodding')
    logger.warning(logged_line)

    disable_logging_to_file(nonexistent_filepath)

    not_logged_line = 'Orange apple'
    logger.warning(logged_line)

    with open(nonexistent_filepath, 'r') as f:
        content = ''.join(f.readlines())

    assert logged_line in content
    assert not_logged_line not in content
