# 🧠 MindMate — AI Mental Health Companion

> A comprehensive mental wellness application built with Python & Streamlit, powered by Groq AI.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io)
[![Groq AI](https://img.shields.io/badge/Groq-AI%20Powered-green)](https://groq.com)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Running Locally](#running-locally)
8. [Demo Credentials](#demo-credentials)
9. [Deployment — Streamlit Cloud](#deployment--streamlit-cloud)
10. [Deployment — Render](#deployment--render)
11. [Troubleshooting](#troubleshooting)
12. [Tech Stack](#tech-stack)

---

## Overview

MindMate is an AI-powered mental wellness companion that helps users track their mood, journal their thoughts, meditate, manage sleep, and connect with professional therapists — all in one place.

---

## Features

| Page | Status | Description |
|---|---|---|
| 🏠 Home Dashboard | ✅ Live | Mood charts, wellness insights, daily prompt |
| 📔 Journal | ✅ Live | Write & analyze journal entries with AI sentiment |
| 😊 Mood Tracker | ✅ Live | Log daily moods with notes |
| 🧘 Meditation Tracker | ✅ Live | Log & track meditation sessions |
| 😴 Sleep Tracker | ✅ Live | Log sleep quality and duration |
| 🎯 Wellness Goals | ✅ Live | Set and track personal goals |
| 🤖 AI Chatbot | ✅ Live | Chat with Groq-powered mental health AI |
| 📊 Analytics | ✅ Live | Charts & insights from all your data |
| 📈 Wellness Dashboard | ✅ Live | Consolidated wellness overview |
| ⏱️ Productivity Timer | ✅ Live | Pomodoro-style focus timer |
| 🌬️ Breathing Exercises | ✅ Live | Guided breathing exercise animations |
| 🧑‍⚕️ Find Therapist | ✅ Live | Browse & request professional therapists |
| 🎨 Personalization | ✅ Live | Profile + therapist matching |
| 🌟 Community | 🔜 Coming Soon | Community support space |
| 🛡️ Personality RPG | 🔜 Coming Soon | Gamified self-discovery |

---

## Project Structure

```
mindmate/
├── main.py                   # App entry point, navigation, routing
├── config.py                 # API keys, database path config
├── data/
│   └── mindmate.db           # SQLite database (auto-created on first run)
├── pages/
│   ├── home.py               # Home dashboard
│   ├── journal.py            # Journal page
│   ├── mood_tracker.py       # Mood tracking
│   ├── meditation_tracker.py # Meditation logging
│   ├── sleep_tracker.py      # Sleep logging
│   ├── goals.py              # Wellness goals
│   ├── chatbot.py            # AI chatbot (Groq powered)
│   ├── analytics.py          # Data analytics & charts
│   ├── wellness_dashboard.py # Combined wellness view
│   ├── productivity_timer.py # Pomodoro timer
│   ├── breathing_exercises.py# Breathing exercises
│   ├── professional_help.py  # Find therapist
│   ├── personalization.py    # User profile & therapist matching
│   ├── community.py          # Coming soon
│   └── personality_rpg.py    # Coming soon
└── utils/
    ├── database.py           # SQLite database connection & schema
    ├── auth.py               # Login, signup, user authentication
    ├── animations.py         # Lottie animation helpers
    ├── mood_analysis.py      # Sentiment analysis & mood trends
    ├── stats_manager.py      # Stats caching & retrieval
    ├── visualization.py      # Plotly charts & graphs
    └── db.py                 # MongoDB stub (mocked — app uses SQLite)
```

---

## Prerequisites

Before setting up, make sure you have the following installed:

### 1. Python 3.10 or higher

Check your version:
```bash
python3 --version
```

Install Python from [python.org](https://python.org/downloads) if needed.

### 2. pip (Python package manager)

Check if pip is installed:
```bash
pip3 --version
```

Upgrade pip if it's out of date:
```bash
pip3 install --upgrade pip
```

### 3. Git

```bash
git --version
```

Install from [git-scm.com](https://git-scm.com) if not installed.

---

## Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/Amaan112005/mindmate.git
cd mindmate
```

### Step 2 — (Recommended) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

### Step 3 — Install all dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | >=1.28.0 | Web app framework |
| `python-dotenv` | >=1.0.0 | Load secrets from `.env` file |
| `pandas` | >=2.0.0 | Data manipulation & analysis |
| `numpy` | >=1.24.0 | Numerical operations |
| `plotly` | >=5.0.0 | Interactive charts |
| `pymongo` | >=4.0.0 | MongoDB (mocked, kept for compatibility) |
| `textblob` | >=0.17.1 | Sentiment analysis on journal text |
| `streamlit-lottie` | >=0.0.3 | Lottie animations in Streamlit |
| `altair` | >=4.2.0 | Declarative charting |
| `seaborn` | >=0.12.2 | Statistical visualization |
| `matplotlib` | >=3.7.0 | Plotting library |
| `groq` | >=0.1.0 | Groq AI API client |
| `pysqlite3-binary` | >=0.5.2 | SQLite fallback for cloud environments |

### Step 4 — Download TextBlob language data

TextBlob requires extra data for sentiment analysis:

```bash
python3 -m textblob.download_corpora
```

---

## Configuration

### Step 1 — Create a `.env` file

In the root of the project, create a file named `.env`:

```bash
touch .env
```

Add the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 2 — Get a Groq API Key (Free)

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to **API Keys** → **Create new key**
4. Copy the key and paste it into your `.env` file

> ⚠️ **Never commit your `.env` file to GitHub.** It's already in `.gitignore` to protect you.

---

## Running Locally

### Start the app

```bash
cd mindmate          # Navigate to repo root (not the mindmate/ subfolder)
python3 -m streamlit run mindmate/main.py
```

The app opens automatically in your browser at:
- **Local:** http://localhost:8501
- **Network:** http://[your-local-ip]:8501

### Stop the app

Press `Ctrl + C` in the terminal.

### Restart the app (after code changes)

```bash
python3 -m streamlit run mindmate/main.py
```

> Streamlit auto-reloads on most file changes. For deep changes (like modifying imports), stop and restart manually.

---

## Demo Credentials

A demo user is automatically created on first launch:

| Field | Value |
|---|---|
| Username | `amaan` |
| Password | `amaan` |

You can also create your own account using the **Sign Up** tab on the login screen.

---

## Deployment — Streamlit Cloud

**Best option** — Free, built specifically for Streamlit apps, SQLite works out of the box.

### Steps:

1. Push your code to GitHub (already done if cloned from the repo)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click **New app**
5. Fill in:
   - **Repository:** `Amaan112005/mindmate`
   - **Branch:** `main`
   - **Main file path:** `mindmate/main.py`
6. Click **Advanced settings**:
   - **Python version:** `3.10`
   - **Secrets** (TOML format):
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```
7. Click **Deploy!**

---

## Deployment — Render

### Steps:

1. Go to [render.com](https://render.com) and sign in with GitHub
2. Click **New +** → **Blueprint**
3. Connect your `mindmate` repository
4. Render auto-detects `render.yaml`
5. In the Environment Variables section, add:
   - **Key:** `GROQ_API_KEY`
   - **Value:** your Groq API key
6. Click **Apply**

> ⚠️ Render uses Docker for this app (configured in `render.yaml` and `Dockerfile`). First build takes ~5 minutes.

---

## Troubleshooting

### `File does not exist: mindmate/main.py`

You're running the command from the wrong directory. Make sure you `cd` into the repo root first:

```bash
cd /path/to/mindmate
python3 -m streamlit run mindmate/main.py
```

### `ModuleNotFoundError: No module named 'streamlit'`

Dependencies aren't installed. Run:

```bash
pip install -r requirements.txt
```

### `Error loading dashboard` or chart errors

The database might have out-of-range mood scores. Run this one-time fix:

```bash
python3 -c "
import sys; sys.path.insert(0, '.')
from mindmate.utils.database import get_db_connection, init_db
init_db()
with get_db_connection() as conn:
    cur = conn.cursor()
    cur.execute('UPDATE journal_entries SET mood_score = (mood_score / 5.0) - 1 WHERE mood_score > 1')
    conn.commit()
    print('Fixed', cur.rowcount, 'rows')
"
```

### `sqlite3.OperationalError` on cloud

The `data/` directory doesn't exist. The fix is already in the code (`mkdir(parents=True, exist_ok=True)` in `auth.py`). Just redeploy.

### Groq API errors

- Check your API key in `.env` is correct
- Check the model at `mindmate/pages/chatbot.py` — must be `llama-3.1-8b-instant` (not the old decommissioned models)

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10** | Core language |
| **Streamlit** | Web app framework (frontend + backend) |
| **SQLite** | Local database (auto-created, no setup needed) |
| **Groq AI** | AI chatbot backend (`llama-3.1-8b-instant` model) |
| **Plotly** | Interactive charts |
| **TextBlob** | Mood/sentiment analysis on journal text |
| **Lottie** | Animations |
| **python-dotenv** | Secure API key management |

---

## License

This project is for educational and portfolio purposes.

---

*Built with ❤️ by Amaan*
