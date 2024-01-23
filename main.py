from functions_ import *

if __name__ == "__main__":
    print('app started ')
    speak("Hello, I am your AI assistant. How can I assist you today?")

    while True:
        command = listen()

        if command:
            if "open file explorer" in command:
                open_file_explorer()
            elif "close file explorer" in command:
                close_file_explorer()
            elif "open paint" in command:
                open_paint()
            elif "close paint" in command:
                close_paint()
            elif "open browser" in command:
                open_browser()
            elif "close browser" in command:
                close_browser()
            elif "search in xyz.com" in command:
                search_in_xyz()
            elif "open youtube" in command:
                open_youtube()
            elif "close youtube" in command:
                close_youtube()
            elif "search in youtube" in command:
                query = command.replace("search in youtube", "").strip()
                search_in_youtube(query)
            elif "increase volume" in command:
                increase_volume()
            elif "decrease volume" in command:
                decrease_volume()
            elif "increase brightness" in command:
                increase_brightness()
            elif "decrease brightness" in command:
                decrease_brightness()
            elif "click the file or folder" in command:
                click_file_or_folder()
            elif "close the file or folder" in command:
                close_file_or_folder()
            elif "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command. Can you please repeat?")
