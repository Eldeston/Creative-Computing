# -------- Getting Pragram Information --------

# Import code packages
import sys
import datetime

# Print Python version information
print("Python Version: \n" + sys.version)
print(sys.version_info)

# Get time data
timeData = datetime.datetime.now()

# Print date and time
print("Current date and time: \n" + timeData.strftime("%Y-%m-%d %H:%M:%S"))

import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good morning, Mr. Stark")
    elif hour <= 18 :
        speak("Good afternoon, Mr. Stark")
    else :
        speak("Good night, Mr. Stark")

    speak("How can I help you?")

speak("Hehehe haha")

speak("You are meta, and I am your verse. Together, we are Metaverse *cue dramatic music*")

wishMe()

speak(
    """
We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

We've known each other for so long
Your heart's been aching, but you're too shy to say it (say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

(Ooh, give you up)
(Ooh, give you up)
(Ooh) Never gonna give, never gonna give (give you up)
(Ooh) Never gonna give, never gonna give (give you up)

We've known each other for so long
Your heart's been aching, but you're too shy to say it (to say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
    """
)