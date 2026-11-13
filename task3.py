#Function to check whether an IP address is valid
def validate_ip(ip):

    #Remove any spaces from the beginning and end
    ip = ip.strip()

    #Check that the inputted IP address contains dots
    if "." not in ip:
        return False

    #Check that the inputted IP address contains exactly three dots
    if ip.count(".") != 3:
        return False

    #Split the IP address into four separate parts using the dots
    parts = ip.split(".")

    #Check that there are exactly four parts
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

    #Return True if all checks have passed
    return True

#Ask the user to enter an IP address
ip = input("Enter an IP address: ")

#Call the function and display the appropriate message
if validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")

