import pvporcupine
import pyaudio

def detect():
    porcupine = pvporcupine.create(keywords=["jarvis"])
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = [int.from_bytes(pcm[i:i+2], 'little', signed=True)
               for i in range(0, len(pcm), 2)]

        if porcupine.process(pcm) >= 0:
            return True
