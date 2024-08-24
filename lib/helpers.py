# lib/helpers.py
import os
from models.project import Project
from models.yarn import Yarn

# STASH FUNCTIONS
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit_program():
    clear_terminal()
    print("Your stash has been managed. Goodbye.")
    exit()

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
        print("No yarn in database.\n")

def find_yarn_by_id():
    clear_terminal()
    id_ = input("Enter the yarn ID: ")
    if yarn := Yarn.find_by_id(id_):
        clear_terminal()
        print(f"{yarn}\nScroll up to view.\n")
    else:
        clear_terminal()
        print("Yarn not found.\n")

def find_yarn_by_weight():
    clear_terminal()
    weight = input("Enter the yarn weight: ")
    yarns = Yarn.get_all()
    matching_yarns = [yarn for yarn in yarns if yarn.weight.lower() == weight.lower()]
    if matching_yarns:
        for yarn in matching_yarns:
            print(yarn)
        print("Scroll up to view.\n")
    else:
        clear_terminal()
        print("Yarn not found.\n")

def get_valid_weight():
    valid_weights = ["lace", "sock", "sport", "dk", "worsted", "aran", "bulky"]
    
    while True:
        weight = input("Enter the yarn weight: ").lower()
        if weight in valid_weights:
            return weight
        else:
            print("Invalid weight. Please enter one of the following: lace, sock, sport, DK, worsted, aran, or bulky.")

def add_yarn():
    clear_terminal()
    brand = input("Enter the yarn brand: ")
    product = input("Enter the product name: ")
    color = input("Enter the yarn color: ")
    weight = get_valid_weight()
    yds = int(input("Enter the number of yds in each skein: "))
    qty = int(input("Enter the total number of skeins: "))
    try:
        yarn = Yarn.create(brand, product, color, weight, yds, qty)
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
            product = input("Enter the product name: ")
            yarn.product = product
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
    print("Function to list all projects")

def find_project_by_id():
    clear_terminal()
    print("Function to find project by ID")

def create_project():
    clear_terminal()
    print("Function to start a project")

def update_project():
    clear_terminal()
    print("Function to update a project")

def delete_project():
    clear_terminal()
    print("Function to delete a project")