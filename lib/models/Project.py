# lib/models/project.py
from models.__init__ import CURSOR, CONN

# TO DO
# Finalize attributes
# Save
# Update
# Delete
# Create
# Instance from DB
# List all
# Find by ID
# Find by weight
# List all projects
# Create a new project
# Update a project
# Delete a project

# STRETCH

class Project:

    all = {}
    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    # update to reflect attributes listed above
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS projects;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def create(cls):
        pass

    @classmethod
    def instance_from_db(cls):
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def find_by_id(cls):
        pass

    @classmethod
    def find_by_yarn_weight():
        pass