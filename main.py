import language_file
import pyttsx3
import random
import time
from datetime import datetime


class ChoiceMade:
    def __init__(self):
        # gets the code from the language_file
        self.script()
        self.code = language_file.LanguageClass().code
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

    @staticmethod
    def script():
        user = input("do you wish to change the values: ")
        if user.lower() == "yes":
            language_file.LanguageClass().language()
        else:
            return

    def random_lang(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        file = []
        while True:
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            second = now.second
            print(f"{hour}:{minute}:{second}")
            time.sleep(1)
            if hour == 10:
                decode = random.choice(numbers)
                numbers.remove(decode)
                file.append(decode)
                value = self.code[decode]
                self.speech_week(value)
                time.sleep(3600)
                if len(numbers) == 0:
                    self.speech_repeat()
                    numbers = file


if __name__ == '__main__':
    choice_taken = ChoiceMade()
