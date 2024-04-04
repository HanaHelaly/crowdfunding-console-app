def save_user(user_data):
    user_data = user_data.strip()
    user_data = user_data+'\n'
    try:
        with open('users.txt','a') as users_f:
            users_f.write(user_data)
    except:
        print("Cannot add user")
        return False
    else:
        print("user has been added successfully!")
        return True


def save_project(project_data):
    project_data = project_data.strip()
    project_data = project_data+'\n'
    try:
        with open('projects.txt','a') as projects_f:
            projects_f.write(project_data)
    except:
        print("Cannot add project")
        return False
    else:
        print("project has been added successfully!")
        return True