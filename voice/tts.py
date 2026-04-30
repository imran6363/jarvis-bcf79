import os

def speak(text: str):
    print("JARVIS:", text)
    os.system(f'espeak "{text}"')
