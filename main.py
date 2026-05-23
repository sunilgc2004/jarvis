from voice import speak, take_command
import webbrowser
import datetime
import pywhatkit
import wikipedia

speak("Hello sir, Jarvis is online")

while True:

    command = take_command()

    # Open YouTube
    if "open youtube" in command:
        speak("Opening YouTube sir")
        webbrowser.open("https://youtube.com")

    # Open Google
    elif "open google" in command:
        speak("Opening Google sir")
        webbrowser.open("https://google.com")

    # Play Song
    elif "play" in command:

        song = command.replace("play", "")

        speak("Playing " + song)

        pywhatkit.playonyt(song)

    # Time
    elif "time" in command:

        time = datetime.datetime.now().strftime('%I:%M %p')

        speak("Current time is " + time)

    # Wikipedia
    elif "who is" in command:

        person = command.replace("who is", "")

        info = wikipedia.summary(person, 2)

        speak(info)

    # Exit
    elif "stop" in command:
        speak("Goodbye sir")
        break