from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

# Correctly retrieve the Serper API key
serper_api_key = os.getenv("SERPER_API_KEY")

# Check if API key is available, otherwise show a warning instead of stopping the app
if not serper_api_key:
    print("⚠️ Warning: SERPER_API_KEY is not set! Ensure it's in your .env file.")
    tool = None  # Prevent errors if API key is missing
else:
    os.environ["SERPER_API_KEY"] = serper_api_key
    tool = SerperDevTool()

