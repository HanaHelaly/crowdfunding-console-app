import inputs as ip
import time
from filehandler import save_user
def login():
    ask=True
    count=0
    while ask:
        email = input("Email:")
        password = input("Password:")

        with open('users.txt', 'r') as users_data:
            user_list = users_data.readlines()

        for user in user_list:
            u = user.strip().split(":")
            if email == u[4]:
                if password == u[5]:
                    ask = False
                    return u
                else:
                    if count == 1:
                        print("you've entered wrong password many times")
                        ans=input("Change your password? Y/N")
                        if ans.lower()=='y':
                            password_chg(u[0])
                        ask=False
                        break
                    count += 1
                    print("the password you've entered maybe incorrect")
                    ask = True
                    break
            else:
                ask = True

        if ask:
            print("We couldn't find an account that matches what you entered")


def password_chg(user_id):
    ask = True
    password = ip.set_password('Enter new password')
    while ask:
        match_password = input("Enter new password again")
        if password == match_password:
            print("Password has been set successfully")
            ask = False
        else:
            print("Not matching, please try again")
            ans = input("Do you want to quit and start over?y/n")
            if ans.lower() == 'y':
                break
    try:
        with open('users.txt','r') as users_f:
            contents = users_f.readlines()
        for i, content in enumerate(contents):
            user_data = content.strip().split(':')
            if int(user_data[0]) == int(user_id):
                user_data[5] = password+'\n'
                contents[i] = ':'.join(user_data)
    except FileNotFoundError:
        print("Error file was not found.")
    try:
        with open('users.txt', 'w') as users_f:
            users_f.writelines(contents)
    except FileNotFoundError:
        print("Error file was not found.")
