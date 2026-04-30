import os

def speak(text):
    print("JARVIS:", text)
    os.system(f'espeak "{text}"')
