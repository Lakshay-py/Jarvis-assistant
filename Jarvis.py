 # modules
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import operator
import random
import os.path
import time
from bs4 import BeautifulSoup
import psutil
import speedtest
import urllib
import numpy as np
from googletrans import Translator
from pytube import YouTube
import keyboard
from playsound import playsound
from pywikihow import search_wikihow
import cartopy.crs as ccrs
import matplotlib.pyplot as plt



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty(voices, voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=120,phrase_time_limit=30)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis sir. Please tell me how may I help you")

# for news
def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4b75e9f4cfe640ce8114091ffb9731b3"

    main_page = requests.get(main_url).json()
    #print main page
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print
        speak(f"today's {day[1]} news is: {head[i]}")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

# logic building for offline tasks
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open code" in query:
            vpath = "C:\\Users\\Ashok Sharma\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(vpath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open chrome" in query:
            chpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
            os.startfile(chpath)

        elif "open picasa" in query:
            pipath = "C:\\Program Files (x86)\\Google\\Picasa3\\Picasa3"
            os.startfile(pipath)

        elif "open power point" in query:
             powerpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT"
             os.startfile(powerpath)

        elif "open settings" in query:
            settingpath = "C:\\WINDOWS\\System32\\control"
            os.startfile(settingpath)

        elif "open zoom" in query:
            zoompath = "C:\\Users\\Ashok Sharma\\AppData\\Roaming\\Zoom\\bin\\Zoom"
            os.startfile(zoompath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k==27:
                    break
                cap.release()
                cv2.destroyAllWindows()

# online works
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
           # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open byjus" in query:
            webbrowser.open("www.byjus.com")

        elif "open cbse" in query:
            webbrowser.open("www.learncbse.com")

        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message"  in query:
            kit.sendwhatmsg("+919992013111", "aur papa", 12, 35)

        elif "track" in query:

            from Nasa import IssTracker

            IssTracker()

# tasks
        if "close notepad" in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
            speak("Okay sir, closing command prompt")
            os.system("taskkill /f /im cmd")

        elif "close chrome" in query:
            speak("Okay sir, closing chrome")
            os.system("taskkill /f /im chrome")

        elif "close picasa" in query:
            speak("Okay sir, closing picasa")
            os.system("taskkill /f /im \Picasa3")

        elif "close code" in query:
            speak("Okay sir, closing VS code")
            os.system("taskkill /f /im Microsoft VS Code")

        elif " close settings" in query:
            speak("Okay sir, closing settings")
            os.system("taskkill /f /im control")

        elif " close zoom" in query:
            speak("Okay sir, closing zoom")
            os.system("taskkill /f /im Zoom")

        elif " close camera" in query:
            speak("Okay sir, closing camera")
            os.system("taskkill /f /im webcam")



# jokes
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

#system on off commands
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("restart /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powerprof.d11,SetSuspendState 0,1,0")

# switch window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

# news      
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news.")
            news()

# location
        elif "where i am" in query or "where are we" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = 'https//get.geojs.io/v1/ip/geo/' +ipAdd+ ".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data["city"]
                state = geo_data["state"]
                country = geo_data["country"]
                speak(f"Sir I am not sure, but I think we are in {city} city of {state} state of {country} country")
            except Exception as e:
                speak("Sorry sir, Due to network issue I am not able to find where we are.")
                pass

# screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir, Please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("Please sir, hold the screen for a few seconds. I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, screenshot is saved in our main folder. Now I am ready for next command")

# wake
        elif "wake up jarvis" in query:
            speak("Hello sir")
            speak("tell me how may I help you") 

        elif "about" in query:
            from Nasa import Summary
            query = query.replace("jarvis ", "")
            query = query.replace("about ", "") 
            Summary(query)

# secreen recorder
      #  elif "record" in query:
      #      from screenrecorder import ScreenRecorder
        

# remember
        elif "remember that" in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = rememberMsg.replace("jarvis", "")
            speak("You told me to remember that :"+rememberMsg)
            remember = open("data.txt", "w")
            remember.write(rememberMsg)
            remember.close()

# remember what
        elif "what do you remember" in query:
            remember = open('data.txt','r')
            speak("You told me that" + remember.read())

        elif "how to" in query:
            speak("Getting data from internet")
            sz = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(sz,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

# exit
        elif "bye" in query or "exit" in query:
            speak("Okay sir, thanks for using me. Have a good day.")
            sys.exit()


# battery
        elif "how much battery left" in query or "how much power do we have" in query or "battery left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery left")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage<15:
                speak("we have very low power, please connect to charging, the system will shutdown very soon")
      
# Satellites
        elif "space news" in query:

            speak("Tell me the date for news extracting process.")

            Date = input("Enter Date:")

            from Features import DateConverter

            value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Date)

            NasaNews(value)

# folders
        elif "new folder" in query:
            speak("Sir, pleas tell me the name of folder")
            from folders import Newfolder         

# internet speed
        elif "internet speed" in query:

            st = speedtest.Speedtest()
            dl = st.upload()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

# volume control
        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query:
            pyautogui.press("volumemute")

# hide
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Sir please tell me, you want to hide this folder or make it visible to everyone")
            foundation = takecommand().lower()
            if "hide" in foundation:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden.")

            elif "visible" in foundation:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I wish you are making this decision in your place")

            elif "leave it" in foundation or "leave for now" in foundation:
                speak("Ok sir")

# mobile camera
        elif "mobile camera" in query:
            URL = "http://192.168.43.1:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow("IPWebcam",img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows()    

# brightness control
        elif "brightness up" in query:
            pyautogui.press("brightnessup")

        elif "brightness down" in query:
            pyautogui.press("brightnessdown")

# repeat words
        elif "repeat my words" in query:
            speak("Speak Sir!")
            jj = takecommand().lower()
            speak(f"You said : {jj}")

# Alarm
        elif "alarm" in query:
            speak("Sir please tell me the time!")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir")
                    playsound("Alarm.mp3")
                    speak("Alarm Closed!")

                elif now>time:
                    break


#  temp
def Temp():
       ''' if "temperature" in query:
         search = "temperature in bhiwani"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text, "html.parser")
         temperature = data.find("div",class_ = "BNeawe").text
         speak(f"The Temperature outside is {temperature} clsius")

         speak("Do I have to tell you temperature of another place?")
         next = takecommand().lower()

         if "yes" in next:
             speak("Tell me the name of the place")
             name = takecommand().lower()
             search = f"temperature in {name}"
             url = f"https://www.google.com/search?q={search}"
             r = requests.get(url)
             data = BeautifulSoup(r.text, "html.parser")
             temperature = data.find("div",class_ = "BNeawe").text
             speak(f"The Temperature in {name} is {temperature} clsius")

         else:
             speak("No problem sir") '''

def YouTubeAuto():

     speak("What's Your Command ?")
     comm = takecommand().lower()

     if "pause" in comm:
        keyboard.press("space bar")

     elif "restart" in comm:
        keyboard.press("0")
    
     elif "mute" in comm:
        keyboard.press("m")

     elif "skip" in comm:
        keyboard.press("l")

     elif "back" in comm:
        keyboard.press("j")

     elif "full screen" in comm:
        keyboard.press("f")

     elif "film mode" in comm:
        keyboard.press("t")

     speak("Done sir")

def ChromeAuto():
    speak("Chrome Automation Started")

    command = takecommand().lower()

    if "close this tab" in command:
        keyboard.press_and_release("ctrl + w")

    elif "open new tab" in command:
        keyboard.press_and_release("ctrl + t")

    elif "open new window" in command:
        keyboard.press_and_release("ctrl + n")

    elif "history" in command:
        keyboard.press_and_release("ctrl + h")

# for temperature
    elif "temperature" in query:
        Temp()

def My_Location():


     og = "https://www.google.co.in/maps/dir/28.8023798,76.143591//@28.8025122,76.07355,12z/data=!4m4!4m3!1m1!4e1!1m0"

     speak("Checking...")

     webbrowser.open(og)

     ip_add = requests.get('https://api.ipify.org').text

     url = "https//get.geojs.io/v1/ip/geo/" + ip_add + '.json'

     geo_q = requests.get(url)

     geo_d = geo_q.json()

     state = geo_d['city']

     country = geo_d['country']

     speak(f"Sir, we are in {state , country} .")





