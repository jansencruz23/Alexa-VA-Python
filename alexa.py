import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
from AyDictionary import AyDictionary
from colorama import Fore

FEMALE_VOICE = 1

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[FEMALE_VOICE].id)
dictionary = AyDictionary()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Alexa is listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()

            if 'alexa' in command:
                return command.replace('alexa', '')
    except:
        return None


def play_song(command):
    try:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    except:
        talk('Cannot play' + command)


def get_time(_):
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)


def get_info(command):
    person = command.replace('who is', '')
    try:
        info = wikipedia.summary(person, 1)
        talk(info)
    except:
        talk('An error occurred. Try again')


def tell_joke(_):
    joke = pyjokes.get_joke()
    talk(joke)


def get_random_fact(_):
    fact = randfacts.get_fact()
    talk(fact)


def get_word_meaning(command):
    word = command.split()[0]
    response = dictionary.meaning(word)
    meaning = next(iter(response.values()))[0]
    talk(meaning)


def shutdown_alexa(_):
    talk('Alexa is turning off')
    quit()


command_functions = {
    'play': play_song,
    'time': get_time,
    'who is': get_info,
    'joke': tell_joke,
    'fact': get_random_fact,
    'trivia': get_random_fact,
    'meaning': get_word_meaning,
    'date': lambda _: talk('Sorry, I am not available'),
    'are you single': lambda _: talk('It is complicated'),
    'handsome': lambda _: talk('The most handsome man in the world is ' + Fore.BLUE + 'Jansen Cruz' + Fore.RESET),
    'shutdown': shutdown_alexa
}

while True:
    command = take_command()
    if command is None:
        talk('I beg your pardon?')
        continue

    for keyword, func in command_functions.items():
        if keyword in command:
            func(command)
            break
    else:
        shutdown_alexa('')