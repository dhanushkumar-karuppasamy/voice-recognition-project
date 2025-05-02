import subprocess
import importlib.util
import os
import speech_recognition as sr
from ai_response import get_ai_response
from speak_engine import speak
from wake_word import detect_wake_word  # Now importing the correct function

# Check if google-generativeai is installed, and install if not
if importlib.util.find_spec("google.generativeai") is None:
    print("Installing Google Generative AI package...")
    subprocess.check_call(["pip", "install", "--upgrade", "google-generativeai"])

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Context variable to store conversation history
conversation_history = []

def get_text_input():
    """Get input from keyboard"""
    text = input("💬 Text Input: ")
    return text.strip()

# Main loop
while True:
    print("🎧 Listening... (or type 't' for text input)")

    # Check for text input before starting voice recognition
    if os.name == 'nt':  # Windows
        import msvcrt
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
            if key == 't':
                text = get_text_input()
                if text.lower() in ["exit", "stop", "quit"]:
                    goodbye_message = "Goodbye chief!"
                    print(f"🤖 AI: {goodbye_message}")
                    speak(goodbye_message)
                    break
                
                response = get_ai_response(text)
                speak(response)
                continue
    
    # Voice input with wake word detection
    try:
        print("🤖 AI: Waiting for 'hello jersey'...")
        while True:
            # Wait for the wake word "hello jersey"
            detected = detect_wake_word()  # Call wake word detection
            if detected:
                print("🤖 AI: Wake word detected, ready to listen!")
                speak("How can I help you, chief?")
                break  # Break the inner loop once the wake word is detected
            
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        # Recognize the speech
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")

        if text.lower() in ["exit", "stop", "quit"]:
            goodbye_message = "Goodbye chief!"
            print(f"🤖 AI: {goodbye_message}")
            speak(goodbye_message)
            break

        response = get_ai_response(text)
        speak(response)

    except sr.WaitTimeoutError:
        continue
    except sr.UnknownValueError:
        error_message = "Sorry chief, I couldn't understand."
        print(f"🤖 AI: {error_message}")
        speak(error_message)
    except sr.RequestError as e:
        error_message = f"Could not request results; {e}"
        print(f"🤖 AI: {error_message}")
        speak(error_message)
