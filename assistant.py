import os
import platform
import sys

import pyttsx3


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print("*" * 39)
    print("******* Welcome To Tools Opener *******")
    print("*" * 39)
    print()
    print("**** For Windows And Linux OS Only ****")
    print("\n")
    print("* To exit press exit or quit or close *\n")
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 50)
    speak("Welcome To Tools Opener")
    # Supported Apps ::
    # "Chrome Browser", "Firefox Browser", "Gedit Text Editor", "Notepad Text Editor", "Visual Studio Code",
    # "VLC Media Player", "Windows Media Player", "Calculator", "Calender", "Discord", "Chess", "To Do", "Gimp",
    # "Blender"

    # Check OS Type
    sys_type = platform.system()

    if sys_type != "Linux" and sys_type != "Windows":
        print("****** This System Not Supported ******")
        sys.exit("Closing Tools Opener")

    while True:
        speak("What can i do for you")
        query = input("\nWhat can i do for you ? ").lower()
        print("\nYour Query :: ", query)
        if "don't" in query or "do not" in query or "not" in query or "never" in query or "not do" in query \
                or "must not" in query or "nope" in query:
            continue
        if ("open" in query or "run" in query or "execute" in query) and ("chrome" in query or "browser" in query):
            speak("Opening Chrome Browser")
            if sys_type == "Windows":
                os.system("start chrome")
            elif sys_type == "Linux":
                os.system("google-chrome")
        elif ("open" in query or "run" in query or "execute" in query) and ("firefox" in query or "browser" in query):
            speak("Opening Firefox Browser")
            if sys_type == "Windows":
                os.system("start firefox")
            elif sys_type == "Linux":
                os.system("firefox")
        elif ("open" in query or "run" in query or "execute" in query) and ("discord" in query):
            speak("Opening Discord")
            if sys_type == "Windows":
                os.system("start discord")
            elif sys_type == "Linux":
                os.system("discord")
        elif ("open" in query or "run" in query or "execute" in query) and ("windows media player" in query):
            speak("Opening Windows Media Player")
            if sys_type == "Windows":
                os.system("start wmplayer")
            else:
                speak("This Feature Is Not Supported")
                print("\n**** This Feature Is Not Supported ****\n")
        elif ("open" in query or "run" in query or "execute" in query) and ("calculator" in query):
            speak("Opening Calculator")
            if sys_type == "Windows":
                os.system("start calculator:")
            elif sys_type == "Linux":
                os.system("gnome-calculator")
        elif ("open" in query or "run" in query or "execute" in query) and "calendar" in query:
            speak("Opening Calendar")
            if sys_type == "Windows":
                os.system("start calendar:")
            elif sys_type == "Linux":
                os.system("gnome-calendar")
        elif ("open" in query or "run" in query or "execute" in query) and ("chess" in query or "gnome chess" in query):
            speak("Opening Chess Game")
            if sys_type == "Linux":
                os.system("gnome-chess")
            else:
                speak("This Feature Is Not Supported")
                print("\n**** This Feature Is Not Supported ****\n")
        elif ("open" in query or "run" in query or "execute" in query) and ("todo" in query or "gnome todo" in query):
            speak("Opening Todo")
            if sys_type == "Linux":
                os.system("gnome-todo")
            else:
                speak("This Feature Is Not Supported")
                print("\n**** This Feature Is Not Supported ****\n")
        elif ("open" in query or "run" in query or "execute" in query) and ("vlc" in query or "video" in query
                                                                            or "audio" in query or
                                                                            "media" in query or
                                                                            "player" in query):
            speak("Opening VLC Media Player")
            if sys_type == "Linux":
                os.system("vlc")
            elif sys_type == "Windows":
                os.system("start vlc:")
        elif ("open" in query or "run" in query or "execute" in query) and ("gimp" in query or "image" in query or
                                                                            "photo" in query) and "editor" in query:
            speak("Opening Gimp")
            if sys_type == "Windows":
                os.system("start gimp")
            elif sys_type == "Linux":
                os.system("gimp")
        elif ("open" in query or "run" in query or "execute" in query) and ("blender" in query or "video" in query
                                                                            or "editor" in query):
            speak("Opening Blender")
            os.system("blender")
        elif ("open" in query or "run" in query or "execute" in query) and ("visual studio code" in query
                                                                            or "code" in query or "code" in query
                                                                            or "editor" in query) and \
                not ("video" in query or "image" in query or "audio" in query or "media" in query):
            speak("Opening Visual Studio Code")
            os.system("code")
        elif ("open" in query or "run" in query or "execute" in query) and ("gedit" in query or "editor" in query) and \
                not ("video" in query or "image" in query or "audio" in query or "media" in query):
            speak("Opening Gedit")
            if sys_type == "Linux":
                os.system("gedit")
            else:
                speak("This Feature Is Not Supported")
                print("\n**** This Feature Is Not Supported ****\n")
        elif ("open" in query or "run" in query or "execute" in query) and ("notepad" in query or "editor" in query) \
                and not ("video" in query or "image" in query or "audio" in query or "media" in query):
            speak("Opening Notepad")
            os.system("notepad")
            if sys_type == "Windows":
                os.system("notepad")
            else:
                speak("This Feature Is Not Supported")
                print("\n**** This Feature Is Not Supported ****\n")
        elif "exit" in query or "quit" in query or "close" in query or "terminate" in query:
            print("\n")
            speak("Thanks For Using Tools Opener")
            print("*" * 39)
            print("**** Thanks For Using Tools Opener ****")
            print("*" * 39)
            break
        else:
            speak("This Feature Is Not Supported")
            print("\n**** This Feature Is Not Supported ****\n")
