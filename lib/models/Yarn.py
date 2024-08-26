# lib/models/yarn.py
from models.__init__ import CURSOR, CONN
from models.project import Project

class Yarn:
    
    all = {}

    def __init__(self, brand, base, color, weight, yds, qty):
        self.brand = brand.title()
        self.base = base.title()
        self.color = color.title()
        self.weight = weight.title()
        self.yds = yds
        self.qty = qty

    def __repr__(self):
        return f"Brand: {self.brand}\nBase: {self.base}\nColor: {self.color}\nWeight: {self.weight}\nYds: {self.yds}\nQty: {self.qty}\nID: {self.id}\n"

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and len(brand) > 0:
            self._brand = brand.title()
        else:
            raise ValueError("Brand must be a non-empty string.")
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if isinstance(base, str) and len(base) > 0:
            self._base = base.title()
        else:
            raise ValueError("Base must be a non-empty string.")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str) and len(color) > 0:
            self._color = color.title()
        else:
            raise ValueError("Color must be a non-empty string.")

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if type(weight) is str and len(weight) > 0:
            self._weight = weight.title()
        else:
            raise ValueError("Weight must be a non-empty string.")

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
                base TEXT,
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
            INSERT INTO yarns (brand, base, color, weight, yds, qty)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.brand, self.base, self.color, self.weight, self.yds, self.qty))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    def update(self):
        sql = """
            UPDATE yarns
            SET brand = ?, product = ?, color = ?, weight = ?, yds = ?, qty = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand, self.product, self.color,
                             self.weight, self.yds, self.qty, self.id))
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
    def create(cls, brand, product, color, weight, yds, qty):
        yarn = cls(brand, product, color, weight, yds, qty)
        yarn.save()
        return yarn
    
    @classmethod
    def instance_from_db(cls, row):
        yarn = cls.all.get(row[0])
        if yarn:
            yarn.brand = row[1]
            yarn.product = row[2]
            yarn.color = row[3]
            yarn.weight = row[4]
            yarn.yds = row[5]
            yarn.qty = row[6]
        else:
            yarn = cls(row[1], row[2], row[3], row[4], row[5], row[6])
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


