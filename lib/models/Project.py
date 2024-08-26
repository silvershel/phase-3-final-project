# lib/models/project.py
from models.__init__ import CURSOR, CONN

class Project:

    all = {}
    
    def __init__(self, pattern, type, size, weight, yds_needed):
        self.pattern = pattern.title()
        self.type = type.title()
        self.size = size
        self.weight = weight.title()
        self.yds_needed = yds_needed

    def __repr__(self):
        return f"Pattern: {self.pattern}\nType: {self.type}\nSize: {self.size}\nWeight: {self.weight}\nYds Needed: {self.yds_needed}\nID: {self.id}\n"

    @property
    def pattern(self):
        return self._pattern
    
    @pattern.setter
    def pattern(self, pattern):
        if isinstance(pattern, str) and len(pattern):
            self._pattern = pattern.title()
        else:
            raise ValueError("Pattern name must be a non-empty string.")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type) > 0:
            self._type = type.title()

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, str) and len(size) > 0:
            self._size = size

    @property
    def weight(self):
        return self._weight
    
    @size.setter
    def weight(self, weight):
        if isinstance(weight, str) and len(weight) > 0:
            self._weight = weight

    @property
    def yds_needed(self):
        return self._yds_needed
    
    @yds_needed.setter
    def yds_needed(self, yds_needed):
        if type(yds_needed) is int:
            self._yds_needed = yds_needed
    
    @classmethod
    def table_exists(cls):
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='projects';"
        return CURSOR.execute(sql).fetchone() is not None

    @classmethod
    def create_table(cls):
        if not cls.table_exists():
            sql = """
                CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                pattern TEXT,
                type TEXT,
                size TEXT,
                weight TEXT,
                yds_needed INTEGER)
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
        Project.create_table()
        sql = """
            INSERT INTO projects (pattern, type, size, weight, yds_needed)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.pattern, self.type, self.size, self.weight, self.yds_needed))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE projects
            SET pattern = ?, type = ?, size = ?, weight = ?, yds_needed = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.pattern, self.type, self.size, self.weight, self.yds_needed, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM projects
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, pattern, type, size, weight, yds_needed):
        project = cls(pattern, type, size, weight, yds_needed)
        project.save()
        return project

    @classmethod
    def instance_from_db(cls, row):
        project = cls.all.get(row[0])
        if project:
            project.pattern = row[1]
            project.type = row[2]
            project.size = row[3]
            project.weight = row[4]
            project.yds_needed = row[5]
        else:
            project = cls(row[1], row[2], row[3], row[4], row[5])
            project.id = row[0]
            cls.all[project.id] = project
        return project

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM projects
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM projects
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_yarn_weight(cls, weight):
        sql = """
            SELECT *
            FROM projects
            WHERE weight is ?
        """
        row = CURSOR.execute(sql, (weight,)).fetchone()
        return cls.instance_from_db(row) if row else None