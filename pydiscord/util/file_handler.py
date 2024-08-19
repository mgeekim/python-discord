from pathlib import Path


class FileHandler:
    def __init__(self, filename: Path):
        self._filename = filename

    def write_text(self, text):
        with open(self._filename, 'w') as file:
            file.write(text)

    def append_text(self, text):
        with open(self._filename, 'a') as file:
            file.write(text)

    def read_text(self) -> str:
        with open(self._filename, 'r') as file:
            content = file.read()

        return content
