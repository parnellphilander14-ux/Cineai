# 🎬 CineAI — Movie Recommender + Chatbot

Final Project Coding — Streamlit + API Integration

## Features
- 🔍 Search movies by title (TMDB API)
- 🎭 Browse movies by genre & sorting
- 🎬 Movie posters, ratings, cast & details
- 🤖 AI Movie Chatbot (Google Gemini)
- 📱 Multi-page sidebar navigation

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get API Keys (both free)
- **TMDB**: https://www.themoviedb.org/settings/api
- **Gemini**: https://aistudio.google.com/apikey

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Enter API Keys in the sidebar of each page

## Project Structure
```
movie_app/
├── app.py                          ← Home page
├── requirements.txt
├── README.md
└── pages/
    ├── 1_🎬_Movie_Recommender.py   ← Search & browse movies
    ├── 2_🤖_Movie_Chatbot.py       ← Gemini AI chatbot
    └── 3_ℹ️_About.py              ← About page
```
