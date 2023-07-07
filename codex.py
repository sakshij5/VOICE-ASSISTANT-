import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import sys
import time
import pyjokes
import pywhatkit
import datetime
import calendar
import psutil
import pyautogui
import requests
from bs4 import BeautifulSoup


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
     engine.say(audio)
     print(audio)
     engine.runAndWait()

#voice to text
def  takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("listening...")
          r.pause_threshold = 1
          audio = r.listen(source, timeout=1, phrase_time_limit=5)

     try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='en-1n')
          print(f"user said: {query}")

     except Exception as e:
          speak("I could not understand say that again please...")
          return "none"
     return query

#def cpu():
 #   usage = str(psutil.cpu_percent())
  #  speak("CPU percentage is "+usage+" percent")

#def battery():
 #   battery = psutil.sensors_battery()
  #  speak("Battery is at "+ str(battery.percent)+" percent")


#to wish
def wish():
     hour = int(datetime.datetime.now().hour)

     if hour>=0 and hour<=12:
          speak("good morning")
     elif hour>12 and hour<18:
          speak("good afternoon")
     else:
          speak("good evening")

     speak("Hello I am your assistant Alpha")
     #speak("What should I call you?")
     #uname = takecommand()
     #speak("welcome" f"{uname}")
     #speak(uname)
     #print("welcome", uname)

     speak("How can I help you?")

def news():
     main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9dde8f2ab4e14d7a82066e265d027f63'

     main_page = requests.get(main_url).json()
     #print(main_page)
     articles = main_page["articles"]
     #print(articles)
     head = []
     day = ["first","second","third","fourth","fifth"]
     for ar in articles:
          head.append(ar["title"])
     for i in range (len(day)):
          speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
     #takecommand()
     #speak("hello there")
     wish()
     while True:

          query = takecommand().lower()

          #logic building for task
          if "time" in query:
               time = datetime.datetime.now().strftime("%H:%M:%S")
               speak("Its " f"{time}")

          elif "date" in query:
               year = int(datetime.datetime.now().year)
               month = int(datetime.datetime.now().month)
               date = int(datetime.datetime.now().day)
               speak("Its " f"{date} " f"{month} " f"{year} ")
               #speak(month)
               #speak(year)

          elif "open notepad" in query:
               npath = "C:\\WINDOWS\\system32\\notepad.exe"
               os.startfile(npath)
               time.sleep(5)

          elif "close notepad" in query:
               os.system("taskkill/im notepad.exe")

          elif "open command prompt" in query:
               os.system("start cmd")
               time.sleep(5)

          elif "close command prompt" in query:
               os.system("taskkill / f /im cmd.exe")

          elif "wikipedia" in query:
               speak("searching wikipedia...")
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query, sentences=2)
               speak("according to wikipedia")
               speak(results)
               print(results)

          elif "open youtube" in query:
               webbrowser.open("www.youtube.com")
               speak("youtube is open now")
               time.sleep(5)

          elif "close youtube" in query:
               os.system("taskkill/im msedge.exe")
               time.sleep(3)

          elif "open facebook" in query:
               webbrowser.open("www.facebook.com")
               speak("facebook is open now")
               time.sleep(5)

          elif "open gmail" in query:
               webbrowser.open("www.gmail.com")
               speak("gmail is open now")
               time.sleep(5)

          elif "open google" in query:
               speak("What should I search on google?")
               cm = takecommand().lower()
               webbrowser.open(f"{cm}")
               time.sleep(5)

          elif "open news" in query:
               news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
               speak("Here are some headlines from the Times of India")
               time.sleep(5)

          elif "tell me a joke" in query:
               speak(pyjokes.get_joke())

          #elif "send message" in query:
           #    pywhatkit.sendwhatmsg("+91 9004711122", "this is a testing protocol",4, 44)

          elif "play song on youtube" in query:
               pywhatkit.playonyt("mama said that it was ok")

          elif "convert text to handwritten text" in query:
               text = ('Hello I am from Thane')
               pywhatkit.text_to_handwriting(text, save_to="sample.png")

          elif "screenshot" in query:
               img = pyautogui.screenshot()
               speak("What should be the naming convention ?")
               filename = takecommand().lower()
               img.save("C:/Users/ADMIN/OneDrive/Pictures/Screenshots" + filename + ".jpg")
               speak("screenshot taken succesfully!")


          elif "cpu percentage" in query:
               usage = str(psutil.cpu_percent())
               speak("CPU percentage is " + usage + " percent")

          elif "battery percentage" in query:
               battery = psutil.sensors_battery()
               speak("Battery percentage is "+ str(battery.percent)+" percent")

          elif "temperature" in query:
               speak("in which city ?")
               city = takecommand().lower()
               search = (f"temperature in {city}")
               url = f"www.google.com/search?q=(search)"
               r=requests.get(url)
               data = BeautifulSoup(r.text,"html.parser")
               temp =data.find("div",class_="BNeawe").text
               speak(f"Current {search} is {temp}")

          elif "no thanks" in query:
               speak("Thank you for your time, have a good day!")
               sys.exit()

          speak("Do you have any other work?")


