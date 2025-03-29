import vosk
import pyaudio

# Initialize Vosk recognizer
model = vosk.Model(r"D:\Projects\App\vosk-model-small-en-in-0.4")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        print(result)