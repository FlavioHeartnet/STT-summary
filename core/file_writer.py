# core/file_writer.py
import os

class FileWriter:
    """A utility class for writing content to files."""

    def write(self, content: str, output_path: str) -> None:
        """
        Writes string content to a specified file path.

        Args:
            content: The string content to write.
            output_path: The destination file path.
        """
        print(f"Writing content to '{output_path}'...")
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("File written successfully.")
        except IOError as e:
            print(f"Error writing to file {output_path}: {e}")
            raise
