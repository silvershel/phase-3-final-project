# lib/helpers.py
import os
from models.project import Project
from models.yarn import Yarn

# Stash Helpers

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exit_program():
    clear_terminal()
    print("Your stash has been managed.")
    exit()

def list_yarn():
    clear_terminal()
    print()
    yarns = Yarn.get_all()
    for yarn in yarns:
        print(yarn)

def find_yarn_by_id():
    clear_terminal()
    print()
    print("Function to find yarn by ID")

def add_yarn():
    clear_terminal()
    print()
    brand = input("Enter the yarn brand: ")
    color = input("Enter the yarn color: ")
    weight = input("Enter the yarn weight: ")
    yds = int(input("Enter the yds in each skein: "))
    qty = int(input("Enter the total number of skeins: "))
    try:
        yarn = Yarn.create(brand, color, weight, yds, qty)
        print(f"New yarn added: {yarn}")
    except Exception as exc:
        print("Error adding new yarn", exc)

def update_yarn():
    clear_terminal()
    print()
    id_ = input("Enter the ID of the yarn you want to update: ")
    if yarn := Yarn.find_by_id(id_):
        try:
            brand = input("Enter the brand: ")
            yarn.brand = brand
            color = input("Enter the color: ")
            yarn.color = color
            weight = input("Enter the weight: ")
            yarn.weight = weight
            yds = int(input("Enter the yds per skein: "))
            yarn.yds = yds
            qty = int(input("Enter the qty: "))
            yarn.qty = qty
            clear_terminal()
            print(f"Success! {yarn}")
        except Exception as exc:
            print("Error updating yarn: ", exc)
    else:
        print(f"Yarn not found.")

def delete_yarn():
    clear_terminal()
    print()
    id_ = input("Enter the ID of the yarn you want to delete: ")
    if yarn := Yarn.find_by_id(id_):
        yarn.delete()
        print(f"Deleted: {yarn.brand} {yarn.weight}, {yarn.color}")
    else:
        print(f"Yarn not found")

# Project Helpers

def list_projects():
    clear_terminal()
    print("Function to list all projects")

def find_project_by_id():
    clear_terminal()
    print("Function to find project by ID")

def create_project():
    clear_terminal()
    print("Function to create a project")

def update_project():
    clear_terminal()
    print("Function to update a project")

def delete_project():
    clear_terminal()
    print("Function to delete a project")