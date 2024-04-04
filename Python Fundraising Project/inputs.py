import re
from getpass import getpass
from datetime import datetime

def get_name(message="Please,Enter your name "):
    while True:
        name = input(message)
        if name.isalpha():
            return name
        else:
            print("Invalid")


def get_mail(message="Enter your e-mail"):

    pattern = r'^[^\d]+\w+@\w+\.com'
    while True:
        mail = input(message)
        if bool(re.search(pattern, mail)):
            break
        else:
            print("Invalid")
    return mail


def check_password(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if len(password) < 8:
        return False
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special_char = any(c in special_characters for c in password)
    if ' ' in password:
        return False
    if ':' in password:
        return False

    return has_digit and has_upper and has_special_char


def set_password(message="Enter password"):
    while True:
        password = input(message)
        valid = check_password(password)
        if valid:
            return password
        else:
            print("password must contain at least:1 special character,1 upper case letter,"
                  "a digit and at least 8 characters long")


def get_phone_num(message="Enter your phone number +20:"):
    pattern = r"1\d{9}"
    while True:
        phone_no = input(message)
        if phone_no.isdigit():
            if bool(re.search(pattern, phone_no)):
                return phone_no
            else:
                print("That's incorrect number")
        else:
            print("that is not a number")


def get_date(message="enter the date in format :yyyy-mm-dd"):
    while True:
        try:
            y, m, d = [int(x) for x in input(message).split('/')]
            if y not in range(2023, 2051):
                print("out of bound year ")
                continue
            elif m not in range(1, 13):
                print("out of bound month")
                continue
            elif m == 2:
                if d not in range(1, 29):
                    print("out of bound day")
                    continue
            elif d not in range(1, 31):
                print("out of bound day")
                continue
        except ValueError:
            print("Invalid date,please enter in given format")
        else:
            date = datetime(y, m, d)
            return f"{date.year}-{date.month}-{date.day}"
