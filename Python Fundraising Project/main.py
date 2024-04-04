import re
def getname(message="Please,Enter your name "):
    while True:
        name = input(message)
        if name.isalpha():
            return name
        else:
            print("Invalid")

def email(message="Please,Enter your e-mail"):
    pattern = r'^[^\d]+\w+@\w+\.com'
    while True:
        mail = input(message)
        if bool(re.search(pattern, mail)):
            break
        else:
            print("Invalid")

    return mail

