# lib/cli.py
from models.project import Project
from models.yarn import Yarn
from helpers import (
    clear_terminal,
    clear_and_print,
    exit_program,
    list_all_projects,
    list_one_project,
    add_project,
    update_project,
    add_yarn_to_project,
    remove_yarn_from_project,
    delete_project,
    list_all_yarn,
    list_yarn_used,
    add_yarn,
    update_yarn,
    delete_yarn,
)

def main_menu():
    clear_terminal()
    while True:
        print("STASH MANAGER")
        print()
        print("1. Projects")
        print("2. Yarn")
        print("3. Needles (coming soon)")
        print()
        print("E to Exit")
        print()

        choice = input("> ").upper()
        if choice == "E":
            exit_program()
        elif choice == "1":
            clear_terminal()
            return projects_menu
        elif choice == "2":
            clear_terminal()
            return yarn_menu
        elif choice == "3":
            clear_terminal()
            return needles_menu
        else:
            clear_and_print("Please select a valid option.")

def projects_menu():
    while True:
        print("ALL PROJECTS")
        print()
        list_all_projects()
        print()
        print("-----")
        print()
        print("Enter the project number to view details, edit, or delete.")
        print("Type '+' to add a project")
        print()
        print("B go Back | E to Exit")
        print()
        choice = input("> ").upper()

        if choice == "+":
            add_project()
            clear_terminal()
            return projects_menu
        elif choice == "B":
            return main_menu
        elif choice == "E":
            exit_program()
        elif choice.isdigit():
            clear_terminal()
            project_num = int(choice)
            projects = Project.get_all()
            if 1 <= project_num <= len(projects):
                return lambda: project_details_menu(project_num)
            else:
                clear_and_print("Please select a valid option.")
        else:
            clear_and_print("Please select a valid option.")

def project_details_menu(project_num):
    while True:
        print("PROJECT DETAILS")
        print()
        list_one_project(project_num)
        print()
        print("-----")
        print()
        print("1. Add yarn to project")
        print("2. Remove yarn from project")
        print("3. Update details")
        print("4. Delete")
        print()
        print("B go Back | E to Exit")
        print()
        choice = input("> ").upper()

        if choice == "B":
            clear_terminal()
            projects_menu()
        elif choice == "E":
            exit_program()
        elif choice == "1":
            clear_terminal()
            return lambda: add_yarn_menu(project_num)
        elif choice == "2":
            clear_terminal()
            return lambda: remove_yarn_menu(project_num)
        elif choice == "3":
            update_project(project_num)
            return lambda: project_details_menu(project_num)
        elif choice == "4":
            delete_project(project_num)
            clear_terminal()
            return projects_menu
        else:
            clear_and_print("Please select a valid option.")

    
def add_yarn_menu(project_num):
    while True:    
        print("ALL YARN")
        print()
        list_all_yarn()
        print("-----")
        print()
        print("Enter a number to select")
        print("B go Back | E to Exit")
        print()
        choice = input("> ").upper()

        if choice == "B":
            clear_terminal()
            project_details_menu(project_num)
        elif choice == "E":
            exit_program()
        elif choice.isdigit():
            yarns = Yarn.get_all()
            yarn_num = int(choice)
            if 1 <= yarn_num <= len(yarns):
                clear_terminal()
                add_yarn_to_project(project_num, yarn_num)
                project_details_menu(project_num)
            else:
                clear_and_print("Please select a valid option.")
                add_yarn_menu(project_num)
        else:
            clear_and_print("Please select a valid option.")
    
def remove_yarn_menu(project_num):
    while True:    
        print("USED YARN")
        print()
        list_yarn_used(project_num)
        print("-----")
        print()
        print("Enter a number to select.")
        print("B go Back | E to Exit")
        print()
        choice = input("> ").upper()

        if choice == "B":
            clear_terminal()
            return lambda: project_details_menu(project_num)
        elif choice == "E":
            exit_program()
        elif choice.isdigit():
            yarn_num = int(choice)
            yarns = Yarn.get_all()
            if 1 <= yarn_num <= len(yarns):
                remove_yarn_from_project(project_num, yarn_num)
                clear_terminal()
            else:
                clear_and_print("Please select a valid option.")
                return project_details_menu(project_num)
        else:
            clear_and_print("Please select a valid option.")
            return project_details_menu(project_num)

def yarn_menu():
    yarns = Yarn.get_all()
    print("ALL YARN")
    print()
    list_all_yarn()
    print("-----")
    print()
    print("YARN")
    print()
    print("1. Add yarn")
    print("2: Update yarn")
    print("3: Delete yarn")
    print()
    print("B go Back | E to Exit")
    print()
    choice = input("> ").upper()
    
    if choice == "E":
        exit_program()
    elif choice == "B":
        return main_menu
    elif choice == "1":
        add_yarn()
        clear_terminal()
        yarn_menu()
    elif choice in ["2", "3"]:
        try:
            yarn_num = int(input(f"Enter the yarn number to {'update' if choice == '2' else 'delete'}: "))
            if 1 <= yarn_num <= len(yarns):
                if choice == "2":
                    update_yarn(yarn_num)
                    clear_terminal()
                    yarn_menu()
                elif choice == "3":
                    delete_yarn(yarn_num)
                    clear_terminal()
                    yarn_menu()
            else:
                clear_and_print("Please select a valid option.")
                yarn_menu()
        except ValueError:
            clear_and_print("Please select a valid option.")
            yarn_menu()
    else:
        clear_and_print("Please select a valid option.")
        yarn_menu()

def needles_menu():
    while True:
        print("NEEDLES (COMING SOON)")
        print()
        print("-----")
        print()
        print("Enter a number to select")
        print("B go Back | E to Exit")
        print()
        choice = input("> ").upper()
        if choice == "B":
            main_menu()
        elif choice == "E":
            exit_program()
        else:
            clear_and_print("Please select a valid option.")

def run_menu():
    current_menu = main_menu
    while current_menu:
        current_menu = current_menu()

if __name__ == "__main__":
    run_menu()