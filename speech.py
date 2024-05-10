import speech_recognition as sr


def transcribe_spoken_speech():
    recognizer = sr.Recognizer()

    transcriptions = []

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something into the microphone...")

        # Adjust the recognizer sensitivity to ambient noise once at the beginning
        recognizer.adjust_for_ambient_noise(source)

        try:
            while True:
                try:
                    print("Listening...")
                    audio = recognizer.listen(source)

                    # Google's web speech recognition will transcribe the audio
                    text = recognizer.recognize_google(audio)
                    print("You said: " + text)

                    transcriptions.append(text)

                except sr.RequestError:
                    print(
                        "Request Error; check your network connection.")
                except sr.UnknownValueError:
                    # Skip unintelligible speech and continue listening
                    continue
        except KeyboardInterrupt:
            # user interrupts, will stop the loop and print appended transcriptions
            print("\nStopping transcription...")
            print("\nFull Transcript:")
            print("\n".join(transcriptions))


if __name__ == "__main__":
    transcribe_audio()
