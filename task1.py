#Correct login details for beginning authentication before menu
correct_username = "admin123"
correct_password = "admin123!"

#Maximum number of failed login attempts
maximum_attempts = 3
failed_logins = 0
authenticated = False

#Startup 
while failed_logins < maximum_attempts:
    username = input("Welcome! Please enter your username: ")
    password = input("Now enter your password: ")

    if username == correct_username and password == correct_password:
        print("---- Authentication successful ----")
        authenticated = True
        break
    else:
        failed_logins += 1
        print("Authentication failed. Please try again.")
        print("Attempts remaining:", maximum_attempts - failed_logins)

#Freeze the account if all attempts fail
if not authenticated:
    print("Your account has been frozen for 24 hours.")

#Security menu only appears if authentication was successfull
if authenticated:
    while True:
        print("\n---- Security Tool ----")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        #Security Event Counter
        if choice == "1":
            correct_count = 0
            incorrect_count = 0

            for i in range(10):
                password_attempt = input("Enter the password: ")

                if password_attempt == correct_password:
                    correct_count += 1
                else:
                    incorrect_count += 1

            print("Correct passwords:", correct_count)
            print("Incorrect passwords:", incorrect_count)

            incorrect_percentage = (incorrect_count / 10) * 100
            print("Percentage of incorrect passwords:",
                  incorrect_percentage, "%")

            if incorrect_percentage > 50:
                print("ALERT: More than 50% of passwords were incorrect!")

        #Brute-Force Simulation
        elif choice == "2":
            brute_force_password = "brute123!"
            maximum_brute_attempts = 5
            brute_attempts = 0

            while brute_attempts < maximum_brute_attempts:
                guess = input("Enter your password guess: ")
                brute_attempts += 1

                if guess == brute_force_password:
                    print("Password successfully guessed!")
                    print("Attempts used:", brute_attempts)
                    break
                else:
                    print("Incorrect password.")

            if (brute_attempts == maximum_brute_attempts
                    and guess != brute_force_password):
                print("Maximum attempts reached. Password not guessed.")

        #Login Authentication
        elif choice == "3":
            login_username = "user123"
            login_password = "pass123!"

            failed_attempts = 0
            maximum_login_attempts = 3
            login_successful = False

            while failed_attempts < maximum_login_attempts:
                entered_username = input("Enter username: ")
                entered_password = input("Enter password: ")

                if (entered_username == login_username
                        and entered_password == login_password):
                    print("Authentication successful!")
                    login_successful = True
                    break
                else:
                    failed_attempts += 1
                    print("Authentication failed.")
                    print("Attempts remaining:",
                          maximum_login_attempts - failed_attempts)

            if not login_successful:
                print("Account is frozen for 24 hours.")

        #Exit
        elif choice == "4":
            print("Thank you for using the security tool")
            break

        #Handle invalid menu choices
        else:
            print("Invalid choice. Please select 1-4.")
