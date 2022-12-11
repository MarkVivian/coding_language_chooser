class LanguageClass:
    def __init__(self):
        self.state = True
        content = open("coding_languages.txt", "r")
        # the readlines will output code in the form of a list []
        self.code = content.readlines()

    # deals with the counter of how many times the user wants to change the code list.
    @staticmethod
    def number_checker():
        state = True
        while state:
            value = input("how many languages do you wish to change: \n")
            if value.isdigit():
                value = int(value)
                if value > 0:
                    return value
                else:
                    print("not possible")
            else:
                print("invalid option")

    # deals with the changing of the languages
    def language_changer(self):
        user = input("what do you wish to do: \n 1) add \n 2) remove \n")
        if user.isdigit():
            user = int(user)
            if user == 1:
                control = input("what do you wish to add \t")
                if control not in self.code:
                    self.code.append(f"{control} \n")
                    print(f"{control} has been added")
                    self.writer(self.code)
                    self.state = False
                else:
                    print(f"{control} already exists")

            elif user == 2:
                control = input("what do you wish to remove \t")
                if control in self.code:
                    self.code.remove(control)
                    print(f"{control} has been removed")
                    print(self.code)
                    self.state = False
                    self.writer(self.code)
                else:
                    print(f"{control} doesn't exist")
            else:
                print("i don't understand")
        else:
            print("invalid option")

    @staticmethod
    def writer(content):
        file = open("coding_languages.txt", "w")
        file.writelines(content)

    # structure all the functions
    def language(self):
        print(self.code)
        while self.state:
            number = self.number_checker()
            while number > 0:
                self.language_changer()
                number = number - 1


'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''
