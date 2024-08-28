# lib/helpers.py

import os
from models.project import Project
from models.yarn import Yarn

# TO DO
# print yarns added to project 
# update_yarn connects to stash.
# no yarn available if in use by another project. 
# List project title under each yarn and change format (color?) to highlight, else None.
# List yarn used under each project.
# List all yarns: add aditional logic to continue alphebetizing by color.

# STRETCH
# YARN - Add color_family
# YARN - Add find_by_color_family
# Be able to search for yarns when adding a project based on multiple attributes.
# Be able to exit out of editing "add" and "update" fields.
# Title case check (Farmer's going to Farmer'S).
# Add .strip() to clean up inputs


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

def print_with_return(message):
    print(message)
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

def check_brand():
    yarns = Yarn.get_all()
    valid_brands = [yarn.brand for yarn in yarns]
    while True:
        brand = input("Enter the brand: ").title()
        if brand in valid_brands:
            return brand
        else:
            print(f"Not found. Please enter one of the following brands: {', '.join(sorted(set(valid_brands)))}")

def check_category():
    valid_categories = ["garment", "accessory", "other"]
    while True:
        category = input("Enter the project category: ").lower()
        if category in valid_categories:
            return category
        else:
            print('Please enter one of the following: "garment", "accessory", or "other"')

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
    print_with_return("ALL YARN (alphabetical by brand)")
    yarns = Yarn.get_all()
    if yarns:
        sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
        for yarn in sorted_yarns:
            print(yarn)
        print_with_return("Scroll up to view.")
    else:
        print_with_return("No yarn in stash.")

def find_yarn_by_brand():
    clear_terminal()
    brand = check_brand()
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.brand.lower() == brand.lower()]
    if matching_yarns:
        clear_terminal()
        for yarn in matching_yarns:
            print(yarn)
        print_with_return("Scroll up to view.")
    else:
        clear_and_print(f"No {brand.lower()} in stash.")

def find_yarn_by_weight():
    clear_terminal()
    weight = check_weight()
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.weight.lower() == weight.lower()]
    if matching_yarns:
        clear_terminal()
        sorted_yarns = sorted(matching_yarns, key=lambda yarn: yarn.brand)
        for yarn in sorted_yarns:
            print(yarn)
        print_with_return("Scroll up to view.")
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
    project_id = None
    try:
        yarn = Yarn.create(brand, base, color, weight, yds, qty, project_id)
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
            project_id = input("Enter the project ID (enter to skip): ")
            yarn.id = id_

            if project_id == "":
                current_project_id = yarn.project_id
                yarn.project_id = current_project_id
            else:
                yarn.project_id = int(project_id)
                    
            yarn.update()
            clear_and_print(yarn, "Scroll up to view.")
        except Exception as exc:
            clear_and_print("Error updating yarn: ", exc)
    else:
        clear_and_print(f"Yarn not found.")

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
    print_with_return("ALL PROJECTS")
    projects = Project.get_all()
    if projects:
        sorted_projects = sorted(projects, key=lambda project: project.pattern)
        for project in sorted_projects:
            print(project)
        print_with_return("Scroll up to view.")
    else:
        print_with_return("No projects in database.")

def find_project_by_category():
    clear_terminal()
    category = check_category()
    projects = Project.get_all()
    matching_projects = [project for project in projects if project.category.lower() == category.lower()]
    if matching_projects:
        clear_terminal()
        for project in matching_projects:
            print(project)
        print_with_return("Scroll up to view.")
    else:
        clear_and_print(f"No {category} projects in library.")

def find_project_by_weight():
    clear_terminal()
    weight = check_weight()
    projects = Project.get_all()
    matching_projects = [project for project in projects if project.weight.lower() == weight.lower()]
    if matching_projects:
        clear_terminal()
        for project in matching_projects:
            print(project)
        print_with_return("Scroll up to view.")
    else:
        clear_and_print(f"No {weight.lower()} weight projects in library.")

def add_project():
    clear_terminal()
    pattern = input_str("pattern name")
    category = check_category()
    size = input_str("size being made")
    weight = check_weight()
    yds_needed = input_int("yds needed")

    try:
        project = Project.create(pattern, category, size, weight, yds_needed)
        yarns = Yarn.get_all()
        matching_yarns = [yarn for yarn in yarns if yarn.weight.lower() == weight.lower()]
        
        if matching_yarns:
            while True:
                connect_yarn = input("Would you like to connect yarn from your stash? (Y/N): ").upper()
                if connect_yarn == "N":
                    clear_terminal()
                    print(project)
                    break
                elif connect_yarn == "Y":
                    clear_terminal()
                    for yarn in matching_yarns:
                        print(yarn)
                    
                    while True:
                        yarn_id = input("Please enter the ID of the yarn you'd like to use: ")
                        yarn = Yarn.find_by_id(yarn_id)
                        if yarn:
                            yarn.project_id = project.id
                            yarn.update()
                            print_with_return(f"{yarn.brand} {yarn.base}, {yarn.color} connected.")
                        else:
                            print("Yarn not found.")

                        more_yarn = input("Would you like to add more yarn? (Y/N): ").upper()
                        if more_yarn == "N":
                            clear_and_print(project, "Scroll up to view.")
                            break
                    break
                                        
        else:
            clear_and_print(project, "Scroll up to view.")

    except Exception as exc:
        clear_and_print("Error adding new project: ", exc)

def update_project():
    clear_terminal()
    id_ = input("Enter the ID of the project you want to update: ")
    if project := Project.find_by_id(id_):
        try:
            project.pattern = input_str("pattern name")
            project.category = check_category()
            project.size = input_str("size being made")
            project.weight = check_weight()
            project.yds_needed = input_int("yds needed")
            project.id = id_
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