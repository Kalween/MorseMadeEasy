# MorseMadeEasy
Python Morse Made Easy
This is a simple program that allows you to translate a string into morse code.

Prerequisites
You will need to install the colorama library in order to run the program. You can install it using the following command:


  pip install colorama

Usage
To use the program, simply run the script in your terminal:


  python morse_translator.py
You will be prompted to enter a string that you would like to translate into morse code. The program will continue to run until you type q or quit to exit.

Code Explanation
The program uses a dictionary morse_code_dict to store the mapping between letters and their corresponding morse code representation. The generator function takes the input string and translates it into morse code using the dictionary. The main_loop function provides the main logic for the program, which is to repeatedly ask the user for a string to translate and to print the result. The print_logo function uses the colorama library to display a colorful logo at the start of the program.

Contributing
This project is open to contributions and improvements. Feel free to submit a pull request if you have any suggestions or fixes.
