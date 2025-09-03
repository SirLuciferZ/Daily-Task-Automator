"""
Motivational Quote Scheduler with Timeout

This script schedules and sends motivational messages
at regular intervals or at a specific time each day.

It uses the `schedule` library to manage timed execution
and fetches random motivational quotes from the
ZenQuotes API with a request timeout to prevent long delays.

When triggered:
    - Retrieves a random motivational quote from the ZenQuotes API (with a 5-second timeout).
    - Formats the quote with its author and a custom motivational intro.
    - Prints the message to the console.
    - Appends the message to a `Log.txt` file in the project directory for record-keeping.

Features:
    - Automated scheduling of motivational messages.
    - API request timeout to avoid hanging if the API is slow or unreachable.
    - Graceful error handling with a fallback message if the API request fails.
    - Persistent logging of all sent messages with timestamps.

Requirements:
    - Python 3.x
    - schedule (install via `pip install schedule`)
    - requests (install via `pip install requests`)

Author: SirLuciferZ
Date: 2025/09/01
"""

import time
from datetime import datetime
import os
from pathlib import Path
import schedule
import requests

# Change the working directory to the project folder
# This ensures that any files created (like Log.txt) are stored here.
# Set working directory to script location
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

# API endpoint for fetching a random motivational quote
QUOTE_API_URL = "https://zenquotes.io/api/random"


def get_quote():
    """
    Fetch a random motivational quote from the ZenQuotes API.

    Returns:
        str: A formatted string containing the quote and its author.

    Process:
        - Sends a GET request to the ZenQuotes API.
        - Parses the JSON response to extract the quote text and author.
        - Formats the output as:
            "Quote text
            <Author>"
    """

    try:
        response = requests.get(QUOTE_API_URL, timeout=5)
        response.raise_for_status()
        json_data = response.json()
        quote = json_data[0].get("q", "Keep going, no matter what.")
        author = json_data[0].get("a", "Unknown")
        return f"{quote}\n<{author}>"
    except requests.exceptions.RequestException as e:
        return f"Stay strong and keep moving forward.\n<Unknown> (Error: {e})"


def send_message():
    """
    Generate and log a daily motivational message.

    Process:
        - Gets the current date and time.
        - Creates a motivational message with a static intro and a random quote.
        - Prints the message to the console.
        - Appends the message to 'Log.txt' for record-keeping.
    """
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Stay focused, Lucifer — greatness is built daily!\n\n{get_quote()}"
    print(f"\n[{date_now}] \n{message}\n")
    with open("Log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{date_now}] \n{message}\n")


# Schedule the send_massage function to run daily at midnight
# Example alternative for testing:
schedule.every(5).seconds.do(send_message)

# schedule.every().day.at("00:00").do(send_message)

# Keep the script running indefinitely to check and execute scheduled tasks
while True:
    # Main loop:
    # - Runs any pending scheduled jobs.
    # - Waits for 1 second before checking again.
    schedule.run_pending()
    time.sleep(1)


# import time
# from datetime import datetime
# import schedule
# import os
# import requests
# from pathlib import Path

# # Set working directory to script location
# BASE_DIR = Path(__file__).resolve().parent
# os.chdir(BASE_DIR)

# # API endpoint for fetching a random motivational quote
# QUOTE_API_URL = "https://zenquotes.io/api/random"

# def get_quote():
#     """
#     Fetch a random motivational quote from the ZenQuotes API.
#     Returns:
#         str: A formatted string containing the quote and its author.
#     """
#     try:
#         response = requests.get(QUOTE_API_URL, timeout=5)
#         response.raise_for_status()
#         json_data = response.json()
#         quote = json_data[0].get("q", "Keep going, no matter what.")
#         author = json_data[0].get("a", "Unknown")
#         return f"{quote}\n<{author}>"
#     except Exception as e:
#         return f"Stay strong and keep moving forward.\n<Unknown> (Error: {e})"

# def send_message():
#     """
#     Generate and log a daily motivational message.
#     """
#     date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     message = f"Stay focused, Lucifer — greatness is built daily!\n\n{get_quote()}"
#     print(f"\n[{date_now}] \n{message}\n")
#     with open("Log.txt", "a", encoding="utf-8") as f:
#         f.write(f"\n[{date_now}] \n{message}\n")

# def main():
#     # Schedule the send_message function to run daily at midnight
#     schedule.every().day.at("00:00").do(send_message)
#     # For testing: schedule.every(5).seconds.do(send_message)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     main()
