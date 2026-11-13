#Import modules needed to generate the random password
import random

#Function to check whether a password meets the security requirements
def validate_password(password):

    #Check that the password contains at least 8 characters
    if len(password) < 8:
        return False

    #Set variables for the different character types
    has_letter = False
    has_digit = False
    has_symbol = False

    #Check each character in the password
    for character in password:

        #Check whether the character is a letter
        if character.isalpha():
            has_letter = True

        #Check whether the character is a number
        elif character.isdigit():
            has_digit = True

        #If it is nnot a letter or number then it is a symbol
        else:
            has_symbol = True

    #Check that the password contains all 3 charcater types
    if has_letter and has_digit and has_symbol:
        return True
    else:
        return False


#Function to check whether the IP address is valid
def validate_ip(ip):

    #Remove any spaces from the beginning and end of the input
    ip = ip.strip()

    #Split the IP address into separate parts using the dots
    parts = ip.split(".")

    #Check that the IP address contains exactly four parts
    if len(parts) != 4:
        return False

    #Check each part of the IP address
    for part in parts:

        #Check that each part contains numbers only
        if not part.isdigit():
            return False

        #Convert the part from a string into an integer
        number = int(part)

        #Check that the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    #Return True if all parts of the IP address are valid
    return True

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*"


#Function to generate a random strong password
#Function to generate a random strong password
def generate_password():

    #Choose a random password length between 10 and 16 characters
    length = random.randint(10, 16)

    #Create an empty list where the password characters will be stored
    password = []

    #Add at least one uppercase letter
    password.append(random.choice(uppercase))

    #Add at least one lowercase letter
    password.append(random.choice(lowercase))

    #Add at least one digit
    password.append(random.choice(digits))

    #Add at least one symbol
    password.append(random.choice(symbols))

    #Add random characters until the correct length is met
    while len(password) < length:
        characters = uppercase + lowercase + digits + symbols
        password.append(random.choice(characters))

    #Shuffle the characters to make the password less guessable
    random.shuffle(password)

    #Join the characters together to create a full password string
    password = "".join(password)

    #Return the finished randomly generated password
    return password
