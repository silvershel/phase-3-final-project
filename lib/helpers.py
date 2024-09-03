# lib/helpers.py

import os
from models.project import Project
from models.yarn import Yarn

# GENERAL TO DO
    # Reformat cli.py to match displayed menu.
    # Make sure headings are consistent.
        # List yarn by brand, no header
        # List yarn by weight, no header
        # Update yarn, no header
        # Delete yarn, no header
    # Make sure indexing is consisten (pick numbers or letters, not both.)

# PROJECT MENU TO DO
# Fix clearing issues for adding yarn to a project (just clears and shows menu again)
# Fix selecting wrong number from adding a yarn (just clears and shows menu again)
# Fix selecting wrong number from removing a yarn (error exits out of program)

# YARN MENU TO DO
# Fix delete yarn
    # non-integer exits program.
    # wrong intger shows "not a valid option" so just make sure language is consistent.
    # Stay on same page to keep deleting until user selects goes back.
# Fix update yarn (same issues as above)
# Fix add yarn

# STRETCH GOALS
# Be able to skip input fields.
# Be able to exit out of input fields.
# Mark yarn as unavailable if in use by another project.
# PROJECT, Add find by designer
# YARN, Add color_family
# YARN, Add find_by_color_family
# Build out needles and tools section

# CLEANUP FUNCTIONS
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
            clear_and_print("Please enter a valid option.")

def select_category():
    while True:
        valid_categories = Project.VALID_CATEGORIES
        
        for i, weight in enumerate(valid_categories, start=1):
            print(f"{i}. {weight}")

        user_input = input("Enter the category: ")
        
        if user_input.isdigit() and 1 <= int(user_input) <= len(valid_categories):
            return valid_categories[int(user_input) - 1]
        else:
            clear_and_print("Please enter a valid option.")

def select_weight():
    while True:
        valid_weights = Yarn.VALID_WEIGHTS
        
        for i, weight in enumerate(valid_weights, start=1):
            print(f"{i}. {weight}")

        user_input = input("Enter the weight: ")
        
        if user_input.isdigit() and 1 <= int(user_input) <= len(valid_weights):
            return valid_weights[int(user_input) - 1]
        else:
            clear_and_print("Please enter a valid option.")
                
def exit_program():
    clear_and_print("Your stash has been managed. Goodbye.")
    exit()

# PROJECT FUNCTIONS
def list_all_projects():
    projects = Project.get_all()
    if projects:
        sorted_projects = sorted(projects, key=lambda project: project.pattern)
        for i, project in enumerate(sorted_projects, start=1):
            print_with_return(f"{i}. {project.pattern}")
    else:
        print_with_return("No projects in database.")

def list_one_project(user_input):
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.project_id == selected_project.id]
    
    if 1 <= user_input <= len(projects):
        if not matching_yarns:
            print(f"{selected_project.pattern}\nDesigner: {selected_project.designer}\nCategory: {selected_project.category}\nSize: {selected_project.size}\nWeight: {selected_project.weight}\nYds Needed: {selected_project.yds_needed}\n")
        else: 
            print(f"{selected_project.pattern}\nDesigner: {selected_project.designer}\nCategory: {selected_project.category}\nSize: {selected_project.size}\nWeight: {selected_project.weight}\nYds Needed: {selected_project.yds_needed}\n")
            print("YARNS USING:")
            for yarn in matching_yarns:
                print(f"{yarn.brand} {yarn.base}, {yarn.color}")
            print()
    else:
        clear_and_print("Project not found.")

def add_project():
    clear_terminal()
    pattern = input_str("pattern name")
    designer = input_str("designer")
    category = select_category()
    size = input_str("size being made")
    weight =  select_weight()
    yds_needed = input_int("yds needed")

    try:
        Project.create(pattern, designer, category, size, weight, yds_needed)
        clear_terminal()

    except Exception as exc:
        clear_and_print("Error adding new project: ", exc)

def update_project(user_input):
    clear_terminal()
    projects = Project.get_all()
    sorted_projects = sorted(projects, key=lambda project: project.pattern)
    selected_project = Project.find_by_id(sorted_projects[user_input - 1].id)
    
    if selected_project in projects:
        clear_terminal()
        selected_project.pattern = input_str("pattern name")
        selected_project.designer = input_str("designer")
        selected_project.category = select_category()
        selected_project.size = input_str("size being made")
        selected_project.weight =  select_weight()
        selected_project.yds_needed = input_int("yds needed")                  
        selected_project.update()
        clear_terminal()
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
        clear_terminal()
    else:
        print("cannot delete. project not here.")

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
        print("yarn deleted")
    

# YARN FUNCTIONS        
def list_yarn():
    clear_and_print("ALL YARN")
    yarns = Yarn.get_all()
    if yarns:
        sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
        for i, yarn in enumerate(sorted_yarns, start=1):
            print(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}\n")
        print_with_return("Scroll up to view.")
    else:
        print_with_return("No yarn in stash.")

def list_yarn_used(user_input):
    clear_and_print("USED YARN")
    projects = Project.get_all()
    selected_project = Project.find_by_id(projects[user_input - 1].id)

    yarns = Yarn.get_all()
    used_yarns = [yarn for yarn in yarns if yarn.project_id == selected_project.id]

    if used_yarns:
        for i, yarn in enumerate(used_yarns, start=1):
            print_with_return(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}")
    else:
        print_with_return("No yarn being used.")

# def list_yarn_not_used(user_input):
#     clear_and_print("AVAILABLE YARN")
#     projects = Project.get_all()
#     selected_project = Project.find_by_id(projects[user_input - 1].id)

#     yarns = Yarn.get_all()
#     used_yarns = [yarn for yarn in yarns if yarn.project_id == None]

#     if used_yarns:
#         for i, yarn in enumerate(used_yarns, start=1):
#             print_with_return(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}")
#     else:
#         print_with_return("No yarn being used.")

def list_yarn_by_brand():
    clear_terminal()
    brand = select_brand()
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.brand.lower() == brand.lower()]
    
    if matching_yarns:
        clear_terminal()
        for i, yarn in enumerate(matching_yarns, start=1):
            print(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}\n")
        print_with_return("Scroll up to view.")
    else:
        clear_and_print(f"Brand not found.")

def list_yarn_by_weight():
    clear_terminal()
    weight =  select_weight()
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.weight == weight]

    if matching_yarns:
        clear_terminal()
        sorted_yarns = sorted(matching_yarns, key=lambda yarn: yarn.brand)
        for i, yarn in enumerate(sorted_yarns, start=1):
            print(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}\n")
        print_with_return("Scroll up to view.")
    else:
        clear_and_print(f"No {weight} weight yarn in stash.")

def add_yarn():
    clear_terminal()
    brand = input_str("brand")
    base = input_str("base")
    color = input_str("color")
    weight =  select_weight()
    yds = input_int("number of yds per skein")
    qty = input_int("total number of skeins")
    project_id = None

    try:
        yarn = Yarn.create(brand, base, color, weight, yds, qty, project_id)
        clear_and_print(f"{yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}", "Scroll up to view.")

    except Exception as exc:
        clear_and_print("Error adding new yarn: ", exc)
    
def update_yarn():
    clear_terminal()
    yarns = Yarn.get_all()
    sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
    enumerated_yarns = {}

    for i, yarn in enumerate(sorted_yarns, start=1):
        print(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}\n")
        enumerated_yarns[i] = yarn

    user_input = int(input("Enter the number of the yarn you want to update: "))

    if user_input in enumerated_yarns:
        clear_terminal()
        selected_yarn = Yarn.find_by_id(enumerated_yarns[user_input].id)
        selected_yarn.brand = input_str("brand")
        selected_yarn.base = input_str("base")
        selected_yarn.color = input_str("color")
        selected_yarn.weight =  select_weight()
        selected_yarn.yds = input_int("number of yds per skein")
        selected_yarn.qty = input_int("total number of skeins")                    
        selected_yarn.update()
        clear_and_print(f"{selected_yarn.brand}, {selected_yarn.base}\nColor: {selected_yarn.color} | Weight: {selected_yarn.weight} | Yds: {selected_yarn.yds} | Qty: {selected_yarn.qty}", "Scroll up to view.")
    else:
        clear_and_print("Yarn not found.")

def delete_yarn():
    clear_terminal()
    yarns = Yarn.get_all()
    sorted_yarns = sorted(yarns, key=lambda yarn: yarn.brand)
    enumerated_yarns = {}

    for i, yarn in enumerate(sorted_yarns, start=1):
        print(f"{i}. {yarn.brand}, {yarn.base}\nColor: {yarn.color} | Weight: {yarn.weight} | Yds: {yarn.yds} | Qty: {yarn.qty}\n")
        enumerated_yarns[i] = yarn

    user_input = int(input("Enter the number of the yarn you want to delete: "))

    if user_input in enumerated_yarns:
        selected_yarn = Yarn.find_by_id(enumerated_yarns[user_input].id)
        clear_and_print("Yarn deleted:", f"{selected_yarn.brand}, {selected_yarn.base}\nColor: {selected_yarn.color} | Weight: {selected_yarn.weight} | Yds: {selected_yarn.yds} | Qty: {selected_yarn.qty}")
        selected_yarn.delete()
    else:
        clear_and_print("Not a valid option.")