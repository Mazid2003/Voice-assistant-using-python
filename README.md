# Voice-assistant-using-python

**📌 Project Overview**

This project is a voice-controlled assistant that runs on a laptop and performs various tasks based on user voice commands. The assistant can:

Authenticate the user using a security voice code before activating.

Recognize and execute voice commands to control system applications.

Provide responses using text-to-speech (TTS) for better interaction.

Execute system-level commands like opening applications, searching the web, or shutting down.

Include a shutdown command to stop its operation when required.

**🔧 Technologies Used**

Python – Main programming language

SpeechRecognition – To capture and process voice commands

pyttsx3 – To convert text into speech

pyaudio – For microphone access

PyAutoGUI – To control system applications

NLTK / OpenAI API – (Optional) for Natural Language Processing


**🚀 Features Implemented**

✅ Security Voice Code – Unlocks only when the correct voice code is spoken

✅ Voice Command Execution – Open apps, search Google, and more

✅ Text-to-Speech (TTS) – Speaks responses for better interaction

✅ System Control – Volume control, shutdown, restart

✅ Stop Command – Stops assistant when needed

**🏗 How It Works**

**Voice Activation:**

The assistant starts in a locked state and waits for the correct security voice code.

If the user speaks the correct code, the assistant activates.

**Command Recognition:**

The program listens to the user's voice, converts it to text, and processes the command.

**Task Execution:**

Based on recognized commands, the assistant performs actions like:

Opening applications (Chrome, Notepad, etc.)

Searching Google or Wikipedia

Sending messages or emails

Controlling system volume

Locking or shutting down the computer

**Stop Command:**

A specific voice command (e.g., "exit assistant") will stop the assistant.

**🚀 How to Run the Project**

Clone the repository

git clone https://github.com/Mazid2003/Voice-Assistant.git
cd Voice-Assistant

Install dependencies

pip install -r requirements.txt

Run the assistant

python main.py

🎯 Next Steps & Improvements

Enhance NLP processing to better understand user commands.

Add a GUI interface for better user experience.

Convert it into a Mobile App using Kivy or Flutter.

🎬 Final Thoughts

This Voice Assistant is a smart system that allows users to control their laptop hands-free. With future improvements, it can become more interactive and even be deployed as a mobile app. 🚀
