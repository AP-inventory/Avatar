import speech_recognition as sr

class SpeechRecognition:
    def __init__(self):
        # Initialize any required variables or resources for speech recognition
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio_file):
        # Perform speech recognition on the audio file and extract the recognized text
        try:
            with sr.AudioFile(audio_file) as source:
                audio_data = self.recognizer.record(source)
                recognized_text = self.recognizer.recognize_google(audio_data)
                return recognized_text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
              
