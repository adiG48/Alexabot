import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PySimpleGUI as sg
import sender as b

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

a = True


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('alexa activated!!')
talk('how can i help you?')


def take_command():
    while a:
        try:
            with sr.Microphone() as source:
                listener.energy_threshold = 10000
                listener.adjust_for_ambient_noise(source, 1.2)
                print('Listening..')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
                break
        except UnboundLocalError:
            print('going to stop')
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'sport' in command:
        talk('My favourite sport is cricket')
    elif 'created' in command:
        talk('I was created by adithyaa')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'email' in command:
        def get_info():
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                print(info)
                return info.lower()

        fr = "adithyaaaibot@gmail.com"
        talk('To Whom you want to send email')
        name = get_info()
        receiver = b.email_list[name]
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the message in your email')
        message = get_info()

        def send():
            b.send_email(receiver, subject, message)
            talk('Hey lazy Your email is sent')

        sg.change_look_and_feel('Dark Blue 3')
        layout = [[sg.Text('Send an Email', font='Default 18')],
                  [sg.T('From:', size=(8, 1)), sg.Input(fr)],
                  [sg.T('To:', size=(8, 1)), sg.Input(receiver)],
                  [sg.T('Subject:', size=(8, 1)), sg.Input(subject)],
                  [sg.T('message', size=(8, 2)), sg.Input(message)],
                  [sg.Button('Send'), sg.Button('Exit')]]
        window = sg.Window('Send An Email', layout)
        event, values = window.read()
        if event == 'Send':
            sg.popup_quick_message('Sending Your Message.... This Will Take A Moment', background_color='red')
            send()
            window.close()
        if event in (None, 'Exit'):
            window.close()
    elif 'stop' in command:
        global a
        talk('alexa deactivated')
        a = False
        return a
    else:
        talk('Sorry I did not catch that')


while True:
    run_alexa()
