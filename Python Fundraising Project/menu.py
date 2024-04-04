import projects
import inputs as ip
from login import login, password_chg
from register import registration
from colorama import Fore, Style
from filehandler import save_user
from filehandler import save_project


def highlight_text_colorama(text, style):
    return f"{style}{text}{Style.RESET_ALL}"


def menu():
    print(highlight_text_colorama("WELCOME TO #1 FUNDRAISING PLATFORM!\n", Fore.LIGHTCYAN_EX+ Style.BRIGHT))
    while True:
        menu_list = ["Login", "Register", "Exit"]
        for i in menu_list:
            print("\t\t\t\t\t\t\t\t\t", end=' ')
            print(highlight_text_colorama(i, Fore.CYAN + Style.BRIGHT))
        ch = input(highlight_text_colorama("To Register press R:\nAlready have an account? press L to login: \nExit press E: ", Fore.LIGHTBLACK_EX + Style.NORMAL))
        if ch.isalpha() and len(ch) == 1:
            if ch.lower() == 'l':
                print('\n\n\n\n\n\n\n')
                print(highlight_text_colorama("Logging in:", Fore.MAGENTA + Style.BRIGHT))
                user_data = login()

                if user_data:
                    logged = True
                    while logged:
                        print(f"\n\n\n\n\n\n\n")
                        print(f"Welcome, {user_data[1]} {user_data[2]}!")
                        in_menu_list = ["Create new project", "View all projects", "Edit project", "Delete project",
                                        "Search for project", "Search project on date", "Change Password" ,"Logout"]
                        for index, ob in enumerate(in_menu_list):
                            print(highlight_text_colorama(f"{index + 1} {ob}", Fore.LIGHTMAGENTA_EX + Style.BRIGHT))
                        while True:
                            get_ans = input()
                            if get_ans.isdigit() and len(get_ans) == 1:
                                print(f"\n\n\n\n\n\n\n")
                                if get_ans == '1':
                                    print(highlight_text_colorama("Creating new project", Fore.LIGHTCYAN_EX + Style.BRIGHT))
                                    prepared_project = projects.create_project(user_data[0])
                                    save_project(prepared_project)
                                    break
                                elif get_ans == '2':
                                    print(highlight_text_colorama("ALL projects", Fore.CYAN + Style.BRIGHT))
                                    projects.view_project()
                                    input("press any key to return to main menu")
                                    break
                                elif get_ans == '3':
                                    print(highlight_text_colorama("Edit project", Fore.CYAN + Style.BRIGHT))
                                    while True:
                                        project_title = input("Enter project title you want to edit:")
                                        if project_title.isalpha():
                                            break
                                        if not project_title.isspace():
                                            break
                                        else:
                                            print("Invalid Project Title")
                                    projects.edit_project(user_data[0], project_title)
                                    input("press any key to return to main menu")
                                    break

                                elif get_ans == '4':
                                    print(highlight_text_colorama("Delete project", Fore.CYAN + Style.BRIGHT))
                                    while True:
                                        project_title = input("Enter project title you want to delete: ")
                                        if project_title.isalpha():
                                            break
                                        if not project_title.isspace():
                                            break
                                        else:
                                            print("Invalid Project Title")
                                    projects.delete_project(user_data[0], project_title)
                                    input("press any key to return to main menu")
                                    break

                                elif get_ans == '5':

                                    print(highlight_text_colorama("Searching for project", Fore.LIGHTBLUE_EX + Style.BRIGHT))
                                    project_title = input("Enter project title ")
                                    projects.search_project(project_title)
                                    input("press any key to return to main menu")
                                    break
                                elif get_ans == '6':

                                    print(highlight_text_colorama("Searching for project", Fore.LIGHTBLUE_EX + Style.BRIGHT))
                                    search_date = ip.get_date("Enter the start date of project in format yyyy/mm/dd: ")
                                    projects.search_project_date(search_date)
                                    input("press any key to return to main menu")
                                    break
                                elif get_ans == '7':
                                    print(highlight_text_colorama("Password change", Fore.LIGHTBLUE_EX + Style.BRIGHT))
                                    password_chg(user_data[0])
                                    input("press any key to return to main menu")
                                    break
                                elif get_ans == '8':
                                    print(highlight_text_colorama("Logged out", Fore.LIGHTBLUE_EX + Style.BRIGHT))
                                    logged = False
                                    break
                                else:
                                    print("Out of bounds,Try again")

            elif ch.lower() == 'r':
                print('\n\n\n\n\n\n\n')
                highlight_text = highlight_text_colorama("Registration:", Fore.MAGENTA + Style.BRIGHT)
                print(highlight_text)
                prepared_data = registration()
                save_user(prepared_data)
            elif ch.lower() == 'e':
                exit(0)
            else:
                continue


menu()
