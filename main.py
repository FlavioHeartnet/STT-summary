# main.py
import os
import argparse
from dotenv import load_dotenv

# Import concrete implementations
from core.audio_converter import PydubAudioConverter
from core.transcriber import WhisperTranscriber
from core.summarizer import GeminiSummarizer
from core.file_writer import FileWriter
from core.pipeline import AudioProcessingPipeline

def main():
    """Main function to setup and run the application."""
    # Load environment variables from .env file
    load_dotenv()

    # --- Setup Command Line Argument Parser ---
    parser = argparse.ArgumentParser(
        description="Transcribe and summarize an audio file using Whisper and Gemini."
    )
    parser.add_argument(
        "input_file", 
        type=str, 
        help="Path to the input audio file (.wav or .mp3)."
    )
    parser.add_argument(
        "--model", 
        type=str, 
        default="base", 
        help="Whisper model to use (e.g., tiny, base, small, medium, large)."
    )
    args = parser.parse_args()

    # --- Dependency Injection and Configuration ---
    try:
        # Retrieve API key and check for its existence
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")
        
        # Instantiate the components (dependency injection)
        audio_converter = PydubAudioConverter()
        transcriber = WhisperTranscriber(model_name=args.model)
        summarizer = GeminiSummarizer(api_key=gemini_api_key)
        file_writer = FileWriter()

        # Instantiate the main pipeline with the components
        pipeline = AudioProcessingPipeline(
            audio_converter=audio_converter,
            transcriber=transcriber,
            summarizer=summarizer,
            file_writer=file_writer
        )

        # --- Run the Pipeline ---
        pipeline.run(args.input_file)

    except (ValueError, FileNotFoundError) as e:
        print(f"Configuration or file error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
