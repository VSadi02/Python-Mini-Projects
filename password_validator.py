password = input("Enter password: ")
confirm_password = input("Confirm password: ")

if password == confirm_password:
    if len(password) >= 8:
        print("Password matched successfully!")
        print("Valid Password")
    else:
        print("Password matched, but it should contain at least 8 characters.")
else:
    print("Passwords do not match!")