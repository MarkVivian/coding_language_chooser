import language_file
import pyttsx3
import random
import time
from datetime import datetime


class ChoiceMade:
    def __init__(self):
        # gets the code from the language_file
        self.code = language_file.LanguageClass().code
        self.code_line = language_file.LanguageClass().code_line
        engine = pyttsx3.init()
        engine.say("welcome sir")
        engine.runAndWait()
        self.script()
        self.random_lang()

    @staticmethod
    def speech_week(choice_decoded):
        print("running")
        engine = pyttsx3.init()
        engine.say(f"hello Mark, today's language is {choice_decoded}")
        engine.runAndWait()

    @staticmethod
    def speech_repeat():
        engine = pyttsx3.init()
        engine.say("lets begin again")
        engine.runAndWait()

    def script(self):
        print(f"your languages are {self.code_line}")
        user = input("do you wish to change the values: ")
        if user.lower() == "yes":
            language_file.LanguageClass().language()
        else:
            return

    def random_lang(self):
        container = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        file = []
        while True:
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            second = now.second
            print(f"{hour}:{minute}:{second}")
            time.sleep(1)
            if hour == 10:
                decode = random.choice(container)
                print(decode)
                container.remove(decode)
                file.append(decode)
                value = self.code[decode]
                self.speech_week(value)
                time.sleep(3600)
                if len(container) == 0:
                    self.speech_repeat()
                    container = file


if __name__ == '__main__':
    choice_taken = ChoiceMade()
