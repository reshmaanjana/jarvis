import pyttsx3
import pyautogui
import webbrowser
import os
import time
import speech_recognition as sr

def speak(text):
    
    engine = pyttsx3.init()
    
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen()
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def open_file_explorer():
    speak("Opening File Explorer")
    os.system("explorer")

def close_file_explorer():
    speak("Closing File Explorer")
    pyautogui.hotkey("alt", "f4")

def open_paint():
    speak("Opening Paint")
    os.system("mspaint")

def close_paint():
    speak("Closing Paint")
    # Assuming Paint is open, press Alt + F4 to close
    pyautogui.hotkey("alt", "f4")

def open_browser():
    speak("Opening Browser")
    webbrowser.open("http://www.google.com")

def close_browser():
    speak("Closing Browser")
    pyautogui.hotkey("ctrl", "w")

def search_in_xyz():
    speak("Searching in XYZ.com")
    webbrowser.open("https://www.xyz.com")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def close_youtube():
    speak("Closing YouTube")
    pyautogui.hotkey("ctrl", "w")

def search_in_youtube(query):
    speak(f"Searching for {query} on YouTube")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def increase_volume():
    speak("Increasing volume")
    # Add code to increase system volume

def decrease_volume():
    speak("Decreasing volume")
    # Add code to decrease system volume

def increase_brightness():
    speak("Increasing brightness")
    # Add code to increase screen brightness

def decrease_brightness():
    speak("Decreasing brightness")
    # Add code to decrease screen brightness

def click_file_or_folder():
    speak("Clicking the file or folder")
    # Add code to simulate a click on the file or folder

def close_file_or_folder():
    speak("Closing the file or folder")
    # Add code to close the file or folder
