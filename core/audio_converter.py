# core/audio_converter.py
import os
from pydub import AudioSegment
from .interfaces import AudioConverter

class PydubAudioConverter(AudioConverter):
    """Implementation of AudioConverter using the pydub library."""

    def convert(self, input_path: str, output_format: str = "mp3") -> str:
        """
        Converts a WAV audio file to MP3 format.

        Args:
            input_path: The path to the input WAV file.
            output_format: The target audio format (e.g., 'mp3').

        Returns:
            The path to the converted MP3 file.
            
        Raises:
            FileNotFoundError: If the input file does not exist.
            Exception: For pydub related errors.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found at: {input_path}")

        try:
            audio = AudioSegment.from_wav(input_path)
            
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}.{output_format}"
            
            print(f"Converting '{input_path}' to '{output_path}'...")
            audio.export(output_path, format=output_format)
            print("Conversion successful.")
            
            return output_path
        except Exception as e:
            print(f"Error during audio conversion: {e}")
            print("Please ensure FFmpeg is installed and accessible in your system's PATH.")
            raise
