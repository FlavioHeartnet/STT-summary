# core/summarizer.py
import os
import google.generativeai as genai
from .interfaces import Summarizer

class GeminiSummarizer(Summarizer):
    """Implementation of Summarizer using Google's Gemini API."""

    def __init__(self, api_key: str):
        """
        Initializes the GeminiSummarizer.

        Args:
            api_key: The API key for the Gemini API.
        
        Raises:
            ValueError: If the API key is not provided.
        """
        if not api_key:
            raise ValueError("Gemini API key is required.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        print("Gemini Summarizer initialized.")

    def summarize(self, text: str) -> str:
        """
        Summarizes the given text using the Gemini model.

        Args:
            text: The text to be summarized.

        Returns:
            The summarized text highlighting key topics.
        """
        print("Generating summary with Gemini...")
        
        prompt = (
            "You are an expert assistant specialized in summarizing content.\n"
            "Please analyze the following text and provide a concise summary that highlights the most important topics and key points.\n"
            "The output should be clear and easy to read, preferably using bullet points for distinct topics. the text must be in portuguese-Br\n\n"
            "--- TEXT TO SUMMARIZE ---\n"
            f"{text}\n"
            "--- END OF TEXT ---\n\n"
            "SUMMARY:"
        )

        try:
            response = self.model.generate_content(prompt)
            print("Summary generated successfully.")
            return response.text
        except Exception as e:
            print(f"An error occurred while calling the Gemini API: {e}")
            raise
