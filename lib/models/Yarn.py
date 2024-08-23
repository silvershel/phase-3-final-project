# lib/models/yarn.py
from models.__init__ import CURSOR, CONN
from models.project import Project

# TO DO
# specify yarn weights to search by toLowerCase (lace, sock, DK, worsted, aran, bulky)

# STRETCH Delete number of skeins only?
# Add yarn with same details to existing entries?
# If string, make search toLowerCase 

class Yarn:
    
    all = {}

    def __init__(self, brand, color, weight, yds, qty):
        self.brand = brand.title()
        self.color = color.title()
        self.weight = weight.title()
        self.yds = yds
        self.qty = qty

    def __repr__(self):
        return f"{self.id}: Brand = {self.brand}, Color = {self.color}, Weight = {self.weight}, Yds = {self.yds}, Qty = {self.qty}"

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and len(brand):
            self._brand = brand.title()
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str) and len(color):
            self._color = color.title()
        else:
            raise ValueError("Color must be a non-empty string.")

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if type(weight) is str:
            self._weight = weight.title()
        else:
            raise ValueError("Weight must be a string.")

    @property
    def yds(self):
        return self._yds
    
    @yds.setter
    def yds(self, yds):
        if type(yds) is int:
            self._yds = yds
        else:
            raise ValueError("Yards must be an integer.")

    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, qty):
        if type(qty) is int:
            self._qty = qty
        else:
            raise ValueError("Quantity must be an integer.")
    
    @classmethod
    def table_exists(cls):
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='yarns';"
        return CURSOR.execute(sql).fetchone() is not None

    @classmethod
    def create_table(cls):
        if not cls.table_exists():
            sql = """
                CREATE TABLE IF NOT EXISTS yarns (
                id INTEGER PRIMARY KEY,
                brand TEXT,
                color TEXT,
                weight TEXT,
                yds INTEGER,
                qty INTEGER)
            """
            CURSOR.execute(sql)
            CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS yarns;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        Yarn.create_table()

        sql = """
            INSERT INTO yarns (brand, color, weight, yds, qty)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.brand, self.color, self.weight, self.yds, self.qty))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    def update(self):
        sql = """
            UPDATE yarns
            SET brand = ?, color = ?, weight = ?, yds = ?, qty = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand, self.color,
                             self.yds, self.qty, self.id))
        CONN.commit()
        
    def delete(self):       
        sql = """
            DELETE FROM yarns
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, brand, color, weight, yds, qty):
        yarn = cls(brand, color, weight, yds, qty)
        yarn.save()
        return yarn
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        yarn = cls.all.get(row[0])
        if yarn:
            # ensure attributes match row values in case local instance was modified
            yarn.brand = row[1]
            yarn.color = row[2]
            yarn.weight = row[3]
            yarn.yds = row[4]
            yarn.qty = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            yarn = cls(row[1], row[2], row[3], row[4], row[5])
            yarn.id = row[0]
            cls.all[yarn.id] = yarn
        return yarn
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM yarns
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM yarns
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_brand(cls, brand):
        sql = """
            SELECT *
            FROM yarns
            WHERE brand is ?
        """

        row = CURSOR.execute(sql, (brand,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_color(cls, color):
        sql = """
            SELECT *
            FROM yarns
            WHERE color is ?
        """

        row = CURSOR.execute(sql, (color,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_weight(cls, weight):
        sql = """
            SELECT *
            FROM yarns
            WHERE weight is ?
        """

        row = CURSOR.execute(sql, (weight,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_yds_range(cls, yds_min, yds_max):
        sql = """
            SELECT *
            FROM yarns
            WHERE (yds * qty) BETWEEN ? AND ?
        """

        rows = CURSOR.execute(sql, (yds_min, yds_max)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []


