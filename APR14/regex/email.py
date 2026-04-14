import re
def home():
    pattern=r'^[a-zA-Z0-9+%_]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mail=input("Enter your email: ")
    if re.fullmatch(pattern,mail):
        print("Valid email")
    else:
        print("Invalid email")
home()
