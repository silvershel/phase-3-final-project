# lib/cli.py
from helpers import (
    clear_terminal,
    exit_program,
    list_yarn,
    find_yarn_by_id,
    find_yarn_by_weight,
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
    print("----- \n")
    print("STASH MANAGER")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. View Yarn")
    print("2. View Projects")

def stash_menu():
    print("----- \n")
    print("YARN")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. Main Menu")
    print("2. List all yarn")
    print("3. Find yarn by ID")
    print("4. Find yarn by weight")
    print("5: Add yarn")
    print("6: Update yarn")
    print("7: Delete yarn")

def project_menu():
    print("----- \n")
    print("PROJECTS")
    print("Select an option:")
    print()
    print("0. Exit")
    print("1. Main Menu")
    print("2. List all projects")
    print("3. Find project by yarn weight") # not created
    print("4: Start a project")
    print("5: Update a project")
    print("6: Delete a project")


def main():
    clear_terminal()
    while True:
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
                    find_yarn_by_weight()
                elif choice == "5":
                    add_yarn()
                elif choice == "6":
                    update_yarn()
                elif choice == "7":
                    delete_yarn()
                else:
                    clear_terminal()
                    print("Please select a valid option.\n")
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
                    start_project()
                elif choice == "5":
                    update_project()
                elif choice == "6":
                    delete_project()
                else:
                    clear_terminal()
                    print("Please select a valid option.\n")
        elif choice == "0":
            clear_terminal()
            exit_program()
        else:
            clear_terminal()
            print("Please select a valid option.\n")


if __name__ == "__main__":
    main()
