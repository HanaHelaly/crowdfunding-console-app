import time
from inputs import get_date


def create_project(user_id):

    while True:
        title = input("Project title:")
        if title.isalpha():
            break
        if not title.isspace():
            break
        else:
            print("Invalid Project Title")

    while True:
        description = input("Project description:")
        if description.isalnum():
            break
        if not description.isspace():
            break
        else:
            print("Invalid Project description")

    while True:
        try:
            target = int(input("Total target in EGP"))
            if target < 100000:
                print("out of range")
                continue
        except ValueError:
            print("Not a number")
        else:
            break
    start_date = get_date("enter the start date of the project in format :yyyy/mm/dd")
    end_date = get_date("enter the end date of the project in format :yyyy/mm/dd")
    project_id = round(time.time())
    project_data = f"{user_id}:{project_id}:{title}:{description}:{target}:{start_date}:{end_date}\n"
    return project_data


def view_project():
    with open('C:\\Users\\hp\\PycharmProjects\\pythonProjectlab3\\projects.txt', 'r') as projects_f:
        contents = projects_f.readlines()

    for index, content in enumerate(contents):
        content = content.strip().split(":")
        print(f"{index + 1}) Project title:{content[2]}")
        print(f"Project Description:{content[3]}")
        print(f"Target fund:{content[4]}EGP")
        print(f"Project start date:{content[5]}")
        print(f"Project end date:{content[6]}\n")


def project_auth(user_id, project_id):
    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()
    for row in p_contents:
        p = row.strip().split(":")
        if str(user_id) == p[0] and project_id == p[1]:
            return True
    return False


def delete_project(user_id, project_title):
    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()
    for index, row in enumerate(p_contents):
        project = row.strip().split(":")
        if project[2].strip().lower() == project_title.strip().lower():
            project_id = project[1]
            project_owner = project[0]
            print("Project was found")
            break
    else:
        print("project not found")
        return 0

    if str(user_id) == project_owner:
        print("Please enter your modifications")
        for index, row in enumerate(p_contents):
            p = row.strip().split(":")
            if str(project_id) == p[1]:
                p_contents.pop(index)
                break
        with open('projects.txt', 'w') as proj_f:
            proj_f.writelines(p_contents)
        print("project has been deleted")
    else:
        print("Failed authorization")


def get_user_projects(user_id):

    projects_for_user = []

    with open('projects.txt', 'r') as project_f:
        project_contents = project_f.readlines()
        for proj_row in project_contents:
            project_data = proj_row.strip().split(":")
            if str(user_id) == project_data[0]:
                project_id = project_data[1]
                project_tile = project_data[2]
                projects_for_user.append([project_id, project_tile])

    return projects_for_user


def edit_project(user_id, project_title):

    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()
    for index, row in enumerate(p_contents):
        project = row.strip().split(":")
        if project[2].strip().lower() == project_title.strip().lower():
            project_id = project[1]
            project_owner = project[0]
            print("Project was found")
            break
    else:
        print("project not found")
        return 0

    if str(user_id) == project_owner:
        print("Please enter your modifications")
        for index, row in enumerate(p_contents):
            p = row.strip().split(":")
            if str(project_id) == p[1]:
                p_contents[index] = create_project(user_id)
                break

        with open('projects.txt', 'w') as proj_f:
            proj_f.writelines(p_contents)

        print("project has been updated")

    else:
        print("Failed authorization")


def search_project_date(start_date):
    matching_projects = []
    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()
    for index, row in enumerate(p_contents):
        project = row.strip().split(":")
        if project[5].strip() == start_date.strip():
            matching_projects.append(project[2])

    for project in matching_projects:
        search_project(project)

""""def search_project_date(start_date):
    matching_projs = []
    proj_row = None
    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()

    for row in p_contents:
        proj_row = row.strip().split(":")
        if start_date.strip() == proj_row[5].strip():
            matching_projs.append(proj_row)

    if len(matching_projs) == 0:
        print("no projects found")
    return matching_projs"""


def search_project(project_title):
    notfound = 1
    with open('projects.txt', 'r') as proj_f:
        p_contents = proj_f.readlines()
    for index, row in enumerate(p_contents):
        project = row.strip().split(":")
        if project_title.strip().lower() in project[2].strip().lower():
            print(f"Project ID: {project[1]}")
            print(f"Project Name: {project[2]}")
            print(f"Project Description: {project[3]}")
            print(f"Project Target funds: {project[4]}")
            print(f"Project Start Date: {project[5]}")
            print(f"Project End Date: {project[6]}\n")
            notfound = 0
    if notfound:
        print("No matching projects")


if __name__ == "__main__":
    #user_projects=get_user_projects(1700232144)
    #project_title = input("Enter project title you want to delete:")
    #delete_project(1700232144,project_title)
    start_date=('2023-12-30')
    search_project_date(start_date)