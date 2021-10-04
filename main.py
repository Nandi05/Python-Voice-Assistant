import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning Nandini! Hope you are doing good!")
    elif hour>12 and hour<16:
        speak("Good afternoon Nandini! Hope you are doing good!")
    elif hour>16 and hour<24:
        speak("good evening nandini. hope you are doing good!")
    speak("I am your personal assistant  Jerry. How may i help you mam?")

def takeCommand(): #takes microphone input and returns the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #seconds before which a phrase spoken by the user is considered as complete
        r.energy_threshold=200
        audio=r.listen(source)
    try:
        print("Recognizzing...")
        query=r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "none"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo #to identify the domain name of the sending hosst to smtp before issuing a mail
    server.starttls #protocol command that tells an email server that the email client wnats to turn from an insecure connectioon to a secured one
    server.login('nandiniwadhwa08@gmail.com','************') #password has to be written here
    server.sendmail('nandiniwadhwa08@gmail.com',to,content)
    server.close()

    

if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        #LOGIC FOR EXECUTING DIFFERENT TASKS

        if 'wikipedia' in query:
            speak("Searching in wikipedia...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak("according to  wikipedia")
            speak(result)
            print(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp web' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime('%H%M%S')
            speak(f'Mam, the time is{strTime}')
        elif 'open code' in query:
            codePath="C:\\Program Files (x86)\\Microsoft VS Code"
            os.startfile(codePath)
        elif 'email to nandini' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="devtuteja1008@gmail.com"
                sendEmail(to,content)
                speak("Your email has been sent to Nandini")
            except Exception as e:
                speak("Sorry dear! I am not ale to send this email to Nandini ")

