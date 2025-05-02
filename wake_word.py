import pvporcupine
import pyaudio
import struct
import os

ACCESS_KEY = "vqiD781jfHIvlYL3tUX+Yf2mZlfUnKFu1P68d31IVOknyKx4P+3+UA=="

def detect_wake_word():
    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(
            access_key=ACCESS_KEY,
            keyword_paths=["hello-jersey_en_windows_v3_0_0.ppn"],  # Make sure the model file is in the same folder
            sensitivities=[0.6]
        )

        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("🕵️ Listening for wake word: 'hello jersey'...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)
            if result >= 0:
                print("🎙️ Wake word detected: Hello Jersey!")
                return True  # Wake word detected, return True

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if pa:
            pa.terminate()
    
    return False  # Return False if wake word was not detected
