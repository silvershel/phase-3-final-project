# lib/helpers.py

import os
from models.project import Project
from models.yarn import Yarn

# TO DO
# Mark yarn as unavailable if in use by another project.
# Refactor repetitive code.
# Check all validations and error handling.
# Add ability to skip input fields.
# Add ability to exit out of input fields.

# GENERAL FUNCTIONS
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_and_print(message_1, message_2=None):
    clear_terminal()
    print(message_1)
    print()
    if message_2:
        print(message_2)
        print()

def print_with_return(message):
    print(message)
    print()

def capitalize_first_letter(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

def input_str(field_name):
    while True:
        value = input(f"Enter the {field_name}: ").lower()
        if value == "dk":
            return "DK"
        elif value:
            return capitalize_first_letter(value)
        else:
            print("Field can not be blank.")

def input_int(field_name):
    while True:
        value = input(f"Enter the {field_name}: ")
        if value.isdigit():
            return int(value)
        elif value == "":
            print("Field cannot be blank.")
        else:
            print("Please enter a number (no letters).")

def select_brand():
    while True:
        yarns = Yarn.get_all()
        brands = sorted(set(yarn.brand for yarn in yarns))

        for i, brand in enumerate(brands, start=1):
            print(f"{i}. {brand}")

        user_input = input("Enter the brand: ")
        
        if user_input.isdigit() and 1 <= int(user_input) <= len(brands):
            return brands[int(user_input) - 1]
        else:
            print("Please enter a valid option.")

def select_category():
    while True:
        valid_categories = Project.VALID_CATEGORIES
        
        for i, weight in enumerate(valid_categories, start=1):
            print(f"{i}. {weight}")

        user_input = input("Enter the category: ")
        
        if user_input.isdigit() and 1 <= int(user_input) <= len(valid_categories):
            return valid_categories[int(user_input) - 1]
        else:
            print("Please enter a valid option.")

def select_weight():
    while True:
        valid_weights = Yarn.VALID_WEIGHTS
        
        for i, weight in enumerate(valid_weights, start=1):
            print(f"{i}. {weight}")

        user_input = input("Enter the weight: ")
        
        if user_input.isdigit() and 1 <= int(user_input) <= len(valid_weights):
            return valid_weights[int(user_input) - 1]
        else:
            print("Please enter a valid option.")
                
def exit_program():
    clear_and_print("Your stash has been managed. Goodbye.")
    exit()

# PROJECT FUNCTIONS
def list_all_projects():
    projects = Project.get_all()
    if projects:
        sorted_projects = sorted(projects, key=lambda project: project.pattern)
        for i, project in enumerate(sorted_projects, start=1):
            print(f"{i}. {project.pattern}")
    else:
        print_with_return("No projects in database.")

def list_one_project(project_num):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[project_num - 1].id)
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.project_id == selected_project.id]
    
    if 1 <= project_num <= len(projects):
        if not matching_yarns:
            print(f"{selected_project.pattern}\nDesigner: {selected_project.designer}\nCategory: {selected_project.category}\nSize: {selected_project.size}\nWeight: {selected_project.weight}\nYds Needed: {selected_project.yds_needed}")
        else: 
            print_with_return(f"{selected_project.pattern}\nDesigner: {selected_project.designer}\nCategory: {selected_project.category}\nSize: {selected_project.size}\nWeight: {selected_project.weight}\nYds Needed: {selected_project.yds_needed}")
            print("YARNS USING:")
            for yarn in matching_yarns:
                print(f"{yarn.brand} {yarn.base}, {yarn.color}")
    else:
        clear_and_print("Project not found.")

def add_project():
    clear_and_print("NEW PROJECT")
    pattern = input_str("pattern name")
    designer = input_str("designer")
    category = select_category()
    size = input_str("size being made")
    weight =  select_weight()
    yds_needed = input_int("yds needed")

    try:
        Project.create(pattern, designer, category, size, weight, yds_needed)

    except Exception as exc:
        clear_and_print("Error adding new project: ", exc)

def update_project(user_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)
    
    if selected_project in projects:
        clear_and_print("PROJECT DETAILS")
        selected_project.pattern = input_str("pattern name")
        selected_project.designer = input_str("designer")
        selected_project.category = select_category()
        selected_project.size = input_str("size being made")
        selected_project.weight =  select_weight()
        selected_project.yds_needed = input_int("yds needed")                  
        selected_project.update()
    else:
        clear_and_print("Project not found.")

def delete_project(user_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)

    yarns = Yarn.get_all()
    for yarn in yarns:
        if yarn.project_id == selected_project.id:
            yarn.project_id = None
            yarn.update()

    if selected_project in projects:
        selected_project.delete()
    else:
        print("Cannot delete. Project not found.")

def add_yarn_to_project(user_input, yarn_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)
    
    yarns = Yarn.get_all()
    sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
    selected_yarn = Yarn.find_by_id(sorted_yarns[int(yarn_input) - 1].id)

    if selected_yarn:
        selected_yarn.project_id = int(selected_project.id)
        selected_yarn.update()

def remove_yarn_from_project(user_input, yarn_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)
    
    yarns = Yarn.get_all()
    used_yarns = [yarn for yarn in yarns if yarn.project_id == selected_project.id]
    selected_yarn = Yarn.find_by_id(used_yarns[int(yarn_input) - 1].id)

    if selected_yarn:
        selected_yarn.project_id = None
        selected_yarn.update()

# YARN FUNCTIONS        
def list_all_yarn():
    yarns = Yarn.get_all()
    if yarns:
        sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
        for i, yarn in enumerate(sorted_yarns, start=1):
            print_with_return(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}")
        print_with_return("Scroll up to view.")
    else:
        print_with_return("No yarn in stash.")

def list_yarn_used(user_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)

    yarns = Yarn.get_all()
    used_yarns = [yarn for yarn in yarns if yarn.project_id == selected_project.id]

    if used_yarns:
        for i, yarn in enumerate(used_yarns, start=1):
            print_with_return(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}")
    else:
        print_with_return("No yarn being used.")

def add_yarn():
    clear_and_print("YARN DETAILS")
    brand = input_str("brand")
    base = input_str("base")
    color = input_str("color")
    weight =  select_weight()
    yds = input_int("number of yds per skein")
    qty = input_int("total number of skeins")
    project_id = None

    try:
        yarn = Yarn.create(brand, base, color, weight, yds, qty, project_id)
        clear_and_print("YARN ADDED", f"{yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}")

    except Exception as exc:
        clear_and_print("Error adding new yarn: ", exc)
    
def update_yarn(yarn_to_update):
    yarns = Yarn.get_all()
    sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
    selected_yarn = Yarn.find_by_id(sorted_yarns[yarn_to_update - 1].id)

    if selected_yarn:
        clear_and_print("YARN DETAILS")
        selected_yarn.brand = input_str("brand")
        selected_yarn.base = input_str("base")
        selected_yarn.color = input_str("color")
        selected_yarn.weight =  select_weight()
        selected_yarn.yds = input_int("number of yds per skein")
        selected_yarn.qty = input_int("total number of skeins")                    
        selected_yarn.update()
    else:
        clear_and_print("Yarn not found.")

def delete_yarn(yarn_to_delete):
    yarns = Yarn.get_all()
    sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
    selected_yarn = Yarn.find_by_id(sorted_yarns[yarn_to_delete - 1].id)

    if selected_yarn:
        selected_yarn.delete()
    else:
        clear_and_print("Yarn not found.")