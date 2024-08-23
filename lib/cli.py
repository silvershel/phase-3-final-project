# lib/cli.py
from helpers import (
    clear_terminal,
    exit_program,
    list_yarn,
    find_yarn_by_id,
    add_yarn,
    update_yarn,
    delete_yarn,
    list_projects,
    find_project_by_id,
    create_project,
    update_project,
    delete_project
)

def main_menu():
    print()
    print("STASH MANAGER")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. Go to Stash")
    print("2. Go to Projects")

def stash_menu():
    print()
    print("STASH")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. Main Menu")
    print("2. List all yarn in stash")
    print("3. Find yarn by ID")
    print("4: Create yarn")
    print("5: Update yarn")
    print("6: Delete yarn")

def project_menu():
    print()
    print("PROJECTS")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. Main Menu")
    print("2. List all projects")
    print("3. Find project by yarn weight") # not created
    print("4: Create project")
    print("5: Update project")
    print("6: Delete project")


def main():
    while True:
        clear_terminal()
        main_menu()
        choice = input("> ")
        if choice == "1":
            clear_terminal()
            while True:
                stash_menu()
                choice = input("> ")
                if choice == "0":
                    clear_terminal()
                    exit_program()
                elif choice == "1":
                    clear_terminal()
                    break
                elif choice == "2":
                    list_yarn()
                elif choice == "3":
                    find_yarn_by_id()
                elif choice == "4":
                    add_yarn()
                elif choice == "5":
                    update_yarn()
                elif choice == "6":
                    delete_yarn()
                else:
                    print("Please select a valid option")
        elif choice == "2":
            clear_terminal()
            while True:
                project_menu()
                choice = input("> ")
                if choice == "0":
                    clear_terminal()
                    exit_program()
                elif choice == "1":
                    clear_terminal()
                    break
                elif choice == "2":
                    list_projects()
                elif choice == "3":
                    find_project_by_id()
                elif choice == "4":
                    create_project()
                elif choice == "5":
                    update_project()
                elif choice == "6":
                    delete_project()
                else:
                    print("Please select a valid option")
        elif choice == "0":
            clear_terminal()
            exit_program()
        else:
            print("Please select a valid option")


if __name__ == "__main__":
    main()
