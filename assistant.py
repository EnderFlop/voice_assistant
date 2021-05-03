import os
from os.path import join, dirname
from dotenv import load_dotenv
import speech_recognition as sr
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import json

#INIT
r = sr.Recognizer()
r.energy_threshold = 300
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
#WIT_AI_KEY = os.environ.get("WIT_AI_KEY")
SPOTIPY_CLIENT_ID=os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET=os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI=os.environ.get("SPOTIPY_REDIRECT_URI")
CHROME_PATH=os.environ.get("CHROME_PATH")
#IBM_USERNAME=os.environ.get("IBM_USERNAME")
#IBM_API_KEY=os.environ.get("IBM_API_KEY")
#IBM_URL=os.environ.get("IBM_URL")
GOOGLE_APPLICATION_CREDENTIALS=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private user-library-modify'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
preferred_phrases = open("phrases.txt", "r").read().splitlines()

#LISTEN TO AUDIO
with sr.Microphone() as source:
  print("Listening...")
  audio = r.listen(source, timeout=5, phrase_time_limit=4)
  print("Done Listening.")

#AUDIO TO TEXT
try:
  #command = r.recognize_wit(audio, key=WIT_AI_KEY)
  #command = r.recognize_ibm(audio, username="apikey", password=IBM_API_KEY).lower()
  command = r.recognize_google_cloud(audio, preferred_phrases=preferred_phrases).lower()
except sr.UnknownValueError:
  print("STT could not understand audio")
except sr.RequestError as e:
  print("Could not request results from STT service; {0}".format(e))

#Recorder function
with open("record.txt", "r+") as command_record:
  record = command_record.read()
  record += f"\n{command}"
  command_record.write(record) #CHANGE SO IT DOESNT ERASE< IT ADDS

#UTILITY FUNCTIONS
def kill_process(process_name):
  print(f"killing {process_name}")
  os.system(f"TASKKILL /F /IM \"{process_name}\"")

def run_process(filepath):
  print(f"running {filepath}")
  os.system(f"\"{filepath}\"")

def remove_first_word(command):
  return command.split(" ", 1)[1]

def open_tab(url):
  print(f"opening {url}")
  webbrowser.get(f"\"{CHROME_PATH}\" %s").open(f"https://www.{url}")

def get_first_word(string):
  return string.split()[0]

#RUN COMMAND
print("Running command: " + command)
command = command.strip() #google puts a space at the end for some reason!
first_word = get_first_word(command)

if first_word in ("close", "kill", "end", "terminate", "destroy", "nuke", "abolish", "assimilate", "decimate", "exterminate"):
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

elif first_word in ("run", "start", "open"):
  #RUN FUNCTIONS
  command = remove_first_word(command)
  if command == "league of legends":
    run_process(r"C:\Riot Games\League of Legends\LeagueClient.exe")

  #WEBBROWSER FUNCTIONS (url = everything after 'www.' in a url)
  elif command == "youtube":
    open_tab("youtube.com")
  elif command == "notepad":
    open_tab("rapidtables.com/tools/notepad.html")
  elif command == "chess":
    open_tab("chess.com/play/online")

  elif get_first_word(command) == "reddit":
    if command == "reddit":
      open_tab("reddit.com")
    else:
      command = remove_first_word(command) #remove reddit
      command = command.replace(" ", "") #reddit doesnt use spaces in subreddit names
      open_tab(f"reddit.com/r/{command}")

  elif get_first_word(command) in ("runes", "statistics", "build"): #STT really hates 'op.gg' :(
    champion = remove_first_word(command)
    open_tab(f"op.gg/champion/{champion}")
  


elif first_word in ("restart"):
  command = remove_first_word(command)
  if command == "league of legends":
    kill_process("League Of Legends.exe")
    kill_process("LeagueClientUX.exe")
    time.sleep(10)
    run_process(r"C:\Riot Games\League of Legends\LeagueClient.exe")

elif first_word in ("spotify", "music"):
  #SPOTIFY FUNCTIONS
  command = remove_first_word(command)
  if command == "pause":
    sp.pause_playback()
  elif command in ("unpause", "resume", "start"):
    sp.start_playback()
  elif command == "previous":
    sp.previous_track()
  elif command == "like":
    sp.current_user_saved_tracks_add(tracks=[sp.current_playback()["item"]["uri"]])

elif first_word in ("google", "search"):
  command = remove_first_word(command)
  open_tab(f"google.com/search?q={command}")

else:
  #COMMAND NOT FOUND
  print("Command not found... Exiting in 5")
  time.sleep(5)

#TODO
# Add opening specific webpages
# Searching Youtube for video
# More complex stuff, maybe opening steam games? formatting applications on windows?