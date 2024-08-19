from pathlib import Path
from unittest.mock import mock_open

import pytest

from pydiscord.util.file_handler import FileHandler


@pytest.fixture
def patch_open(mocker, request):
    if hasattr(request, "param") and isinstance(request.param, str):
        mock = mock_open(read_data=request.param)
    else:
        mock = mock_open()
    mocker.patch("builtins.open", mock)

    return mock


def test_write_text(patch_open):
    test_text: str = "Hello, world!"
    path: Path = Path("test.txt")

    handler = FileHandler(path)
    handler.write_text(test_text)

    patch_open.assert_called_once_with(path, 'w')
    patch_open().write.assert_called_once_with(test_text)


def test_append_text(patch_open):
    test_text: str = "Hello, world!"
    path: Path = Path("test.txt")

    handler = FileHandler(path)
    handler.append_text(test_text)

    patch_open.assert_called_once_with(path, 'a')
    patch_open().write.assert_called_once_with(test_text)


@pytest.mark.parametrize('patch_open', ["Hello, world!"], indirect=True)
def test_read_text(patch_open):
    test_text: str = "Hello, world!"
    path: Path = Path("test.txt")

    handler = FileHandler(path)
    result = handler.read_text()

    patch_open.assert_called_once_with(path, 'r')
    assert result == test_text
