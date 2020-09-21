import subprocess as sp
import platform
import sys

import pyttsx3


def speak(text):
    pyttsx3.speak(text)
    engine.runAndWait()


if __name__ == '__main__':

    # Check OS Type
    sys_type = platform.system()

    # init pyttsx3
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate', engine.getProperty('rate') + 50)

    print()
    print("-" * 39)
    print("\n******* Welcome To My Assistant *******\n")
    print("-" * 39)
    print("**** For Windows And Linux OS Only ****")
    print("-" * 39)

    # Welcome Message
    speak("Welcome")
    
    # Validate For Windows And Linux Only
    if sys_type != "Linux" and sys_type != "Windows":
        print("****** This System Not Supported ******")
        sys.exit("Closing Assistant")
        print("-" * 39)

    print("\t\t[ Menu ]")
    print("-" * 39)
    print("*** Choose Any One Of The Following ***")
    print("-" * 39)
    print()
    speak("I can do the following")

    if sys_type == "Windows":
        print("Chrome Browser || Firefox Browser")
        print()
        print("Calculator || Visual Studio Code")
        print()
        print("Gimp || Notepad || Calender || Discord")
        print()
        print("VLC Media Player || Windows Media Player")
        
    elif sys_type == "Linux":
        print("Chrome Browser || Firefox Browser")
        print()
        print("Gimp || Blender || Gedit || Calendar")
        print()
        print("Discord || Chess || To-Do || Calculator")
        print()
        print("Visual Studio Code || VLC Media Player")
    print()
    print()
    print("To exit app type exit or quit or close")
    print("-" * 39)
    print("To clear the console type clear or cls")
    print("-" * 39)
    print("To exit the opened tool press Ctrl + C")
    print("-" * 39)

    while True:

        # Ask For Query
        speak("What can i do for you")
        print()

        # Taking Query From User
        query = input("\nWhat can i do for you ? ").strip().lower()

        spout = ()

        # Printing User Query
        print("\nYour Query :: ", query, end="\n\n")

        if "don't" in query or "do not" in query or "never" in query or "not do" in query or "must not" in query or "nope" in query:
            continue
        if "clear" in query or "cls" in query:
            if sys_type == "Windows":
                spout = sp.getstatusoutput("cls")
                if spout[0] != 0:
                    print(spout[1])
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("clear")
                if spout[0] != 0:
                    print(spout[1])
        elif "ip" in query or "ip address" in query or "address" in query:
            if sys_type == "Windows":
                spout = sp.getstatusoutput("ipconfig")
                if spout[0] == 0:
                    print(spout[1])
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("ifconfig")
                if spout[0] == 0:
                    print(spout[1])
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("chrome" in query
        or "browser" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start chrome")
                if spout[0] == 0:
                    speak("Chrome Closed")
                else:
                    speak("Chrome Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("google-chrome")
                if spout[0] == 0:
                    speak("Chrome Closed")
                else:
                    speak("Chrome Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("firefox" in query
        or "browser" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start firefox")
                if spout[0] == 0:
                    speak("Firefox Closed")
                else:
                    speak("Firefox Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("firefox")
                if spout[0] == 0:
                    speak("Firefox Closed")
                else:
                    speak("Firefox Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("discord" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start discord")
                if spout[0] == 0:
                    speak("Discord Closed")
                else:
                    speak("Discord Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("discord")
                if spout[0] == 0:
                    speak("Discord Closed")
                else:
                    speak("Discord Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("windows media player" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start wmplayer")
                if spout[0] == 0:
                    speak("Windows Media Player Closed")
                else:
                    speak("Windows Media Player Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("calculator" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start calculator:")
                if spout[0] == 0:
                    speak("Calculator Closed")
                else:
                    speak("Calculator Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("gnome-calculator")
                if spout == 0:
                    speak("Calculator Closed")
                else:
                    speak("Calculator Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query or "show") and ("calendar" in query
        or "date" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start calendar:")
                if spout[0] == 0:
                    speak("Calendar Closed")
                else:
                    speak("Calendar Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("gnome-calendar")
                if spout[0] != 0:
                    print(sp.getoutput("cal"))
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("chess" in query
        or "gnome chess" in query):
            if sys_type == "Linux":
                spout = sp.getstatusoutput("gnome-chess")
                if spout[0] == 0:
                    speak("Chess Game Closed")
                else:
                    speak("Chess Game Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("todo" in query or "to-do" in query or "to do" in query or "gnome todo" in query):
            if sys_type == "Linux":
                spout = sp.getstatusoutput("gnome-todo")
                if spout[0] == 0:
                    speak("To Do Closed")
                else:
                    speak("To Do Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("vlc" in query
        or "video" in query or "audio" in query or "media" in query or "player" in query):
            if sys_type == "Linux":
                spout = sp.getstatusoutput("vlc")
                if spout[0] == 0:
                    speak("VLC Media Player Closed")
                else:
                    speak("VLC Media Player Not Found")
            elif sys_type == "Windows":
                spout = sp.getstatusoutput("start vlc:")
                if spout[0] == 0:
                    speak("VLC Media Player Closed")
                else:
                    speak("VLC Media Player Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("gimp" in query
        or "image" in query or "photo" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("start gimp")
                if spout[0] == 0:
                    speak("Gimp Closed")
                else:
                    speak("Gimp Not Found")
            elif sys_type == "Linux":
                spout = sp.getstatusoutput("gimp")
                if spout[0] == 0:
                    speak("Gimp Closed")
                else:
                    speak("Gimp Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("visual studio code"
        in query or "code" in query or "visual code" in query):
            spout = sp.getstatusoutput("code")
            if spout[0] == 0:
                speak("Visual Studio Closed")
            else:
                speak("Visual Studio Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("blender" in query or "video" in query):
            spout = sp.getstatusoutput("blender")
            if spout[0] == 0:
                speak("Blender Closed")
            else:
                speak("Blender Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("gedit" in query or "editor" in query):
            if sys_type == "Linux":
                spout = sp.getstatusoutput("gedit")
                if spout[0] == 0:
                    speak("Gedit Closed")
                else:
                    speak("Gedit Not Found")
            elif sys_type == "Windows":
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("notepad" in query or "note pad" in query or "editor" in query):
            if sys_type == "Windows":
                spout = sp.getstatusoutput("gedit")
                if spout[0] == 0:
                    speak("Notepad Closed")
                else:
                    speak("Notepad Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****")
                speak("This Feature Is Not Supported")
        elif "exit" == query or "quit" == query or "close" == query or "terminate" == query:
            print("\n")
            print("-" * 39)
            print("**** Thanks For Using My Assistant ****")
            print("-" * 39)
            print()
            speak("Thanks For Using My Assistant")
            break
        else:
            print("\n**** This Feature Is Not Supported ****")
            speak("This Feature Is Not Supported")