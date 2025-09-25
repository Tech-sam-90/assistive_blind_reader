import pvporcupine
import pyaudio
import struct
import os
import requests
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from array import array

# Path to the custom wake word file
custom_wake_word_path = r"C:\Users\hp\Desktop\Wakeword\echo.ppn"

# Initialize Porcupine with the custom wake word
porcupine = None
try:
    porcupine = pvporcupine.create(
        keyword_paths=[custom_wake_word_path],
        access_key="Hk/Ev7RvIk7JtQEJmQwJCpQkFMzJ4Kl/dK5KLDtdTQJ4LUNZKzP7pg=="
    )
except Exception as e:
    print(f"Failed to initialize Porcupine: {e}")
    exit(1)

# Audio stream setup
pa = pyaudio.PyAudio()

audio_stream = None
try:
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
except Exception as e:
    print(f"Failed to open audio stream: {e}")
    if porcupine is not None:
        porcupine.delete()
    exit(1)

print("Listening for custom wake word...")

try:
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        # Check if wake word is detected
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Custom wake word detected!")
            mp3_fp = BytesIO()
            tts = gTTS("Welcome, please select your language preference, I can only offer English, French or Spanish", lang='en', tld='com.ng')
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            audio = AudioSegment.from_file(mp3_fp, format='mp3')
            play(audio)
            break

except KeyboardInterrupt:
    print("Stopping...")

finally:
    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()

    if porcupine is not None:
        porcupine.delete()
