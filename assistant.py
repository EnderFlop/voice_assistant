import os
from os.path import join, dirname
from dotenv import load_dotenv
import speech_recognition as sr
import time

#INIT
r = sr.Recognizer()
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
WIT_AI_KEY = os.environ.get("WIT_AI_KEY")

#LISTEN TO AUDIO
with sr.Microphone() as source:
  print("Listening...")
  audio = r.listen(source, timeout=5, phrase_time_limit=2)
  print("Done Listening.")

#AUDIO TO TEXT
try:
  command = r.recognize_wit(audio, key=WIT_AI_KEY)
except sr.UnknownValueError:
  print("Wit.ai could not understand audio")
except sr.RequestError as e:
  print("Could not request results from Wit.ai service; {0}".format(e))

#UTILITY FUNCTIONS
def kill_process(process_name):
  print(f"killing {process_name}")
  os.system(f"TASKKILL /F /IM \"{process_name}\"")

def run_process(filepath):
  print(f"running {filepath}")
  os.system(f"\"{filepath}\"")

def remove_first_word(command):
  return command.split(" ", 1)[1]

#RUN COMMAND
print("Running command: " + command)

if command.split()[0] in ("close", "kill", "end", "terminate", "destroy", "nuke", "abolish", "assimilate", "decimate", "exterminate"):
  #KILL FUNCTIONS
  command = remove_first_word(command)
  print(command)
  if command == "firefox":
    kill_process("firefox.exe")
  elif command == "league client":
    kill_process("LeagueClientUX.exe")
  elif command == "league of legends":
    kill_process("League Of Legends.exe")
  elif command == "steam":
    kill_process("Steam.exe")
  elif command == "discord":
    kill_process("Discord.exe")
  elif command == "spotify":
    kill_process("spotify.exe")

if command.split()[0] in ("run", "start", "open"):
  #RUN FUNCTIONS
  command = remove_first_word(command)
  if command == "league of legends":
    run_process(r"C:\Riot Games\League of Legends\LeagueClient.exe")

if command.split()[0] in ("restart"):
  command = remove_first_word(command)
  if command == "league of legends":
    kill_process("League Of Legends.exe")
    kill_process("LeagueClientUX.exe")
    time.sleep(10)
    run_process(r"C:\Riot Games\League of Legends\LeagueClient.exe")