# core/interfaces.py
from abc import ABC, abstractmethod

class AudioConverter(ABC):
    """Interface for audio conversion services."""
    @abstractmethod
    def convert(self, input_path: str, output_format: str) -> str:
        """Converts an audio file to a specified format."""
        pass

class Transcriber(ABC):
    """Interface for transcription services."""
    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        """Transcribes an audio file to text."""
        pass

class Summarizer(ABC):
    """Interface for text summarization services."""
    @abstractmethod
    def summarize(self, text: str) -> str:
        """Summarizes a given text."""
        pass
