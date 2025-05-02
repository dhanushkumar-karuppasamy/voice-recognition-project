import pvporcupine
import sounddevice as sd
import struct
import speech_recognition as sr
from ai_response import get_ai_response
from speak_engine import speak

ACCESS_KEY = "vqiD781jfHIvlYL3tUX+Yf2mZlfUnKFu1P68d31IVOknyKx4P+3+UA=="  # Paste your key here

porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=["hey google"])
samplerate = 16000
frame_length = porcupine.frame_length

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_for_wake_word():
    print("👂 Waiting for wake word 'Hey Chief'...")
    with sd.RawInputStream(samplerate=samplerate, blocksize=frame_length, dtype='int16',
                           channels=1, callback=callback):
        sd.sleep(-1)

def callback(indata, frames, time, status):
    pcm = struct.unpack_from("h" * frame_length, indata)
    result = porcupine.process(pcm)
    if result >= 0:
        print("🎤 Wake word detected!")
        speak("Yes, chief?")
        capture_command()

def capture_command():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎧 Listening for your command...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        if text.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye chief!")
            exit()
        response = get_ai_response(text)
        speak(response)
    except:
        speak("Sorry chief, I didn't catch that.")

if __name__ == "__main__":
    speak("Hello chief! Say 'Hey Chief' to wake me up.")
    listen_for_wake_word()
