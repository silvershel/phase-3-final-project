# lib/cli.py
from helpers import (
    clear_terminal,
    exit_program,
    list_yarn,
    find_yarn_by_brand,
    find_yarn_by_weight,
    add_yarn,
    update_yarn,
    delete_yarn,
    list_projects,
    find_project_by_weight,
    add_project,
    update_project,
    delete_project
)

def main_menu():
    print("----- \n")
    print("STASH MANAGER")
    print()
    print("1. Yarn")
    print("2. Projects")
    print()
    print("EXIT to exit")
    print()

def stash_menu():
    print("----- \n")
    print("YARN")
    print()
    print("1. List all yarn")
    print("2. Find yarn by brand")
    print("3. Find yarn by weight")
    print("4: Add yarn")
    print("5: Update yarn")
    print("6: Delete yarn")
    print()
    print("EXIT to exit | MAIN for Main Menu")
    print()

def project_menu():
    print("----- \n")
    print("PROJECTS")
    print()
    print("1. List all projects")
    print("2. Find project by yarn weight")
    print("4: Add a project")
    print("3: Update a project")
    print("4: Delete a project")
    print()
    print("EXIT to exit | MAIN for Main Menu")
    print()


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
                if choice == "EXIT":
                    clear_terminal()
                    exit_program()
                elif choice == "MAIN":
                    clear_terminal()
                    break
                elif choice == "1":
                    list_yarn()
                elif choice == "2":
                    find_yarn_by_brand()
                elif choice == "3":
                    find_yarn_by_weight()
                elif choice == "4":
                    add_yarn()
                elif choice == "5":
                    update_yarn()
                elif choice == "6":
                    delete_yarn()
                else:
                    clear_terminal()
                    print("Please select a valid option.\n")
        elif choice == "2":
            clear_terminal()
            while True:
                project_menu()
                choice = input("> ")
                if choice == "EXIT":
                    clear_terminal()
                    exit_program()
                elif choice == "MAIN":
                    clear_terminal()
                    break
                elif choice == "1":
                    list_projects()
                elif choice == "2":
                    find_project_by_weight()
                elif choice == "3":
                    add_project()
                elif choice == "4":
                    update_project()
                elif choice == "5":
                    delete_project()
                else:
                    clear_terminal()
                    print("Please select a valid option.\n")
        elif choice == "EXIT":
            clear_terminal()
            exit_program()
        else:
            clear_terminal()
            print("Please select a valid option.\n")


if __name__ == "__main__":
    main()
