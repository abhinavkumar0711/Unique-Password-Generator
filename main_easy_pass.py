from secrets import randbelow, choice
from random import shuffle
import string

def create_easy_pass(pass_length, allowedchar):

    # Opening the file and storing all the lines as a list
    words = open("words.txt","r").read().split("\n")
    shuffle(words)

    # letter_len_in_password calculates the no. of letters that has to be there in password
    letter_len_in_password = pass_length
    if(allowedchar[2] == 1):
        letter_len_in_password -= 3

    if(allowedchar[3] == 1):
        letter_len_in_password -= 1

    password=""
    if allowedchar[0] == 1 or allowedchar[1] == 1: # if atleast lowercase or uppercase letter is selected

        while pass_length > len(password):

            if allowedchar[0] == 1 and allowedchar[1] == 1: # if both lower and upper are selected
                password+=choice(words).lower().capitalize() # Adds random words from text file to password

            elif allowedchar[0] == 1:   # if only lowercase selected
                password+=choice(words).lower()

            elif allowedchar[1] == 1:   # if only uppercase selected
                password+=choice(words).upper()
        password =password[:letter_len_in_password]

    # loop for adding digits and symbols to the password
    if allowedchar[2] == 1 or allowedchar[3] == 1: # if atleast one of digit or symbol is selected

        while pass_length > len(password):

            if allowedchar[3] == 1: # if special characters is selected
                for _ in range(1):
                    password+=choice(string.punctuation)

            if allowedchar[2] == 1: # if digits is selected
                for _ in range(3):
                    password+=str(randbelow(10)) # Adds random numbers to the password below 10

    password = password[:pass_length]
    return password

