import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   
    else:
        speak("Good Evening sir")  
    print("How can I assist you today?")
    speak("How can I assist you today?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("AI : Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("AI : Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def exitAi():
    exit()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            try:
                music_dir = "C:\\Users\\HP\\Music"
                songs = os.listdir(music_dir)
                random_song = random.randint(0,len(songs))
                #print(songs)
                os.startfile(os.path.join(music_dir, songs[random_song]))
                print("Song : ",songs[random_song])
            except Exception as e:
                print("Unable to play music at the moment")
                speak("Unable to play music at the moment")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir,The time is {strTime}")

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {strDate}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            print("VS code opened")

        elif 'open pictures' in query:
            picPath = "C:\\Users\\HP\\OneDrive\\Pictures"
            os.startfile(picPath)
            print("Pictures opened")

        elif 'email to karan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mrkaran2k5@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry Sir.I am unable to send this email at this moment")
                speak("Sorry Sir.I am unable to send this email at this moment")
        elif 'close program' in query:
            print("Thanks for your time sir")
            speak("Thanks for your time sir")
            exitAi()