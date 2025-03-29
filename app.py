import vosk
import pyaudio
import pyttsx3
import json  # Import json to parse Vosk's result

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

# Initialize Vosk recognizer
model = vosk.Model(r"D:\Projects\App\vosk-model-small-en-in-0.4")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)  # Parse the JSON result
            recognized_text = result_dict.get("text", "")  # Extract the recognized text
            if recognized_text:  # If text is recognized
                print(f"Recognized: {recognized_text}")
                engine.say(recognized_text)  # Convert text to speech
                engine.runAndWait()
except KeyboardInterrupt:
    print("Stopping...")

# Stop and close the stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Stop the text-to-speech engine
engine.stop()