import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import subprocess
import keyboard
import requests


r = sr.Recognizer()


def voice(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def respon():
    print("okey dude!!!")
    voice("okey dude!")


def ulang():
    print('How can i help you again dude? y/n?')
    while True:
        if(keyboard.is_pressed("shift+`")):
            exit()
        elif(keyboard.is_pressed("`")):
            return False


def start():
    print('How can i help you dude? y/n?')
    while True:
        if(keyboard.is_pressed("shift+`")):
            exit()
        elif(keyboard.is_pressed("`")):
            return False


def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print("Koneksikan ke Internet!!!")
        return False


print("Hallo dude, How Are You?")
voice("Hallo dude, How Are You?")
start()
while True:
    checkInternetRequests()
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("What i can help you???")
            voice("What i can help you?")
            audio_text = r.listen(source)
            x = r.recognize_google(audio_text).lower()
            print("Hasil : " + x)
            if (x == "open notepad" or x == "buka notepad" or x == "notepad"):
                respon()
                subprocess.call("C://Windows//notepad.exe")
                ulang()
            elif (x == "open folder" or x == "buka folder" or x == "folder" or x == "explorer"):
                respon()
                subprocess.call("C://Windows//explorer.exe")
                ulang()
            elif (x == "open game 1" or x == "buka game 1" or x == "game 1"):
                respon()
                subprocess.call(
                    "C://ProgramData//Microsoft//Windows//Start Menu//Programs//Riot Games//VALORANT")
                ulang()
            elif (x == "code" or x == "lets code" or x == "let's code"):
                respon()
                os.startfile(
                    "C://Users//HP//AppData//Local//Programs//Microsoft VS Code//Code.exe")
                ulang()
            elif (x == "spotify" or x == "music"):
                respon()
                os.startfile(
                    "C://Users//HP//AppData//Roaming//Spotify//Spotify.exe")
                ulang()
            elif (x == "discord"):
                respon()
                subprocess.call(
                    "C://Users//HP//AppData//Local//Discord//Update.exe --processStart Discord.exe")
                ulang()
            elif (x == "open chrome" or x == "buka chrome" or x == "chrome"):
                respon()
                print("What do you want to search ??? ")
                voice("What do you want to search?")
                search_text = r.listen(source)
                y = r.recognize_google(search_text).lower()
                url = "https://www.google.com.tr/search?q={}".format(y)
                webbrowser.register('chrome',
                                    None,
                                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
                ulang()
            elif (x == "open youtube" or x == "buka youtube" or x == "youtube"):
                respon()
                print("What do you want to search ??? ")
                voice("What do you want to search?")
                search_text = r.listen(source)
                y = r.recognize_google(search_text).lower()
                url = "https://www.youtube.com/results?search_query={}".format(
                    y)
                webbrowser.register('chrome',
                                    None,
                                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
                ulang()
            elif (x == "youtube my playlist"):
                respon()
                url = "https://www.youtube.com/playlist?list=PLCdRkjurqUw2iBpM00wF5pHWqKZtBIEqG"
                webbrowser.register('chrome',
                                    None,
                                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
                ulang()
            elif (x == "buka laporan" or x == "laporan"):
                respon()
                os.startfile(
                    "D://TUGAS//PROYEK 1//proyek_kuliah//Kelompok//Proyek 1//Revisi 3.docx")
                ulang()
            elif (x == "open whatsapp" or x == "buka whatsapp" or x == "whatsapp"):
                respon()
                url = "https://web.whatsapp.com/"
                webbrowser.register('chrome',
                                    None,
                                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
                ulang()
            elif (x == "bye"):
                voice("See you next time dude")
                break
            elif (x == "skip"):
                voice("Okey dude")
                ulang()
            elif (x == "sleep"):
                respon()
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                ulang()
            elif (x == "shutdown" or x == "shut down"):
                respon()
                os.system("shutdown /s /t 1")
                break
            elif (x == "restart"):
                respon()
                os.system("shutdown /r /t 1")
                break
            else:
                print("Sorry dude, Your command is not registered -_-")
                voice("Sorry dude, Your command is not registered")
        except sr.UnknownValueError:
            print("Sorry, tell me what can I help you?")
