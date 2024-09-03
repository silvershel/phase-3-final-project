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
    list_yarn_by_brand,
    list_yarn_by_weight,
    add_yarn,
    update_yarn,
    delete_yarn,
)

def main_menu():
    print("STASH MANAGER")
    print()
    print("1. Projects")
    print("2. Yarn")
    print("3. Needles (coming soon)")
    print()
    print("E to Exit")
    print()

def projects_menu():
    print("-----")
    print()
    print("Enter the project number to view details, edit, or delete.")
    print("Type '+' to add a project")
    print()
    print("B go Back | E to Exit")
    
    print()

def project_menu():
    print("-----")
    print()
    print("1. Add yarn to project")
    print("2. Remove yarn from project")
    print("3. Update details")
    print("4. Delete")
    print()
    print("B go Back | E to Exit")
    print()

def mini_menu():
    print("-----")
    print()
    print("Enter a number to select")
    print("B go Back | E to Exit")
    print()

def yarn_menu():
    print("-----")
    print()
    print("YARN")
    print()
    print("1. List all yarn")
    print("2. List yarn by brand")
    print("3. List yarn by weight")
    print("4. Add yarn")
    print("5: Update yarn")
    print("6: Delete yarn")
    print()
    print("B go Back | E to Exit")
    print()

def main():
    clear_terminal()
    while True:
        main_menu()
        choice = input("> ").upper()
        if choice == "1":
            while True:
                clear_and_print("ALL PROJECTS")
                list_all_projects()
                print()
                projects_menu()
                choice = input("> ").upper()
                if choice == "B":
                    clear_terminal()
                    break
                elif choice == "E":
                    clear_terminal()
                    exit_program()
                elif choice == "+":
                    add_project()
                elif choice.isdigit():
                    user_input = int(choice)
                    projects = Project.get_all()
                    if 1 <= user_input <= len(projects):
                        while True: 
                            clear_and_print("PROJECT DETAILS")
                            list_one_project(user_input)
                            print()
                            project_menu()
                            choice = input("> ").upper()
                            if choice == "B":
                                clear_terminal()
                                break
                            elif choice == "E":
                                clear_terminal()
                                exit_program()
                                break
                            elif choice == "1":
                                clear_terminal()
                                while True: 
                                    list_all_yarn()
                                    mini_menu()
                                    choice = input("> ").upper()  
                                    if choice == "B":
                                        clear_terminal()
                                        break
                                    elif choice == "E":
                                        clear_terminal()
                                        exit_program()
                                    elif choice.isdigit():
                                        yarns = Yarn.get_all()
                                        yarn_input = int(choice)
                                        if 1 <= yarn_input <= len(yarns):
                                            add_yarn_to_project(user_input, yarn_input)  
                                        else:
                                            print("Please select a valid option.")
                                    else:
                                        print("Please select a valid option.")       
                            elif choice == "2":         
                                while True:
                                    list_yarn_used(user_input)
                                    mini_menu()
                                    choice = input("> ").upper()
                                    if choice.isdigit():
                                        yarn_input = choice
                                        remove_yarn_from_project(user_input, yarn_input)
                                    elif choice == "B":
                                        clear_terminal()
                                        break
                                    elif choice == "E":
                                        clear_terminal()
                                        exit_program()
                                    else:
                                        clear_and_print("Please select a valid option.")
                            elif choice == "3":
                                update_project(user_input)
                            elif choice == "4":
                                delete_project(user_input)
                                break
                            else:
                                clear_and_print("Please select a valid option.")
                    else:
                        clear_and_print("Please select a valid option.") 
                else:
                    clear_and_print("Please select a valid option.")
        elif choice == "2":
            clear_terminal()
            while True:
                yarn_menu()
                choice = input("> ").upper()
                if choice == "E":
                    clear_terminal()
                    exit_program()
                elif choice == "B":
                    clear_terminal()
                    break
                elif choice == "1":
                    list_all_yarn()
                elif choice == "2":
                    list_yarn_by_brand()
                elif choice == "3":
                    list_yarn_by_weight()
                elif choice == "4":
                    add_yarn()
                elif choice == "5":
                    update_yarn()
                elif choice == "6":
                    delete_yarn()
                else:
                    clear_and_print("Please select a valid option.")
        elif choice == "3":
            clear_and_print("NEEDLES (COMING SOON)")
            while True:
                mini_menu()
                choice = input("> ").upper()
                if choice == "B":
                    clear_terminal()
                    break
                elif choice == "E":
                    clear_terminal()
                    exit_program()
                else:
                    clear_and_print("NEEDLES (COMING SOON)", "Please select a valid option.")
        elif choice == "E":
            clear_terminal()
            exit_program()
        else:
            clear_and_print("Please select a valid option.")


if __name__ == "__main__":
    main()
