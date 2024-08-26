# lib/helpers.py
import os
from models.project import Project
from models.yarn import Yarn

# TO DO
# YARN Add one to many relationship.
# YARN Add search by color family.
# PROJECT Add find_by_type function.
# Fix inputs and connection to class validation.
# Look for repeated code and create functions to simplify.
    # display_items
    # find_item_by_attribute
# Clean up:
    # Add .strip() to inputs
    # Title case check (Farmer's going to Farmer'S).
    # Exit out of add/update options

# STRETCH 
# YARN Add dye lot option.
# YARN Combine yarn with same details?



# HELPER FUNCTIONS
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_and_print(message_1, message_2=None):
    clear_terminal()
    print(message_1)
    if message_2:
        print(message_2)
    print()

def input_str(field_name):
    while True:
        value = input(f"Enter the {field_name}: ")
        if value:
            return value
        else:
            print(f"Field can not be blank.")

def input_int(field_name):
    while True:
        value = input(f"Enter the {field_name}: ")
        if value.isdigit():
            return int(value)
        elif value == "":
            print("Field cannot be blank.")
        else:
            print("Please enter a number (no letters).")

def check_weight():
    valid_weights = ["lace", "sock", "sport", "dk", "worsted", "aran", "bulky"]

    while True:
        weight = input("Enter the yarn weight: ").lower()
        if weight in valid_weights:
            return weight
        else:
            print('Please enter one of the following: "lace", "sock", "sport", "DK", "worsted", "aran", or "bulky".')
    
def exit_program():
    clear_and_print("Your stash has been managed. Goodbye.")
    exit()

# YARN FUNCTIONS
def list_yarn():
    clear_terminal()
    print("ALL YARN (alphabetical by brand)")
    print()
    yarns = Yarn.get_all()
    if yarns:
        sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
        for yarn in sorted_yarns:
            print(yarn)
        print("Scroll up to view.")
        print()
    else:
        print("No yarn in stash.")
        print()

def find_yarn_by_brand():
    clear_terminal()
    brand = input("Enter the brand: ")
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.brand.lower() == brand.lower()]
    if matching_yarns:
        clear_terminal()
        for yarn in matching_yarns:
            print(yarn)
        print("Scroll up to view.")
        print()
    else:
        clear_and_print(f"No {brand.lower()} in stash.")

def find_yarn_by_weight():
    clear_terminal()
    weight = input("Enter the yarn weight: ")
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.weight.lower() == weight.lower()]
    if matching_yarns:
        clear_terminal()
        sorted_yarns = sorted(matching_yarns, key=lambda yarn: yarn.brand)
        for yarn in sorted_yarns:
            print(yarn)
        print("Scroll up to view.")
        print()
    else:
        clear_and_print(f"No {weight.lower()} weight yarn in stash.")

def add_yarn():
    clear_terminal()
    brand = input_str("brand")
    base = input_str("base")
    color = input_str("color")
    weight = check_weight()
    yds = int(input_int("number of yds per skein"))
    qty = int(input_int("total number of skeins"))
    try:
        yarn = Yarn.create(brand, base, color, weight, yds, qty)
        clear_and_print(yarn, "Scroll up to view.")
    except Exception as exc:
        clear_and_print("Error adding new yarn: ", exc)

def update_yarn():
    clear_terminal()
    id_ = input("Enter the ID of the yarn you want to update: ")
    if yarn := Yarn.find_by_id(id_):
        try:
            yarn.brand = input_str("brand")
            yarn.base = input_str("base")
            yarn.color = input_str("color")
            yarn.weight = check_weight()
            yarn.yds = input_int("number of yds per skein")
            yarn.qty = input_int("total number of skeins")
            yarn.update()
            clear_and_print(yarn, "Scroll up to view.")
        except Exception as exc:
            clear_and_print("Error updating yarn: ", exc)
    else:
        clear_terminal()
        print(f"Yarn not found.\n")

def delete_yarn():
    clear_terminal()
    id_ = input("Enter the ID of the yarn you want to delete: ")
    if yarn := Yarn.find_by_id(id_):
        clear_and_print(f"Yarn {yarn.id} has been deleted.")
        yarn.delete()
    else:
        clear_and_print("Yarn not found.")


# PROJECT FUNCTIONS
def list_projects():
    clear_terminal()
    print("ALL PROJECTS")
    print()
    projects = Project.get_all()
    if projects:
        for project in projects:
            print(project)
        print("Scroll up to view.")
        print()
    else:
        print("No projects in database.")
        print()

def find_project_by_weight():
    clear_terminal()
    weight = input("Enter the yarn weight used: ")
    projects = Project.get_all()
    matching_projects = [project for project in projects if project.weight.lower() == weight.lower()]
    if matching_projects:
        clear_terminal()
        for project in matching_projects:
            print(project)
        print("Scroll up to view.")
        print()
    else:
        clear_and_print(f"No {weight.lower()} weight projects in library.")

def add_project():
    clear_terminal()
    pattern = input("Enter the pattern name: ")
    type = input("Enter the project type (eg, sweater, hat...): ")
    size = input("Enter the size being made (n/a for none): ")
    weight = check_weight()
    yds_needed = int(input("Enter the approximate yardage needed: "))
    try:
        project = Project.create(pattern, type, size, weight, yds_needed)
        clear_and_print(project, "Scroll up to view.")
    except Exception as exc:
        clear_and_print("Error adding new project: ", exc)

def update_project():
    clear_terminal()
    id_ = input("Enter the ID of the project you want to update: ")
    if project := Project.find_by_id(id_):
        try:
            project.pattern = input_str("pattern name")
            project.type = input_str("project type")
            project.size = input_str("size being made")
            project.weight = check_weight()
            project.yds_needed = input_int("yds needed")
            project.update()
            clear_and_print(project, "Scroll up to view.")
        except Exception as exc:
            clear_and_print("Error updating project: ", exc)
    else:
        clear_and_print(f"Project not found.")

def delete_project():
    clear_terminal()
    id_ = input("Enter the ID of the project you want to delete: ")
    if project := Project.find_by_id(id_):
        clear_and_print(f"Project {project.id} has been deleted.")
        project.delete()
    else:
        clear_and_print(f"Project not found.")