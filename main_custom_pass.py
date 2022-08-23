from random import shuffle
from secrets import choice
import string

def create_custom_pass(allowedchar, len_of_char):

    password_list = []

    if allowedchar[0] == 1: # adding lowercase letters
        for _ in range(len_of_char[0]):
            password_list.append(choice(string.ascii_lowercase))

    if allowedchar[1] == 1: # adding uppercase letters
        for _ in range(len_of_char[1]):
            password_list.append(choice(string.ascii_uppercase))

    if allowedchar[2] == 1: # adding digits
        for _ in range(len_of_char[2]):
            password_list.append(choice(string.digits))

    if allowedchar[3] == 1: # adding special characters
        for _ in range(len_of_char[3]):
            password_list.append(choice(string.punctuation))

    shuffle(password_list)
    password = ""
    password = ''.join(str(e) for e in password_list) #converting list into string
    return password

# live calculating the length of custom_pass as per user selection
def length_custom_pass (len_of_char, allowedchar):

    total_length = 0
    if allowedchar[0] == 1:
        total_length += len_of_char[0]

    if allowedchar[1] == 1:
        total_length += len_of_char[1]

    if allowedchar[2] == 1:
        total_length += len_of_char[2]

    if allowedchar[3] == 1:
        total_length += len_of_char[3]
    return total_length

