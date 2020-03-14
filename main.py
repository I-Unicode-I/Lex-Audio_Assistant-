from gtts import gTTS
import pyaudio
import speech_recognition as sr
import os
import webbrowser
import smtplib


def talk_to_me(audio):
    """ Definition for a program talking to person """
    print(audio)

    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


# Listens for commands
def my_command():
    """ Definition for a program that listens to a person """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = my_command()

    return command


# if statements for executing commands
def assistant(command):
    """ Definition for a program that execute a command """

    if 'open reddit python' in command:
        chrome_path = "/Users/AI-Init/AppData/Local/Google/Chrome SxS/Application/chrome.exe"
        url = 'https://www.reddit.com/r/python'
        webbrowser.open(url)

    if 'what\'s up' in command:
        talk_to_me('WAsssss uuuuuuup')

    if 'email' in command:
        talk_to_me('Who is the recipient')
        recipient = my_command()

        if 'andrew' in recipient:
            talk_to_me('What should I say')
            content = my_command()

            # init email SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # login to mail
            mail.login('greal446@gmail.com', 'mInD_V-linkW559')

            # send message
            mail.sendmail('NIKITA', 'greal446@gmail.com', content)

            # close connection
            mail.close()

            talk_to_me('Email sent')


def main():
    """ Main code where run definition 'talk_to_me' and loop for definition 'assistant' """
    talk_to_me('I am ready your command')

    # loop command
    while True:
        assistant(my_command())


if __name__ == '__main__':
    main()
