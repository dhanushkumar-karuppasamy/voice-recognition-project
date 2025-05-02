# 🎙️ Jersey - Voice Recognition Assistant

**Jersey** is a smart voice assistant built using Python that listens for your voice, responds with AI, and remembers context for natural conversation. It’s lightweight, modular, and built for beginners and developers alike.

## 🚀 Features

- 🛎️ Wake word detection: Activates when you say "hello jersey" using Picovoice Porcupine.
- 🎤 Speech-to-text: Captures and converts your voice to text.
- 🤖 AI response: Uses Google Gemini 1.5 Pro for short, beginner-friendly answers.
- 🧠 Context memory: Remembers the last 2 interactions for better replies.
- 🗣️ Text-to-speech: Speaks back the AI response using `pyttsx3`.
- ⚙️ Modular structure: Code is cleanly split into files for easy expansion.

## 📁 Project Structure

voice_recognition_project/
├── main.py # Main control loop
├── ai_response.py # Handles Gemini AI with context memory
├── voice_input.py # Speech recognition
├── speak_engine.py # Text-to-speech engine
├── wake_listener.py # Wake word listener using Porcupine
├── hello-jersey.ppn # Wake word model (keep in root)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


Future Enhancements
        Add GUI (Tkinter or PyQt)
        Execute local system commands
        Improve intent classification
        Add voice feedback tones
