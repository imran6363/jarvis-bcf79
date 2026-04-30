import vosk
import json
import sounddevice as sd

model = vosk.Model("model-bn")

def listen():
    rec = vosk.KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1):
        data = sd.rec(8000, samplerate=16000, channels=1)
        sd.wait()

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result.get("text", "")
