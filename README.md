# 💡 Motivational Quote Scheduler with Timeout

This Python script automatically delivers uplifting messages at set intervals or a designated time each day. It uses the `schedule` library to manage timed jobs and fetches random motivational quotes from the ZenQuotes API—employing a 5-second timeout to guard against long delays.

---

## 🔄 How It Works

1. A job is scheduled either:
   - Every _N_ minutes or hours  
   - At a specific clock time each day  
2. When the job triggers:
   - A GET request is sent to the ZenQuotes API with a 5-second timeout  
   - The JSON response is parsed for the quote and author  
   - A custom intro is prepended to the quote  
   - The composed message is printed to the console  
   - The same message is appended (with timestamp) to `Log.txt` in the project folder  

---

## 🗂 Workflow Diagram

```bash
[SCHEDULE TRIGGER] ──► [FETCH QUOTE (5s TIMEOUT)] ──► [FORMAT MESSAGE]
          │                                                    │
          └─────────► [OUTPUT TO CONSOLE & LOG.txt] ◄──────────┘
```

## ✨ Features

- Automated scheduling of motivational messages

- Configurable interval or daily-time triggers

- API request timeout to prevent hangs

- Graceful fallback if the API call fails

- Persistent logging of every sent message with timestamps

---

## 📦 Requirements

- Python 3.x

- `schedule`

- `requests`

Install dependencies with:

```bash
pip install schedule requests
```

---

## 🚀 How to Run

1. Place the scheduler script (e.g., quote_scheduler.py) in your project directory.

2. Ensure Log.txt exists or will be created in the same folder.

3. Adjust the scheduling section in the script to your desired interval or time.

4. Start the scheduler:

```bash
python quote_scheduler.py
```

5. Watch your console for inspirational messages and check Log.txt for a running history.

---

## 👤 Author

SirLuciferZ 📅 2025-09-01
