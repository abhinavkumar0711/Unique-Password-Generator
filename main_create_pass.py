from random import shuffle
from secrets import choice
import string

def Create_character_list(allowedchar): # list containing all the allowed characters by user

	all_character_set = []

	if allowedchar[0] == 1: # are lowercase letters allowed?
		lower_letters_list = list(string.ascii_lowercase.strip(" "))
		shuffle(lower_letters_list)
		all_character_set.extend(lower_letters_list)

	if allowedchar[1] == 1: # are uppercase letters allowed?
		upper_letters_list = list(string.ascii_uppercase.strip(" "))
		shuffle(upper_letters_list)
		all_character_set.extend(upper_letters_list)

	if allowedchar[2] == 1: # are digits allowed?
		digits_list = list(string.digits.strip(" "))
		shuffle(digits_list)
		all_character_set.extend(digits_list)
		all_character_set.extend(digits_list)

	if allowedchar[3] == 1: # are special characters allowed?
		special_char_list = list(string.punctuation.strip(" "))
		shuffle(special_char_list)
		all_character_set.extend(special_char_list)

	shuffle(all_character_set)
	return all_character_set

def create_strong_pass(pass_length, allowedchar):

	all_character_set = Create_character_list(allowedchar)
	password = ""
	for x in range(pass_length):
		password += choice(all_character_set)

	return password
