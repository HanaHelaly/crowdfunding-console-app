import inputs as ip
import time
# from getpass import getpass


def registration():
    first_name = ip.get_name("Enter your first name")
    last_name = ip.get_name("Enter your last name")
    phone_no = ip.get_phone_num()
    mail = ip.get_mail()
    password = ip.set_password()
    while True:
        match_password = input("enter password again")
        if password == match_password:
            print("Password has been set successfully")
            break
        else:
            print("Not matching,please try again")
            ans = input("Do you want to quit and start over?y/n")
            if ans.lower() == 'y':
                break

    user_id = round(time.time())
    user_data = f"{user_id}:{first_name}:{last_name}:{phone_no}:{mail}:{password}"
    return user_data


