import os
import platform
import sys

import pyttsx3


def speak(text):
    pyttsx3.speak(text)
    engine.runAndWait()


if __name__ == '__main__':

    print("*" * 39)
    print("******* Welcome To Tools Opener *******")
    print("*" * 39)
    print()
    print("****** Developed By Vishal Yadav ******")
    print()
    print("**** For Windows And Linux OS Only ****")
    print("\n")
    print("To exit app press exit or quit or close\n")
    print()
    print("To exit the opened tool press Ctrl + C \n")

    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    engine.setProperty('rate', engine.getProperty('rate') + 50)
    
    # Welcome Message
    speak("Welcome To Tools Opener")

    # Supported Apps(14) ::

    # Windows :: "Chrome Browser", "Firefox Browser", "Notepad Text Editor", "Visual Studio Code", "VLC Media Player",
    #            "Windows Media Player", "Calculator", "Calender", "Discord", "Gimp", "Blender"

    # Linux :: "Chrome Browser", "Firefox Browser", "Gedit Text Editor", "Visual Studio Code", "VLC Media Player",
    #          "Calculator", "Calendar", "Discord", "Chess", "To Do", "Gimp", "Blender"

    # Check OS Type
    sys_type = platform.system()

    # Validate For Windows And Linux Only
    if sys_type != "Linux" and sys_type != "Windows":
        print("****** This System Not Supported ******")
        sys.exit("Closing Tools Opener")

    while True:

        # Ask For Query
        speak("What can i do for you")

        # Taking Query From User
        query = input("\nWhat can i do for you ? ").lower()

        # Printing User Query
        print("\nYour Query :: ", query)

        if "don't" in query or "do not" in query or "not" in query or "never" in query or "not do" in query \
                or "must not" in query or "nope" in query:
            continue
        if ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("chrome" in query
        or "browser" in query):
            speak("Opening Chrome Browser")
            if sys_type == "Windows":
                if os.system("start chrome") != 0:
                    speak("Chrome Not Found")
            elif sys_type == "Linux":
                if os.system("google-chrome") != 0:
                    speak("Chrome Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("firefox" in query
        or "browser" in query):
            speak("Opening Firefox Browser")
            if sys_type == "Windows":
                if os.system("start firefox") != 0:
                    speak("Firefox Not Found")
            elif sys_type == "Linux":
                if os.system("firefox") != 0:
                    speak("Firefox Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("discord" in query):
            speak("Opening Discord")
            if sys_type == "Windows":
                if os.system("start discord") != 0:
                    speak("Discord Not Found")
            elif sys_type == "Linux":
                if os.system("discord") != 0:
                    speak("Discord Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("windows media player" in query):
            speak("Opening Windows Media Player")
            if sys_type == "Windows":
                if os.system("start wmplayer") != 0:
                    speak("Windows Media Player Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("calculator" in query):
            speak("Opening Calculator")
            if sys_type == "Windows":
                if os.system("start calculator:") != 0:
                    speak("Calculator Not Found")
            elif sys_type == "Linux":
                if os.system("gnome-calculator") != 0:
                    speak("Calculator Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and "calendar" in query:
            speak("Opening Calendar")
            if sys_type == "Windows":
                if os.system("start calendar:") != 0:
                    speak("Calendar Not Found")
            elif sys_type == "Linux":
                if os.system("gnome-calendar") != 0:
                    speak("Calendar Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("chess" in query
        or "gnome chess" in query):
            speak("Opening Chess Game")
            if sys_type == "Linux":
                if os.system("gnome-chess") != 0:
                    speak("Chess Game Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("todo" in query
        or "to do" in query or "gnome todo" in query):
            speak("Opening To Do")
            if sys_type == "Linux":
                if os.system("gnome-todo") != 0:
                    speak("Todo Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("vlc" in query
        or "video" in query or "audio" in query or "media" in query or "player" in query):
            speak("Opening VLC Media Player")
            if sys_type == "Linux":
                if os.system("vlc") != 0:
                    speak("VLC Media Player Not Found")
            elif sys_type == "Windows":
                if os.system("start vlc:") != 0:
                    speak("VLC Media Player Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("gimp" in query
        or "image" in query or "photo" in query):
            speak("Opening Gimp")
            if sys_type == "Windows":
                if os.system("start gimp") != 0:
                    speak("Gimp Not Found")
            elif sys_type == "Linux":
                if os.system("gimp") != 0:
                    speak("Gimp Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in query) and ("visual studio code"
        in query or "code" in query or "code" in query or "editor" in query) and not ("video" in query or "image"
        in query or "audio" in query or "media" in query or "gedit" in query):
            speak("Opening Visual Studio Code")
            if os.system("code") != 0:
                speak("Visual Studio Code Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("blender" in query or "video" in query):
            speak("Opening Blender")
            if os.system("blender") != 0:
                speak("Blender Not Found")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("gedit" in query or "editor" in query) and not ("video" in query or "image" in query or "audio" in query or "media" in query):
            speak("Opening Gedit")
            if sys_type == "Linux":
                if os.system("gedit") != 0:
                    speak("Gedit Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif ("open" in query or "run" in query or "execute" in query or "launch" in  query) and ("notepad" in query or "editor" in query) and not ("video" in query or "image" in query or "audio" in query or "media" in query):
            speak("Opening Notepad")
            if sys_type == "Windows":
                if os.system("notepad") != 0:
                    speak("Notepad Not Found")
            else:
                print("\n**** This Feature Is Not Supported ****\n")
                speak("This Feature Is Not Supported")
        elif "exit" in query or "quit" in query or "close" in query or "terminate" in query:
            print("\n")
            print("*" * 39)
            print("**** Thanks For Using Tools Opener ****")
            print("*" * 39)
            speak("Thanks For Using Tools Opener")
            break
        else:
            print("\n**** This Feature Is Not Supported ****\n")
            speak("This Feature Is Not Supported")