def twoFactorLogin():
    while True:
        password1 = input("Enter your password: ")
        if password1 == "correct_password":  
            password2 = float(input("Enter your second password : "))
            if password2 == 123.45:  
                print("Access granted! Congratulations!")
                break
            else:
                print("Second password incorrect, try again.")
        else:
            print("First password incorrect, try again.")

twoFactorLogin()
