#Import security tools module
import security_tools

#Ask the user to enter a password and IP address
password = input("Enter a password: ")
ip = input("Enter an IP address: ")

#Check if the password is valid, if it is not then return appropriate message 
if security_tools.validate_password(password):
    print("Password is valid")
else:
    print("Password is not strong enough")
    print("Suggested strong password:", security_tools.generate_password())

#Check if the IP address is valid, if it is not return the appropriate message 
if security_tools.validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")
