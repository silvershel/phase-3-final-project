# lib/helpers.py
import os
from models.project import Project
from models.yarn import Yarn

# TO DO
# Add one to many relationship
# YARN Update add_yarn function for easy input (no exiting, enter to pass through)
# YARN Update update_yarn function for easy inputs (no exiting, enter to pass through)
# PROJECT Add find_by_type function
# Look for repeated code and create functions to simplify
    # get_input
    # display_message
    # display_items
    # find_item_by_attribute
# Be able to exit out from updating an entry.
# Title case check (Farmer's going to Farmer'S)

# STRETCH 
# Delete number of skeins only?
# Add yarn with same details to existing entries?



# HELPER FUNCTIONS
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit_program():
    clear_terminal()
    print("Your stash has been managed. Goodbye.")
    exit()

def get_valid_weight():
    valid_weights = ["lace", "sock", "sport", "dk", "worsted", "aran", "bulky"]
    
    while True:
        weight = input("Enter the yarn weight: ").lower()
        if weight in valid_weights:
            return weight
        else:
            print("Invalid weight. Please enter one of the following: lace, sock, sport, DK, worsted, aran, or bulky.")

# STASH FUNCTIONS
# No changes
def list_yarn():
    clear_terminal()
    print("ALL YARN\n")
    yarns = Yarn.get_all()
    if yarns:
        sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
        for yarn in sorted_yarns:
            print(yarn)
        print("Scroll up to view.\n")
    else:
        print("No yarn in stash.\n")

def find_yarn_by_brand():
    clear_terminal()
    brand = input("Enter the brand: ")
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.brand.lower() == brand.lower()]
    if matching_yarns:
        clear_terminal()
        for yarn in matching_yarns:
            print(yarn)
        print("Scroll up to view.\n")
    else:
        clear_terminal()
        print(f"No {brand.lower()} in stash.\n")

# No changes
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
        print("Scroll up to view.\n")
    else:
        clear_terminal()
        print(f"No {weight.lower()} weight yarn in stash.\n")

def add_yarn():
    clear_terminal()
    brand = input("Enter the yarn brand: ")
    base = input("Enter the base name: ")
    color = input("Enter the yarn color: ")
    weight = get_valid_weight()
    yds = int(input("Enter the number of yds in each skein: "))
    qty = int(input("Enter the total number of skeins: "))
    try:
        yarn = Yarn.create(brand, base, color, weight, yds, qty)
        clear_terminal()
        print(f"{yarn}\nScroll up to view.\n")
    except Exception as exc:
        clear_terminal()
        print("Error adding new yarn: ", exc)

def update_yarn():
    clear_terminal()
    id_ = input("Enter the ID of the yarn you want to update: ")
    if yarn := Yarn.find_by_id(id_):
        try:
            # working on this to loop to make sure brand 
            # is correctly entered and doesn't go back 
            # to the main screen. Then update others.
            while True:
                brand = input("Enter the brand: ")
                if brand:
                    yarn.brand = brand
                    break
                else:
                    print("Brand cannot be empty. Please try again.")
            base = input("Enter the base name: ")
            yarn.base = base
            color = input("Enter the color: ")
            yarn.color = color
            weight = get_valid_weight()
            yarn.weight = weight
            yds = int(input("Enter the number of yds in each skein: "))
            yarn.yds = yds
            qty = int(input("Enter the qty: "))
            yarn.qty = qty
            yarn.update()
            clear_terminal()
            print(f"{yarn}\nScroll up to view.\n")
        except Exception as exc:
            clear_terminal()
            print("Error updating yarn: ", exc)
    else:
        clear_terminal()
        print(f"Yarn not found.\n")

# No changes
def delete_yarn():
    clear_terminal()
    id_ = input("Enter the ID of the yarn you want to delete: ")
    if yarn := Yarn.find_by_id(id_):
        clear_terminal()
        print(f"Yarn {yarn.id} has been deleted.\n")
        yarn.delete()
    else:
        clear_terminal()
        print(f"Yarn not found.\n")


# PROJECT FUNCTIONS
def list_projects():
    clear_terminal()
    print("ALL PROJECTS\n")
    projects = Project.get_all()
    if projects:
        for project in projects:
            print(project)
        print("Scroll up to view.\n")
    else:
        print("No projects in database.\n")

def find_project_by_weight():
    clear_terminal()
    weight = input("Enter the yarn weight used: ")
    projects = Project.get_all()
    matching_projects = [project for project in projects if project.weight.lower() == weight.lower()]
    if matching_projects:
        clear_terminal()
        for project in matching_projects:
            print(project)
            print("Scroll up to view.\n")
    else:
        clear_terminal()
        print(f"No {weight.lower()} weight projects in library.\n")

def add_project():
    clear_terminal()
    name = input("Enter the project name: ")
    type = input("Enter the project type (eg, sweater, hat...): ")
    size = input("Enter the size being made (n/a for none): ")
    weight = get_valid_weight()
    yds_needed = int(input("Enter the approximate yardage needed: "))
    try:
        project = Project.create(name, type, size, weight, yds_needed)
        clear_terminal()
        print(f"{project}\nScroll up to view.\n")
    except Exception as exc:
        clear_terminal()
        print("Error adding new project: ", exc)

def update_project():
    clear_terminal()
    id_ = input("Enter the ID of the project you want to update: ")
    if project := Project.find_by_id(id_):
        try:
            name = input("Enter the name: ")
            project.name = name
            type = input("Enter the project type (eg, sweater, hat...): ")
            project.type = type
            size = input("Enter the size being made (n/a for none): ")
            project.size = size
            weight = input("Enter the weight of the yarn used: ")
            project.weight = weight
            project.update()
            clear_terminal()
            print(f"{project}\nScroll up to view.\n")
        except Exception as exc:
            clear_terminal()
            print("Error updating project: ", exc)
    else:
        clear_terminal()
        print(f"Project not found.\n")

# No changes
def delete_project():
    clear_terminal()
    id_ = input("Enter the ID of the project you want to delete: ")
    if project := Project.find_by_id(id_):
        clear_terminal()
        print(f"Project {project.id} has been deleted.\n")
        project.delete()
    else:
        clear_terminal()
        print(f"Project not found.\n")