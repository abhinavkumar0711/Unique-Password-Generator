from passwordmeter import test
from main_create_pass import *
from main_easy_pass import *
from main_custom_pass import *

choice = 'y'
while(choice == 'y'):

	allowedchar = []
	len_of_char = []

	pass_type = int(input("Enter,\n1. For a strong password\n2. For easy to remember password\n3. For Customized password\n"))
	pass_length = int(input("Enter the length of the password(length>6): "))
	if(pass_length < 6):
			print("Password length is invalid")
			continue
	allowedchar.append(input("want to include lower case characters?(y/n) "))
	allowedchar.append(input("want to include upper case characters?(y/n) "))
	allowedchar.append(input("want to include digits?(y/n) "))
	allowedchar.append(input("want to include special characters?(y/n) "))

	if pass_type == 1:
		create_strong_pass(pass_length, allowedchar)
	elif pass_type == 2:
		create_easy_pass(pass_length, allowedchar)
	elif pass_type == 3:
		len_of_char.append(int(input("How many lower letters? ")))
		len_of_char.append(int(input("How many upper letters? ")))
		len_of_char.append(int(input("How many digits letters? ")))
		len_of_char.append(int(input("How many special letters? ")))
		create_custom_pass(pass_length, allowedchar, len_of_char)
	else:
		print("invalid choice")
	choice = input("\nDo you want more passwords?(y/n) ")
