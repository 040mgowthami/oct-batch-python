
import random
import datetime

import pyttsx3
import speech_recognition as sr
import wikipedia


# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

# Initialize speech recognition
recognizer = sr.Recognizer()

# Set Wikipedia language
wikipedia.set_lang("en")

# Basic jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "Why did the Python programmer wear glasses? Because they could not C!",
    "Why did the computer go to the doctor? Because it had a virus!"
]


def speak(text):
    """Speak a response and display it on the screen."""
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the microphone and return recognized text."""
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now.")
            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")
        command = recognizer.recognize_google(
            audio, language="en-IN"
        )
        print("You:", command)
        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected. Try again.")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
    except sr.RequestError:
        speak("Speech recognition is unavailable. Check your internet connection.")
    except OSError:
        speak("I cannot access your microphone. Check your microphone settings.")

    return ""


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )
    speak(f"Today's date is {current_date}")


def tell_joke():
    speak(random.choice(jokes))


def search_wikipedia(command):
    """Search Wikipedia using the words in the voice command."""
    query = command

    prefixes = [
        "search wikipedia for ",
        "search wikipedia about ",
        "wikipedia ",
        "tell me about ",
        "who is ",
        "what is ",
        "who was ",
        "what was "
    ]

    for prefix in prefixes:
        if query.startswith(prefix):
            query = query[len(prefix):]
            break

    query = query.strip()

    if not query:
        speak("Please tell me what you want to search for.")
        return

    try:
        speak(f"Searching Wikipedia for {query}")

        summary = wikipedia.summary(
            query,
            sentences=2,
            auto_suggest=True,
            redirect=True
        )
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as error:
        options = ", ".join(error.options[:5])
        speak(
            "There are multiple results. Please be more specific. "
            f"Some options are: {options}"
        )

    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find a Wikipedia page for that topic.")

    except Exception:
        speak("Sorry, I could not complete the Wikipedia search.")


def process_command(command):
    """Decide what action to perform."""
    if not command:
        return True

    if any(word in command for word in [
        "exit", "quit", "stop assistant", "goodbye"
    ]):
        speak("Goodbye! Have a nice day.")
        return False

    elif any(phrase in command for phrase in [
        "hello", "hi alexa", "hey alexa"
    ]):
        speak("Hello! How can I help you?")

    elif "your name" in command:
        speak("I am your Python desktop voice assistant.")

    elif "time" in command:
        tell_time()

    elif "date" in command or "today" in command:
        tell_date()

    elif "joke" in command or "make me laugh" in command:
        tell_joke()

    elif "help" in command or "what can you do" in command:
        speak(
            
            "I can tell the time and date, tell jokes, "
            "search Wikipedia, and answer simple greetings. "
            "Say goodbye to exit."
        )

    elif any(phrase in command for phrase in [
        "search wikipedia",
        "wikipedia",
        "tell me about",
        "who is",
        "what is",
        "who was",
        "what was"
    ]):
        search_wikipedia(command)

    else:
        speak(
            "Sorry, I do not know that command yet. "
            "Say help to hear what I can do."
        )

    return True


def main():
    speak("Hello! Your desktop assistant is ready.")
    speak("Say help to learn my commands.")

    running = True

    while running:
        command = listen()
        running = process_command(command)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant stopped.")
    finally:
        engine.stop()
