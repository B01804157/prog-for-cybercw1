from datetime import datetime

#Store correct login
correct_username = "admin123"
correct_password = "admin123!"

#Set the IP address
ip_address = "192.168.1.25"

#Set the first event ID
event_id = 3971

#Check whether the user has authenticated
authenticated = False

#Keep asking for login until it is successful
while not authenticated:

    #Ask the user for their login details
    username = input("Welcome! Please enter your username: ")
    password = input("Please enter your password: ")

    #Get the current date and time
    timestamp = datetime.now()

    #Check the username and password are correct
    if username == correct_username and password == correct_password:
        event = "Successful login"
        authenticated = True
        print("Login successful!")

    else:
        event = "Failed login"
        print("Authentication failed, please try again.")

    #Display the security event log
    print("\n----- Security Event Log -----")
    print("Event ID:", event_id)
    print("Username:", username)
    print("IP Address:", ip_address)
    print("Event:", event)
    print("Timestamp:", timestamp)
    print("------------------------------")

    #Increase the event ID for the next attempt
    event_id += 1




