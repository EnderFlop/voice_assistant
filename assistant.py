import os
from os.path import join, dirname
from dotenv import load_dotenv

import speech_recognition as sr

r = sr.Recognizer()

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
WIT_AI_KEY = os.environ.get("WIT_AI_KEY")

print(WIT_AI_KEY)
with sr.Microphone() as source:
  print("Listening...")
  audio = r.listen(source)


print(audio)