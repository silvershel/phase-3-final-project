# lib/models/project.py
from models.__init__ import CURSOR, CONN

class Project:
    
    def __init__(self, name, id = None):
        self.id = id
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
        """ Create a new table to persist the attributes of Project instances """
        sql = """
            CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    # drop_table
    
    # save 
    # update 
    # delete 
    # create (new project instance)
    # instance_from_db (return project object from database)
        # needed for below
    # get_all (return list containing one project object per row)
    # find_by_id (return project object matching the specified id)
    # find_by_name (return project object matching the specified name)