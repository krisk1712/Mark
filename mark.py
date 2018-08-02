#!/Python3.6virtual/bin/activate
import wikipedia
import wolframalpha
import speech_recognition as sr
from time import ctime
import time
import datetime
import os
import timeit
import urllib.parse
import webbrowser
import pyttsx3


currentTime = datetime.datetime.now()
currentTime.hour

engine = pyttsx3.init()
voices= engine.getProperty('voices')

def speak(audioString):
    engine.setProperty('voice', voices[7].id)
    engine.say(audioString)
    engine.runAndWait()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Sir i coud not understand you, can you please repeat it sir?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("Sir? I am afraid that i am lost from the internet sir. Please forgive me")

    return data

def mak(data):
    if "hello mak" in data:
        speak("hello sir")
        speak("How can i help you sir?")
    if "how are you" in data:
        speak("I am fine")
        speak("How are you doing sir? ")

    if "what time is it" in data:
        print(ctime())
        speak(ctime())

    if "compute" in data:
        app_id = "UJ5KU9-X5HYJ6R6UW"
        client = wolframalpha.Client(app_id)
        res = client.query(data)
        answer = next(res.results).text
        print(answer)
        speak("The answer for your question is " + answer)
    if "get information on" in data:
        data = data.split(" ")
        ans = data[3]
        print(wikipedia.summary(ans))
        speak(wikipedia.summary(ans))

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("open https://www.google.nl/maps/place/" + location + "/&amp;")
    if "check my email" in data:
        speak("sir i am afraid i am updating on the protocols sir....")
    if "open application" in data:
        data = data.split(" ")
        app = data[2]
        speak("Here is the application that you wanted sir ->")
        os.system("open /Applications/" + app + ".app")
    if "search for" in data:
        speak("Searching for your query sir.")
        search_query = data
        query_encoded = urllib.parse.quote_plus(search_query)
        google_search_url = "http://www.google.com/search?q=" + format(query_encoded)
        webbrowser.open(google_search_url)
    if "say hello to" in data:
        data = data.split(" ")
        name = data[2]
        speak("Hi"+name)
        speak("how are you?")
        speak("Glad to meet you.")
    if "bye" in data:
        if currentTime.hour < 12:
            speak("Have a Pleasant day ahead sir.")
        elif 12 <= currentTime.hour < 18:
            speak("Eat well and have good afternoon sir")
        elif 18 <= currentTime.hour < 20:
            speak("have a pleasant Evening sir")
        elif 20 <= currentTime.hour < 23:
            speak("Sir dont work so hard have a good sleep sir bye")
        exit(0)
    if "sing a song" in data:
        speak("sir i am going to say you something i am not a AI i am human....")

time.sleep(1)
if currentTime.hour < 12:
    print('Good morning.')
    speak("Good Morning sir")
elif 12 <= currentTime.hour < 18:
    print('Good afternoon.')
    speak("Good Afternoon Sir")
elif 18 <= currentTime.hour < 20:
    print('Good evening.')
    speak("Good evening sir")
elif 20 <= currentTime.hour < 23:
    print("Sir i am afraid that you are working late")
    speak("Sir i am afraid that you are working late")
    speak("its Bedtime sir please go to sleep")
else:
    speak("sir its too late.")
while 1:
    data = recordAudio()
    mak(data)



