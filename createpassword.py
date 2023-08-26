#password generator

import random
import re

def Passwordchecker():
    password = input("input your password here")
    flag = 0
    while True:
	    if (len(password)<=8):
		    flag = -1
		    break
	    elif not re.search("[a-z]", password):
		    flag = -1
		    break
	    elif not re.search("[A-Z]", password):
		    flag = -1
		    break
	    elif not re.search("[0-9]", password):
		    flag = -1
		    break
	    elif not re.search("[_@$]" , password):
		    flag = -1
		    break
	    elif re.search("\s" , password):
		    flag = -1
		    break
	    else:
		    flag = 0
		    print("Valid Password")
		    break

    if flag == -1:
	    print("Not a Valid Password ")

askuser = input("do you want to check or to create a password? (check or create)")
if askuser == "create":
    easy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    hard = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '.', '<', '>', '/', '?']

    lenght = input("how long do you want your password to be?")
    newlenght = int(lenght)

    def createhardpassword():
        return ''.join(random.choice(hard)for _ in range(newlenght))  # Generates an 8-character password

    def createeasypassword():
        return ''.join(random.choice(easy)for _ in range(newlenght))  # Generates an 8-character password

    question = input("Do you want a simple password or a hard one? (simple, hard) ")
    if question == "hard":
        while True:
            password = createhardpassword()
            print("Generated password:", password)
            question1 = input("Are you satisfied? (y or n) ")
            if question1.lower() == "y":
                break
    else:
        while True:
            password1 = createeasypassword()
            print("Generated password:", password1)
            question2 = input("Are you satisfied? (y or n) ")
            if question2.lower() == "y":
                break

#! Password validator, this will ask if you want to check how secure your current password is

elif askuser == "check":
    Passwordchecker()