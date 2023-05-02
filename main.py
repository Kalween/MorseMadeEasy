#import colorama for coloring the logo.
from colorama import Fore, Style, init

#True function for loop
its_on = True

#dictionary for translation
morse_code_dict = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',  'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}

#logo function
def print_logo():
    init(autoreset=True)

    text = "PYTHON MORSE MADE EASY"
    colors = [Fore.RED,Fore.YELLOW, Fore.WHITE]

    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end="")

    print(Style.RESET_ALL)




#generates input to list and then translates the string to morse code
def generator(string_input: str) -> str:
    characters = [char.upper() for char in list(string_input)]
    morse_string = [morse_code_dict.get(char,"/") for char in characters]
    return " ".join(morse_string)


#main function
def main_loop():
    print_logo()
    print("Welcome to the string to morse translator.")

    while its_on:
        string_input = input("What do you want translated into morse code? to stop type (q)uit : ")
        if string_input == 'q' or string_input == 'quit':
            break
        print(generator(string_input))


if __name__ == "__main__":
    main_loop()
