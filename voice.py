import speech_recognition as sr
import pyttsx3
import os
import pyautogui

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech speed

SECURITY_KEYWORD = "hey akhil"  # Change this to your preferred wake word

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the security keyword...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Could not connect to the service.")
        return ""

def open_app(app_name):
    if "chrome" in app_name:
        os.system("start chrome")  
    elif "notepad" in app_name:
        os.system("notepad")  
    elif "whatsapp" in app_name:
        os.system("start whatsapp")
    elif "youtube" in app_name:
        os.system("start https://www.youtube.com")
    else:
        speak("App not recognized")

def control_settings(command):
    if "wifi" in command:
        os.system("netsh interface set interface Wi-Fi disable")  
        speak("Turning off Wi-Fi")
    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        speak("Screenshot taken")
    elif "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")
    else:
        speak("Command not recognized")

def main():
    speak("Hello! Say the security keyword to activate me.")
    
    while True:
        keyword = recognize_speech()
        if SECURITY_KEYWORD in keyword:
            speak("Access granted. How can I help you?")
            
            while True:
                command = recognize_speech()
                
                if "open" in command:
                    open_app(command.replace("open ", ""))
                elif "turn off" in command or "volume up" in command:
                    control_settings(command)
                elif "exit" in command or "stop" in command:
                    speak("Goodbye!")
                    return
                else:
                    speak("I didn't understand that command.")
        else:
            speak("Unauthorized access. Please say the correct keyword.")

if __name__ == "__main__":
    main()
