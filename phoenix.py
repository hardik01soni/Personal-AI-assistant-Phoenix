import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')  #To take the voices sapi5(api)
voices=engine.getProperty('voices')
print(voices[1].id)   #this show the voice of ai
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")
        
    speak(" I am Phoenix, sir. How may I assist you today")

def takeCommand():
    # It takes input from microphone and show output as string 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.dynamic_energy_threshold =700
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
if __name__=="__main__":
    # speak("Phoenix is a best person")
    wishMe()
    # takeCommand()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vs code' in query:
            vscodepath= "C:\\Users\\Hardi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe"
            os.startfile(vscodepath) 
        elif 'hello phoenix' in query:
            speak("Hello Sir!")  
        # elif 'send email' in query:
        #     try:
        #         speak('What Should i say?')
        #         content = takeCommand()
        #         to = "hardiksoni606@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Hardik Sir. I am not able to send this email")
        elif 'bye phoenix' in query:
            speak('Ok Good Bye Sir, have a great day')
            exit()