from os import startfile
from pyautogui import click
from keyboard import write
from time import sleep
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyjokes
import subprocess
from pyttsx3 import speak

from javris import takecommand

"""def whatsappmsg(name,MESSAGE):
    startfile("C:\\Users\\ADMIN\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15)
    click(x=1244, y=1051)
    sleep(1)
    write(name)
    sleep(1)
    click(x=1301, y=1051)
    sleep(1)
    click(x=1299, y=1050)
    sleep(1)
    write(MESSAGE)
    print('Enter')
    whatsappmsg('Aleron DBIT','hi')"""

def notepad():
    speak("tell me the query. ")
    speak("i am ready to write.")
    writes = takecommand().lower()

    time = int(datetime.now().strfile("%H:%M"))
    filename = str(time)+ "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)

    path_1 = "C:\\Users\\ADMIN\\PycharmProjects\\pythonProject6\\automations.py\\"+str(filename)
    path_2 = "C:\\Users\\ADMIN\\PycharmProjects\\pythonProject6\\automations.py\\"+str(filename)
    os.rename = (path_1,path_2)
    os.startfile(path_2)