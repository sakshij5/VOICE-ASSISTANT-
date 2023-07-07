#from bs4 import beautifulsoup
import requests
import csv
import pandas as pd



import os

import geopy
import geocoder
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import datetime
#import osssa
import sys
import time
import webbrowser
import pyautogui
import pyjokes
import subprocess
import requests
from word_write_feature import write
#import BeautifulSoup
from bs4 import BeautifulSoup

import json
#import keyboard
#from os import startfile
#from time import sleep
#from keyboard import press
#from keyboard import write
#from pyautogui import click
#import SECURITY as SE
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from userHandler import UserData
import FACE_UNLOCKER as FU
"""
background, textColor = 'black', '#F6FAFB'
background, textColor = textColor, background

avatarChoosen = 0
choosedAvtrImage = None
user_name = ''
user_gender = ''

try:
     face_classifier = cv2.CascadeClassifier(
          'C:/Users/ADMIN/PycharmProjects/pythonProject6/Cascade/haarcascade_frontalface_default.xml')
except Exception as e:
     print('Cascade File is missing...')
     raise SystemExit

if os.path.exists('userData') == False:
     os.mkdir('userData')
if os.path.exists('userData/faceData') == False:
     os.mkdir('userData/faceData')


###### ROOT1 ########
def startLogin():
     try:
          result = FU.startDetecting()
          if result:
               user = UserData()
               user.extractData()
               userName = user.getName().split()[0]
               welcLbl['text'] = 'Hi ' 'sakshi '',\nWelcome to the world of\nScience & Technology'
               loginStatus['text'] = 'UNLOCKED'
               loginStatus['fg'] = 'green'
               faceStatus['text'] = '(Logged In)'
               #os.system('python GUIASSISTANT.py')
               return
          
          else:
               print('Error Occurred')

     except Exception as e:
          print(e)


####### ROOT2 ########
def trainFace():
     data_path = 'userData/faceData/'
     onlyfiles = [f for f in os.listdir(data_path) if isfile(join(data_path, f))]

     Training_data = []
     Labels = []

     for i, files in enumerate(onlyfiles):
          image_path = data_path + onlyfiles[i]
          images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

          Training_data.append(np.asarray(images, dtype=np.uint8))
          Labels.append(i)

     Labels = np.asarray(Labels, dtype=np.int32)

     model = cv2.face.LBPHFaceRecognizer_create()
     model.train(np.asarray(Training_data), np.asarray(Labels))

     print('Model Trained Successfully !!!')
     model.save('userData/trainer.yml')
     print('Model Saved !!!')


def face_extractor(img):
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_classifier.detectMultiScale(gray, 1.3, 5)

     if faces is ():
          return None

     for (x, y, w, h) in faces:
          cropped_face = img[y:y + h, x:x + w]

     return cropped_face


cap = None
count = 0


def startCapturing():
     global count, cap
     ret, frame = cap.read()
     if face_extractor(frame) is not None:
          count += 1
          face = cv2.resize(face_extractor(frame), (200, 200))
          face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

          file_name_path = 'userData/faceData/img' + str(count) + '.png'
          cv2.imwrite(file_name_path, face)
          print(count)
          progress_bar['value'] = count

          cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
     else:
          pass

     if count == 100:
          progress_bar.destroy()
          lmain['image'] = defaultImg2
          statusLbl['text'] = '(Face added successfully)'
          cap.release()
          cv2.destroyAllWindows()
          Thread(target=trainFace).start()
          addBtn['text'] = '        Next        '
          addBtn['command'] = lambda: raise_frame(root3)
          return

     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
     frame = cv2.flip(frame, 1)
     img = Image.fromarray(frame)
     imgtk = ImageTk.PhotoImage(image=img)
     lmain.imgtk = imgtk
     lmain.configure(image=imgtk)
     lmain.after(10, startCapturing)


def Add_Face():
     global cap, user_name, user_gender
     user_name = nameField.get()
     user_gender = r.get()
     if user_name != '' and user_gender != 0:
          if agr.get() == 1:
               cap = cv2.VideoCapture(0)
               startCapturing()
               progress_bar.place(x=20, y=273)
               statusLbl['text'] = ''
          else:
               statusLbl['text'] = '(Check the Condition)'
     else:
          statusLbl['text'] = '(Please fill the details)'


def SuccessfullyRegistered():
     if avatarChoosen != 0:
          gen = 'Male'
          if user_gender == 2: gen = 'Female'
          u = UserData()
          u.updateData(user_name, gen, avatarChoosen)
          usernameLbl['text'] = user_name
          raise_frame(root4)


def selectAVATAR(avt=0):
     global avatarChoosen, choosedAvtrImage
     avatarChoosen = avt
     i = 1
     for avtr in (avtb1, avtb2, avtb3, avtb4, avtb5, avtb6, avtb7, avtb8):
          if i == avt:
               avtr['state'] = 'disabled'
               userPIC['image'] = avtr['image']
          else:
               avtr['state'] = 'normal'
          i += 1


################################################# GUI ###############################


def raise_frame(frame):
     frame.tkraise()


if __name__ == '__main__':

     root = Tk()
     root.title('F.R.I.D.A.Y.')
     w_width, w_height = 350, 600
     s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
     x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
     root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
     root.configure(bg=background)
     # root.attributes('-toolwindow', True)
     root1 = Frame(root, bg=background)
     root2 = Frame(root, bg=background)
     root3 = Frame(root, bg=background)
     root4 = Frame(root, bg=background)

     for f in (root1, root2, root3, root4):
          f.grid(row=0, column=0, sticky='news')

     ################################
     ########  MAIN SCREEN  #########
     ################################

     image1 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/home2.jpg')
     image1 = image1.resize((300, 250))
     defaultImg1 = ImageTk.PhotoImage(image1)

     dataFrame1 = Frame(root1, bd=10, bg=background)
     dataFrame1.pack()
     logo = Label(dataFrame1, width=300, height=250, image=defaultImg1)
     logo.pack(padx=10, pady=10)

     # welcome label
     welcLbl = Label(root1, text='Hi there,\nWelcome to the world of\nScience & Technology', font=('Arial Bold', 15),
                     fg='#303E54', bg=background)
     welcLbl.pack(padx=10, pady=20)

     # add face
     loginStatus = Label(root1, text='LOCKED', font=('Arial Bold', 15), bg=background, fg='red')
     loginStatus.pack(pady=(40, 20))

     if os.path.exists('userData/trainer.yml') == False:
          loginStatus['text'] = 'Your Face is not registered'
          addFace = Button(root1, text='   Register Face   ', font=('Arial', 12), bg='#018384', fg='white', relief=FLAT,
                           command=lambda: raise_frame(root2))
          addFace.pack(ipadx=10)
     else:
          # pass
          Thread(target=startLogin).start()

     # status of add face
     faceStatus = Label(root1, text='(Face Not Detected)', font=('Arial 10'), fg=textColor, bg=background)
     faceStatus.pack(pady=5)

     ##################################
     ########  FACE ADD SCREEN  #######
     ##################################

     image2 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/defaultFace4.png')
     image2 = image2.resize((300, 250))
     defaultImg2 = ImageTk.PhotoImage(image2)

     dataFrame2 = Frame(root2, bd=10, bg=background)
     dataFrame2.pack(fill=X)
     lmain = Label(dataFrame2, width=300, height=250, image=defaultImg2)
     lmain.pack(padx=10, pady=10)

     # Details
     detailFrame2 = Frame(root2, bd=10, bg=background)
     detailFrame2.pack(fill=X)
     userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
     userFrame2.pack(padx=10, pady=10)

     # progress
     progress_bar = ttk.Progressbar(root2, orient=HORIZONTAL, length=303, mode='determinate')

     # name
     nameLbl = Label(userFrame2, text='Name', font=('Arial Bold', 12), fg='#303E54', bg=background)
     nameLbl.place(x=10, y=10)
     nameField = Entry(userFrame2, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
     nameField.focus()
     nameField.place(x=80, y=10)

     genLbl = Label(userFrame2, text='Gender', font=('Arial Bold', 12), fg='#303E54', bg=background)
     genLbl.place(x=10, y=50)
     r = IntVar()
     s = ttk.Style()
     s.configure('Wild.TRadiobutton', background=background, foreground=textColor, font=('Arial Bold', 10),
                 focuscolor=s.configure(".")["background"])
     genMale = ttk.Radiobutton(userFrame2, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
     genMale.place(x=80, y=52)
     genFemale = ttk.Radiobutton(userFrame2, text='Female', value=2, variable=r, style='Wild.TRadiobutton',
                                 takefocus=False)
     genFemale.place(x=150, y=52)

     # agreement
     agr = IntVar()
     sc = ttk.Style()
     sc.configure('Wild.TCheckbutton', background=background, foreground='#303E54', font=('Arial Bold', 10),
                  focuscolor=sc.configure(".")["background"])
     # agree = Checkbutton(userFrame2, text='I agree to use my face for Security purpose', fg=textColor, bg=background, activebackground=background, activeforeground=textColor)
     agree = ttk.Checkbutton(userFrame2, text='I agree to use my Face for Security', style='Wild.TCheckbutton',
                             takefocus=False, variable=agr)
     agree.place(x=28, y=100)
     # add face
     addBtn = Button(userFrame2, text='    Add Face    ', font=('Arial Bold', 12), bg='#01933B', fg='white',
                     command=Add_Face, relief=FLAT)
     addBtn.place(x=90, y=150)

     # status of add face
     statusLbl = Label(userFrame2, text='', font=('Arial 10'), fg=textColor, bg=background)
     statusLbl.place(x=80, y=190)

     ##########################
     #### AVATAR SELECTION ####
     ##########################

     Label(root3, text="Choose Your Avatar", font=('arial', 15), bg=background, fg='#303E54').pack()

     avatarContainer = Frame(root3, bg=background, width=300, height=500)
     avatarContainer.pack(pady=10)
     size = 100

     avtr1 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a1.png')
     avtr1 = avtr1.resize((size, size))
     avtr1 = ImageTk.PhotoImage(avtr1)
     avtr2 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a2.png')
     avtr2 = avtr2.resize((size, size))
     avtr2 = ImageTk.PhotoImage(avtr2)
     avtr3 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a3.png')
     avtr3 = avtr3.resize((size, size))
     avtr3 = ImageTk.PhotoImage(avtr3)
     avtr4 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a4.png')
     avtr4 = avtr4.resize((size, size))
     avtr4 = ImageTk.PhotoImage(avtr4)
     avtr5 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a5.png')
     avtr5 = avtr5.resize((size, size))
     avtr5 = ImageTk.PhotoImage(avtr5)
     avtr6 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a6.png')
     avtr6 = avtr6.resize((size, size))
     avtr6 = ImageTk.PhotoImage(avtr6)
     avtr7 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a7.png')
     avtr7 = avtr7.resize((size, size))
     avtr7 = ImageTk.PhotoImage(avtr7)
     avtr8 = Image.open('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/avatars/a8.png')
     avtr8 = avtr8.resize((size, size))
     avtr8 = ImageTk.PhotoImage(avtr8)

     avtb1 = Button(avatarContainer, image=avtr1, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(1))
     avtb1.grid(row=0, column=0, ipadx=25, ipady=10)

     avtb2 = Button(avatarContainer, image=avtr2, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(2))
     avtb2.grid(row=0, column=1, ipadx=25, ipady=10)

     avtb3 = Button(avatarContainer, image=avtr3, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(3))
     avtb3.grid(row=1, column=0, ipadx=25, ipady=10)

     avtb4 = Button(avatarContainer, image=avtr4, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(4))
     avtb4.grid(row=1, column=1, ipadx=25, ipady=10)

     avtb5 = Button(avatarContainer, image=avtr5, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(5))
     avtb5.grid(row=2, column=0, ipadx=25, ipady=10)

     avtb6 = Button(avatarContainer, image=avtr6, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(6))
     avtb6.grid(row=2, column=1, ipadx=25, ipady=10)

     avtb7 = Button(avatarContainer, image=avtr7, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(7))
     avtb7.grid(row=3, column=0, ipadx=25, ipady=10)

     avtb8 = Button(avatarContainer, image=avtr8, bg=background, activebackground=background, relief=FLAT, bd=0,
                    command=lambda: selectAVATAR(8))
     avtb8.grid(row=3, column=1, ipadx=25, ipady=10)

     Button(root3, text='         Submit         ', font=('Arial Bold', 15), bg='#01933B', fg='white', bd=0,
            relief=FLAT, command=SuccessfullyRegistered).pack()

     #########################################
     ######## SUCCESSFULL REGISTRATION #######
     #########################################

     userPIC = Label(root4, bg=background, image=avtr1)
     userPIC.pack(pady=(40, 10))
     usernameLbl = Label(root4, text="Roshan Kumar", font=('Arial Bold', 15), bg=background, fg='#85AD4F')
     usernameLbl.pack(pady=(0, 70))

     Label(root4, text="Your account has been successfully activated!", font=('Arial Bold', 15), bg=background,
           fg='#303E54', wraplength=300).pack(pady=10)
     Label(root4, text="Launch the APP again to get started the conversation with your Personal Assistant",
           font=('arial', 13), bg=background, fg='#A3A5AB', wraplength=350).pack()

     Button(root4, text='     OK     ', bg='#0475BB', fg='white', font=('Arial Bold', 18), bd=0, relief=FLAT,
            command=lambda: quit()).pack(pady=50)

     root.iconbitmap('C:/Users/ADMIN/PycharmProjects/pythonProject6/extrafiles/images/assistant2.ico')
     raise_frame(root1)
     root.mainloop()
"""

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
#engine.setProperty('voices', voices[0].id)

#for voice in voices:
#    print(voice.id)
print("Available voice options:")
"""engine.setProperty('voice',voices[0].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('voice',voices[2].id)
engine.setProperty('voice',voices[3].id)
engine.setProperty('voice',voices[4].id)"""
print("david, ravi,mark,heera,zira")
val = input("Enter your choice: ")
print(val)
if val=='david':
      engine.setProperty('voice',voices[0].id)
elif val=='ravi':
     engine.setProperty('voice', voices[1].id)
elif val=='mark':
     engine.setProperty('voice', voices[2].id)
elif val=='heera':
     engine.setProperty('voice', voices[3].id)
elif val=='zira':
     engine.setProperty('voice', voices[4].id)

#for voice in voices:
 #    print(voice.id)
     #engine.setProperty('voice',voices[2].id)


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


#to wish
def wish():
     hour = int(datetime.datetime.now().hour)

     if hour>=0 and hour<=12:
          speak("Good Morning")
     elif hour>12 and hour<18:
          speak("Good Afternoon")
     else:
          speak("Good Evening")

     speak("Hello I am your assistant Alpha")
     """print('please enter username')
     username = input()
     if username == 'Aleron' or username == 'Sanika' or username == 'Sakshi':
          print('Hello'  + username +  '\nplease enter your password')
          password = input()
          if username == 'Aleron' and password == 'abc123':
               print('Access granted')
          elif username == 'Sanika' and password == '1234':
               print('Access granted')
          elif username == 'Sakshi' and password == '9999':
               print('Access granted')
          else:
               print('Incorrect Password')
               print('access denied')
               quit()
     else:
          print('no such username!')
          print('Access denied')
          quit()"""
     #speak("What should I call you?")
     #uname = takecommand()
     #speak("welcome"  f"{uname}")
     #speak(uname)
     #print("welcome", uname)

     speak("How can I help you?")

"""def googlemaps(place):
     url_place= "https://www.google.com/maps/place/" + str(place)
     geolocater = Nominatim(user_agent= "myGeocoder")
     location = geolocater.geocode(place,addressdetails= True)
     target_latlon =location.latitude ,location.longitude
     location = location .raw['address']
     target = { city :location.get('city',''),
               state :location.get('state',''),
               country :location.get('country','')}
     current_loca =geocoder.ip('me')
     current_loca = current_loca.latlng
     distance = str(great_circle(current_latlon,target_latlon))
     distance = str(distance.split(' ',1)[0])
     distance = round(float(distance),2)
     web.open(url=url_place)
     speak(target)
     speak(f"maam ,{place} is {distance} kilometer away from you ")
     googlemaps('mumbai')"""


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

"""def notepad():
    speak("tell me the query. ")
    speak("i am ready to write.")
    writes = takecommand().lower()

    time = datetime.datetime.now().strfile("%H:%M")
    filename = str(time).replace(":","-")+ "-note.txt"
    filename = "demo1" +"-note.txt"
    with open(filename,"w") as file:
        file.write(writes)

    path_1 = "C:\\Users\\ADMIN\\PycharmProjects\\pythonProject6\\automations.py\\"+str(filename)
    path_2 = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\notepad file\\"
    os.rename = (path_1,path_2)
    os.startfile(path_2)
"""

def notepad():
     speak("Tell me the query.")
     speak("I am ready to write.")
     writes = takecommand()
     speak('What should I name this file ?')
     fname = takecommand().lower()
     filename = str(fname) + "-note.txt"
     with open(filename,"w") as file:
          file.write(writes)
     path1 = "C:\\Users\\ADMIN\\PycharmProjects\\pythonProject6\\" + str(filename)
     os.startfile(path1)
     #time.sleep(3)
     speak('I have saved your file')

def word():
     """
     speak("Tell me the query.")
     speak("I am ready to write.")
     writes1 = takecommand()
     speak('What should I name this file ?')
     fname1 = takecommand().lower()
     filename1 = str(fname1) + ".docx"
     with open(filename1,"w") as file:
          file.write(writes1)
     path10 = "C:\\Users\\DELL\\PycharmProjects\\pythonProject1\\" + str(filename1)
     os.startfile(path10)
     #time.sleep(3)
     speak('I have saved your file')
     """
     speak("What should I enter in the file?")
     content = takecommand()
     speak("What should I name it?")
     filename = takecommand()
     write(content=content, filename=filename)




"""def whatsapp(name,message):
    startfile("C:\\Users\\ADMIN\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=195,y=115)
    sleep(1)
    write(name)
    sleep(2)
    click(x=118,y=249)
    sleep(1)
    click(x=571,y=690)
    sleep(1)
    write(message)
    press ('enter')
    whatsapp('mummy','hiii')"""

"""def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ") """






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
               notepad()
               time.sleep(5)
               #time.sleep(5)

          elif "close notepad" in query:
               os.system("taskkill /f /im notepad.exe")

          elif "open command prompt" in query:
               os.system("start cmd")
               time.sleep(5)

          elif "close command prompt" in query:
               os.system("taskkill /f /im cmd.exe")

          elif "details" in query:
               speak("searching wikipedia...")
               query = query.replace("details", "")
               results = wikipedia.summary(query, sentences=2)
               speak("according to wikipedia")
               speak(results)
               print(results)

          elif "open youtube" in query:
               #webbrowser.open("www.youtube.com")
               #speak("youtube is open now")
               #speak("what should I play on youtube?")
               #pl = takecommand().lower()
               #c = webbrowser.get("Chrome")
               #c.open(f"{pl}")
               #webbrowser.get('msedge').open(f"{pl}")
               speak("what should I play on youtube?")
               rqst = takecommand().lower()
               pywhatkit.playonyt(f"{rqst}")
               speak("Here you go")
               time.sleep(5)

          elif "close youtube" in query:
               os.system("taskkill /f /im msedge.exe")
               time.sleep(3)

          elif "open facebook" in query:
               webbrowser.open("www.facebook.com")
               speak("facebook is open now")
               time.sleep(5)

          elif "close facebook" in query:
               os.system("taskkill /f /im msedge.exe")
               time.sleep(3)

          elif "open gmail" in query:
               webbrowser.open("www.gmail.com")
               speak("gmail is open now")
               time.sleep(5)

          elif "open google" in query:
               speak("What should I search on google?")
               cm = takecommand().lower()
               pywhatkit.search(f"{cm}")
               time.sleep(5)

          elif "close google" in query:
               os.system("taskkill /f /im msedge.exe")
               time.sleep(3)

          elif "tell me news" in query:
               speak("Here are some headlines")
               news()
               time.sleep(3)


          elif "shut down" in query:
               speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
               subprocess.call(["shutdown", "/l"])

          #elif "close news" in query:
            #  os.system("taskkill /f /im msedge.exe")
             # time.sleep(3)

          elif "tell me a joke" in query:
               speak(pyjokes.get_joke())

          #elif "send message" in query:
              # pywhatkit.sendwhatmsg("+91 9004711122", "this is a testing protocol",4, 44)

          elif "convert text to handwritten text" in query:
               speak("which text should I convert?")
               text = takecommand()
               speak("what should I name this file?")
               file = takecommand().lower()
               time.sleep(3)
               pywhatkit.text_to_handwriting(f"{text}", save_to=f"{file}.png")
               speak("I have converted the text")


          #elif "location" in query:
               #GoogleMaps(Place)

          elif "take screenshot" in query:
               speak("what should I name this file?")
               name = takecommand().lower()
               speak("hold the screen for few seconds, I am taking a screenshot")
               time.sleep(3)
               img = pyautogui.screenshot()
               img.save(f"{name}.png")
               speak("the screenshot has been saved")





          elif "weather" in query:
               api_key = "7af7806b99e3d7605f9765803c40782a"
               base_url = "https://api.openweathermap.org/data/2.5/weather?"
               speak("what is the city name")
               city_name = takecommand().lower()
               complete_url = base_url + "appid=" + api_key + "&q=" + city_name
               response = requests.get(complete_url)
               x = response.json()
               if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

          elif "compare" in query:
                    speak("What should I compare ?")
                    cm = takecommand().lower()
                    pywhatkit.search(f"{cm}")
                    time.sleep(5)

          elif 'word' in query:
               word()





          elif "no thanks" in query:
               speak("Thank you for your time, have a good day!")
               sys.exit()

          speak("Do you have any other work?")