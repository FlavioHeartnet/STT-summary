# core/pipeline.py
import os
from .interfaces import AudioConverter, Transcriber, Summarizer
from .file_writer import FileWriter

class AudioProcessingPipeline:
    """Orchestrates the audio processing workflow."""

    def __init__(
        self,
        audio_converter: AudioConverter,
        transcriber: Transcriber,
        summarizer: Summarizer,
        file_writer: FileWriter
    ):
        """
        Initializes the pipeline with required service components.
        
        Args:
            audio_converter: An object that implements the AudioConverter interface.
            transcriber: An object that implements the Transcriber interface.
            summarizer: An object that implements the Summarizer interface.
            file_writer: An object for writing files.
        """
        self.audio_converter = audio_converter
        self.transcriber = transcriber
        self.summarizer = summarizer
        self.file_writer = file_writer

    def run(self, input_audio_path: str):
        """
        Executes the full audio processing pipeline.

        Args:
            input_audio_path: The path to the input audio file.
        """
        print(f"--- Starting Audio Processing Pipeline for: {input_audio_path} ---")
        try:
            # Step 0: Validate input and get file extension
            if not os.path.exists(input_audio_path):
                raise FileNotFoundError(f"The input file was not found: {input_audio_path}")

            file_ext = os.path.splitext(input_audio_path)[1].lower()
            
            # Requirement 1: Convert WAV to MP3 if necessary
            # Note: Whisper can handle WAV, but this fulfills the requirement.
            # We treat the user's '.waptt' as a typo for '.wav'.
            audio_to_transcribe = input_audio_path
            if file_ext == '.wav' or file_ext == '.opus':
                audio_to_transcribe = self.audio_converter.convert(input_audio_path, 'mp3')
            elif file_ext != '.mp3':
                raise ValueError(f"Unsupported audio format: '{file_ext}'. Only .wav and .mp3 are accepted.")

            # Step 1: Transcribe audio to text
            transcribed_text = self.transcriber.transcribe(audio_to_transcribe)

            # Step 2: Save the full transcription
            base_output_path = os.path.splitext(input_audio_path)[0]
            transcription_path = f"{base_output_path}_transcription.txt"
            self.file_writer.write(transcribed_text, transcription_path)

            # Step 3: Summarize the text
            summary_text = self.summarizer.summarize(transcribed_text)

            # Step 4: Save the summary
            summary_path = f"{base_output_path}_summary.txt"
            self.file_writer.write(summary_text, summary_path)

            print("\n--- Pipeline finished successfully! ---")
            print(f"Full transcription saved to: {transcription_path}")
            print(f"Summary saved to: {summary_path}")

        except Exception as e:
            print(f"\n--- Pipeline failed: {e} ---")
