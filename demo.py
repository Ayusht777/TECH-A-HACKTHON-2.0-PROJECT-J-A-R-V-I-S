import pyttsx3
from decouple import config

#USERNAME = config('USER')
#BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
print(voices[0].id)
for i in voices:
    print(i.id)
engine.setProperty('voice', voices[1].id)
