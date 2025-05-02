import pyttsx3
import re

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Find female voice
female_voice = None
for voice in voices:
    if "female" in voice.name.lower():
        female_voice = voice.id
        break

# Use first female voice found, or default to index 1 (typically female on most systems)
if female_voice:
    engine.setProperty('voice', female_voice)
else:
    engine.setProperty('voice', voices[1].id)

# Increase speed and volume for bold, clear voice
engine.setProperty('rate', 170)  # Increased from 150
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"🤖 AI: {text}")
    
    # Clean the text for speech - remove asterisks and other special characters
    speech_text = text
    
    # Remove asterisks, which get pronounced as "asterisk"
    speech_text = speech_text.replace('*', '')
    
    # Remove other potentially annoying special characters
    speech_text = speech_text.replace('#', '')
    speech_text = speech_text.replace('_', ' ')
    
    # Handle markdown formatting markers
    speech_text = re.sub(r'\*\*(.*?)\*\*', r'\1', speech_text)  # Bold text
    speech_text = re.sub(r'\*(.*?)\*', r'\1', speech_text)      # Italic text
    speech_text = re.sub(r'`(.*?)`', r'\1', speech_text)        # Code text
    
    # Fix spacing issues that might have been created
    speech_text = re.sub(r'\s+', ' ', speech_text).strip()
    
    engine.say(speech_text)
    engine.runAndWait()