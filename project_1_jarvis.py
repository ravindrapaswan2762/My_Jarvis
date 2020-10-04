### pip install pipwin ####
### pipwin install pyaudio ####
import pyttsx3 # pip install pyttsx3=2.7 or pyttsx3
import datetime # inbuilt module
import speech_recognition as sr  # pip install apeechRecognition
import wikipedia  # pip install wikipedia
import webbrowser # inbuilt module
import os # inbuilt module
import smtplib # inbuilt module
import random  # inbuilt module
import getpass # inbuilt module

import datefinder
import winsound





# for taking a voice like david or zara...
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

# for speak of taken voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good mornning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evenning!")
    speak("HI sir, this is jaarvis. please tell me how may i help you!")

 # it takes microphone input from the user and returns string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        #speak(query)
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mk5643931@gmail.com', 'password here')
    server.sendmail('mk5643931@gmail.com', to, content)
    server.close()

def setAlarm(text):
    date_Time = datefinder.find_dates(text)
    for match in date_Time:
        print(match)
    stringA = str(match)
    timeA = stringA[11:]
    print(timeA)
    hourA = timeA[:-6]
    print(hourA)
    minuteA = timeA[3:-3]
    print(minuteA)
    minuteA = int(minuteA)

    while True:
        if hourA == datetime.datetime.now().hour:
            if minuteA == datetime.datetime.now().minute:
                print("alarm is running...")
                winsound.playsound('D:\\VEDEOS\\Playlists\\Famous-Flute-Ringtone-2020', winsound.SND_LOOP)
            elif minuteA>datetime.datetime.now().minute:
                break







if __name__ == '__main__':
    setAlarm("set alarm at 16:57 pm ")
    wishme()

    while True:

        query = takecommand().lower()

        # logic for executing task bassed on queris
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            speak("Opening chrome")
            webbrowser.open("chrome.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\VEDEOS'
            songs = os.listdir(music_dir)
            n = len(songs)
            index = random.randint(1, n)
            # print(songs)
            speak("Opening music")

            # songs = random.randint[0,len(songs)]
            os.startfile(os.path.join(music_dir, songs[index]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"SIR, The time is {strTime}")

        elif 'open sublime text' in query:
            path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            speak("Opening sublime text")
            os.startfile(path)

        elif 'open VLC Player' in query:
            path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            speak("Opening v l c player")
            os.startfile(path)

        elif 'email to ravindra' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "paswanravindra209@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry my friend ravindra. i am not able to send this Email !")

        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open('facebook.com')

        elif 'according to google' in query:
            speak("Opening google")
            query = query.replace('according to google', "")
            webbrowser.open('https://google.com/#q=' + query, new=2)

        elif 'your name' in query or 'about you' in query or 'your detail' in query:
            query = takecommand().lower()
            print(query)
            speak("hi, i am, jaarvis, as a, computer based program ")

        elif 'any girlfriend' in query or 'your girlfriend' in query or 'girlfriend' in query:
            query = takecommand().lower()
            print(query)
            speak("Not now, but, i am still trying, on alexa, her voices are, so sweet")

        elif 'can i' in query:
            query = takecommand().lower()
            print(query)
            speak("Why, Not ! ")

        elif 'hello' in query or 'hi' in query or 'hello jaarvis' in query or 'hi jaarvis' in query:
            query = takecommand().lower()
            print(query)
            speak("HELLO, ravindra sir,! how may i help you ! ")

        elif 'your date of birth' in query or 'DOB' in query:
            query = takecommand().lower()
            print(query)
            speak("My activation date is, my date of birth, and i  activated on, 12 september, 2020")

        elif 'who invented you' in query or 'who created you' in query:
            query = takecommand().lower()
            print(query)
            speak("I am invented by, SIR Ravindra, paaswaan, and, now we are, a best friend")

        """elif 'set alarm' in query or 'set the alarm' in query:
            query = takecommand().lower()

            speak("What hour, do you, want set ")
            #alarm_hour = int(input("What hour, do you, want, set alarm "))
            takecommand()


            speak("What minute, do you, want set ")
            #alarm_minute = int(input("What minute, do you, want, set alarm "))
            takecommand()


            speak("am or pm ")
            #ampm = str(input("AM or PM "))
            takecommand()

            setAlarm()"""





































#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
"""import pyttsx3  # pip install pyttsx3=2.7 or pyttsx3
import datetime  # inbuilt module
import speech_recognition as sr  # pip install apeechRecognition
import wikipedia  # pip install wikipedia
import webbrowser  # inbuilt module
import os  # inbuilt module
import smtplib  # inbuilt module
import random  # inbuilt module
import getpass

# for taking a voice like david or zara...
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)


# for speak of taken voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good mornning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evenning!")
    speak("HI sir, this is jaarvis. please tell me how may i help you!")


# it takes microphone input from the user and returns string output
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        speak("Opening youtube")
        webbrowser.open("youtube.com")

    elif query.find('google') != -1:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak("Opening google")
        webbrowser.open("google.com")

    elif 'open chrome' in query:
        speak("Opening chrome")
        webbrowser.open("chrome.com")

    elif 'open stackoverflow' in query:
        speak("Opening stackoverflow")
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\VEDEOS'
        songs = os.listdir(music_dir)
        n = len(songs)
        index = random.randint(1, n)
        # print(songs)
        speak("Opening music")

        # songs = random.randint[0,len(songs)]
        os.startfile(os.path.join(music_dir, songs[index]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"SIR, The time is {strTime}")

    elif 'open sublime text' in query:
        path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        speak("Opening sublime text")
        os.startfile(path)

    elif 'open VLC Player' in query:
        path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
        speak("Opening v l c player")
        os.startfile(path)

    elif 'email to ravindra' in query:
        try:
            speak("What should I say?")
            content = takecommand()
            to = "paswanravindra209@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            print("Sorry my friend ravindra. i am not able to send this Email !")

    elif 'open facebook' in query:
        speak("Opening facebook")
        webbrowser.open('facebook.com')

    elif 'according to google' in query:
        speak("Opening google")
        query = query.replace('according to google', "")
        webbrowser.open('https://google.com/#q=' + query, new=2)

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mk5643931@gmail.com', 'mrkhan.**5643931**')
    server.sendmail('mk5643931@gmail.com', to, content)
    server.close()




def killcomand():
    pass



if __name__ == '__main__':
    wishme()

    while (1):
        if query not in query:
            break
        else:
            query = takecommand().lower()

            if "OPEN" in query or "START" in query or "PLAY" in query:
                actoncomand(query)
            elif "CLOSE" in query or "TURN OFF" in query or "TERMINATE" in query:
                killcomand()"""




#################################################################################################################3
#################################################################################################################3



