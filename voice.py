import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")
        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:

        print("I couldn't understand you.")
        return None

    except sr.RequestError:

        print("Speech recognition service is unavailable.")
        return None