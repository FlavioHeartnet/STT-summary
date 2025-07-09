# core/transcriber.py
import whisper
from .interfaces import Transcriber

class WhisperTranscriber(Transcriber):
    """Implementation of Transcriber using OpenAI's Whisper model."""

    def __init__(self, model_name: str = "base"):
        """
        Initializes the WhisperTranscriber.

        Args:
            model_name: The name of the Whisper model to use 
                        (e.g., "tiny", "base", "small", "medium", "large").
        """
        print(f"Loading Whisper model: '{model_name}'...")
        self.model = whisper.load_model(model_name)
        print("Whisper model loaded.")

    def transcribe(self, audio_path: str) -> str:
        """
        Transcribes an audio file using the Whisper model.

        Args:
            audio_path: Path to the audio file (MP3 format recommended).

        Returns:
            The transcribed text.
        """
        print(f"Starting transcription for '{audio_path}'...")
        result = self.model.transcribe(audio_path, fp16=False)
        print("Transcription completed.")
        return result['text']
