# STASH MANAGER
### This CLI keeps track of a user's personal yarn stash and related projects by allowing the user to input important details for each yarn or project.

## CLI MENU (cli.py)
Organizes the CLI menu and navigates to each category/task based on user inputs. Menus (as visible to the user) are shown below:

### Main Menu
```
STASH MANAGER

1. Yarn
2. Projects

EXIT to exit

> 
```

### Yarn Menu
```
YARN

1. List all yarn
2. Find yarn by brand
3. Find yarn by weight
4: Add yarn
5: Update yarn
6: Delete yarn

EXIT to exit | MAIN for Main Menu

> 
```

### Projects Menu
```
PROJECTS

1. List all projects
2. Find projects by category
3. Find projects by yarn weight
4: Add a project
5: Update a project
6: Delete a project

EXIT to exit | MAIN for Main Menu

> 
```


## YARN CLASS (yarn.py)
This class includes methods that allow the user to add, update, and delete a yarn and places the corresponding data into a table. Each table includes colums for important details including the yarn brand, base, color, weight, yards per skein (yds), and total number of skeins (qty).


## PROJECT CLASS (project.py)
This class includes methods that allow the user to add, update, and delete a project and places the corresponding data into a table. Each table includes colums for important details including the pattern name (pattern), category, size being made (size), yarn weight (weight), and total yards needed (yds_needed).

## HELPER FUNCTIONS (helpers.py)

### Cleanup Functions
Used to simplify code blocks, check inputs, and prompt user with instructions. 

```clear_terminal(), clear_and_print(), print_with_return()```
Various clear and print functions to maintain a clean user experience.

```input_str(), input_int()``` Checks inputs for correct data types.

```check_brand()```
Checks the input for a match based on brands listed in the database.

```check_category()```
Checks the input for a match based on a list of of pre-determined categories.

```check_weight()```
Checks the input for a match based on a list of of pre-determined yarn weights.

```exit_program()```
Exits the program. 

### Yarn Functions
Functions related specifically to the Yarn class.

```list_yarn()```
Lists all yarn in the database alphebetically by brand. 

```find_yarn_by_brand(), find_yarn_by_weight()```
Based on user input, finds and prints every yarn in the database that matches each function's specific criteria (brand or weight). Example:

```
ALL YARN (alphabetical by brand)

De Rerum Natura, Dilliatt
Color: Tempete | Weight: Dk | Yds: 273 | Qty: 5
ID: 1
Being used for: 4 Letter Sweater.

De Rerum Natura, Gilliatt
Color: Caramel | Weight: Worsted | Yds: 273 | Qty: 1
ID: 3
Being used for: 4 Letter Sweater.

Spincycle, Metamorphic
Color: Marl No. 29 | Weight: Dk | Yds: 400 | Qty: 3
ID: 2

Scroll up to view.

----- 

YARN

1. List all yarn
2. Find yarn by brand
3. Find yarn by weight
4: Add yarn
5: Update yarn
6: Delete yarn

EXIT to exit | MAIN for Main Menu

> 
```

```add_yarn()```
Allows the user to add a new yarn to the database and assigns important details including: brand, base, color, weight, yds, and qty.

```update_yarn()```
Allows the user to update the data for a specific yarn including: brand, base, color, weight, yds, qty, and (if applicable) a related project id.

```delete_yarn()```
Allows the user to manually delete a specific yarn.

### Project Functions
Functions related specifically to the Project class. 

```list_projects()```
Lists all projects in the database alphebetically by pattern name. 

```find_project_by_category(), find_project_by_weight()```
Based on user input, finds and prints every project in the database that matches each function's specific criteria (category or weight).

```add_project()```
Allows the user to add a new project to the database and assigns important details including: pattern, category, size, weight, and yards needed. The user can also look for and assign the project id to yarns in their stash to mark for use.

```update_project()```
Allows the user to update the data for a specific project including: pattern, category, size, weight, and yards needed.

```delete_project()```
Allows the user to manually delete a specific project.


## License

[Link](https://choosealicense.com/licenses/mit/)