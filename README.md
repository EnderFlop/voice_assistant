### PERSONAL VOICE ASSISTANT
This is a lil Alexa-type voice assistant that I set up for myself as practice with speech recognition and working with cloud APIs. Currently there is a lot of setup if you would like to use this yourself, including fixing an error in the Python speech_recognition library's source code. I'll do my best to detail everything below.
## Things you need to fix lol

 1. Create a file in the source directory name "record.txt". This will hold a record of all voice commands given.
 2. Create a [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text) API and download your credentials JSON. Put the file path to the JSON in an environment file as GOOGLE_APPLICATION_CREDENTIALS="C:\{file_path_here}"
 3. Edit line 924 of your copy of the speech_recognition library to say ["speechContexts"] rather than ["speechContext"]. Silly mistake by the devs, unsure why it hasn't been fixed.
 4. Delete/Comment out all of the environment variables you aren't using in the #INIT section of assistant.py. If you want to use them, you can simply set environment variables to what they require. For example, if you want to open browser tabs you will need to set CHROME_PATH to your computer's installation of Google Chrome, and to use the Spotify commands you will need a Spotify dev account.
 5. You should be good! Sorry things are a little shaky, I don't really know how to structure code or what to .gitignore, etc. Oh, also you can edit phrases.txt to contain phrases the Google Cloud should look for! Just make sure each specific phrase is on a newline.

Thanks for checking this out!
