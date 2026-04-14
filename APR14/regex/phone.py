import re
def home():
    phone=input("Enter your phone number: ")
    pattern=r'^[6-9]\d{9}$'
    if re.fullmatch(pattern,phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")
home()
