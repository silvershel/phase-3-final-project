# STASH MANAGER
### This CLI keeps track of a user's knitting projects and yarn stash by allowing the user to input important details for each project and/or yarn.

## MENUS

### Main Menu
The main menu displays the three main components that make up a knitter's stash: projects, yarn, and needles. Currently this program is only built to handle projects and yarn, but the ability to add needles (and other tools) will be added in the future.
```
STASH MANAGER

1. Projects
2. Yarn
3. Needles (coming soon)

E to Exit

> 
```

### Main Menu > Projects Menu
The projects menu displays all of the user's current projects. From this menu, the user can enter any number to view, edit, or delete that project, or enter "A" to add a new project to the list.
```
ALL PROJECTS

1. 4 Letter Sweater

2. Shifty Sweater

-----

Enter the project number to view details, edit, or delete.
Type A to add a project.

B go Back | E to Exit

> 
```

### Main Menu > Projects Menu > Project Details
When the user selects a project, the details of that project are displayed along with any yarn being used for that project. From there the user can carry out the tasks mentioned previously including adding yarn, removing yarn, updating that project's details, or deleting the project.
```
PROJECT DETAILS

4 Letter Sweater
Designer: Degen
Category: Garment
Size: Small
Weight: Worsted
Yds Needed: 1200

YARNS USING:
De Rerum Natura Gilliatt, Tempete
De Rerum Natura Gilliatt, Caramel

-----

Type A to add yarn to project.
Type R to remove yarn from project.
Type U to update details.
Type D to delete.

B go Back | E to Exit

>  
```
### Main Menu > Projects Menu > Project Details > Add Yarn
When the user selects "A" to add yarn, all yarn will be listed. The user can enter any number from this list to add that yarn to the project.
```
ALL YARN

1. De Rerum Natura, Gilliatt
Color: Tempete | Weight: Worsted | Yds: 273 | Qty: 5

2. De Rerum Natura, Gilliatt
Color: Caramel | Weight: Worsted | Yds: 273 | Qty: 1

3. De Rerum Natura, Gilliatt
Color: Genet | Weight: Worsted | Yds: 273 | Qty: 2

4. De Rerum Natura, Gillatt
Color: Bouleau | Weight: Worsted | Yds: 273 | Qty: 1

5. De Rerum Natura, Gilliatt
Color: Sel | Weight: Worsted | Yds: 273 | Qty: 1

6. Farmer's Daughter Fibers, Pishkun
Color: Ranch Romance | Weight: DK | Yds: 250 | Qty: 3

7. Spincycle, Metamorphic
Color: Marl No. 29 | Weight: DK | Yds: 400 | Qty: 3

8. Spincycle, Dyed In The Wool
Color: Mississippi Marsala | Weight: Sport | Yds: 200 | Qty: 2

9. Spincycle, Dyed In The Wool
Color: Wololo | Weight: Sport | Yds: 200 | Qty: 2

Scroll up to view.

-----

Enter the yarn number to select.
B go Back | E to Exit

> 
```
### Main Menu > Projects Menu > Project Details > Remove Yarn
When the user selects "R" to remove yarn, only the yarn being used for that project will be listed. The user can select any number from this list to remove that yarn.
```
USED YARN

1. De Rerum Natura, Gilliatt
Color: Tempete | Weight: Worsted | Yds: 273 | Qty: 5

2. De Rerum Natura, Gilliatt
Color: Caramel | Weight: Worsted | Yds: 273 | Qty: 1

-----

Enter the yarn number to select.
B go Back | E to Exit

> 
```
### Main Menu > Projects Menu > Add Project
### Main Menu > Projects Menu > Project Details > Update Details
Whether adding a project or updating the details for a project, the user will be prompted to fill out a field for each project detail. The "category" and "yarn weight" fields are limited by specific selections, the other fields are open to any input to maintain flexibility for the user. After completing all fields, the user will be taken back to view the project details.
```
Enter the pattern name: Pattern Name
Enter the designer: Designer Name
1. Garment
2. Accessory
3. Other
Enter the category: 1
Enter the size being made: Medium
1. Lace
2. Sock
3. Sport
4. DK
5. Worsted
6. Aran
7. Bulky
Enter the weight: 5
Enter the yds needed: 1200

>  
```
### Main Menu > Projects Menu > Project Details > Delete
When the user selects "D" to delete a project, that project will be deleted from the database. The user will be brought back to the main list of projects showing that the project has been deleted.
```
ALL PROJECTS

1. 4 Letter Sweater

-----

Enter the project number to view details, edit, or delete.
Type A to add a project.

B go Back | E to Exit

> 
```
### Yarn Menu
From the yarn menu, the user can select a corresponding number to list all yarn, list yarn by brand, list yarn by weight, add yarn, update yarn, or delete yarn. The yarn lists and prompts to add or update yarn appear in the same format as in the project editor.
```
YARN

1. List all yarn
2. List yarn by brand
3. List yarn by weight
4: Add yarn
5: Update yarn
6: Delete yarn

B go Back | E to Exit

>  
```