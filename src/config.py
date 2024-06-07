# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

# Print to verify (for debugging purposes only; remove in production)
print("Database URL:", DATABASE_URL)
print("API Key:", API_KEY)
