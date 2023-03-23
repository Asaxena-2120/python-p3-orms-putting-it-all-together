import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    def __init__(self,name,breed,id=None) -> None:
        self.id=id
        self.name=name
        self.breed=breed
    
    @classmethod
    def create_table(cls):
        sql="""
        CREATE TABLE dogs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
        )
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql="""
        DROP TABLE IF EXISTS dogs 
        """
        CURSOR.execute(sql)

    
    def save(self):
        sql="""
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)

        """
        CURSOR.execute(sql, (self.name,self.breed))
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls,name,breed):
        dog = cls(name,breed) # dog=Dog(name,breed)
        dog.save()
        return dog
    
    @classmethod
    def new_from_db(cls,row):
        dog = cls(
            name=row[1],
            breed=row[2],
            id=row[0]
        )
        return dog
    
    @classmethod
    def get_all(cls):
        sql="""
            SELECT * FROM dogs
        """
        data=[cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]
        return data
    @classmethod
    def find_by_name(cls,name):
        sql="""
            SELECT * FROM dogs
            WHERE name=?
            LIMIT 1
            
        """
        
        data=cls.new_from_db(CURSOR.execute(sql,(name,)).fetchone())
        if not data:
            return None
        return data
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
            SELECT * FROM dogs
            WHERE id=?
            LIMIT 1
        """
        data=cls.new_from_db(CURSOR.execute(sql,(id,)).fetchone())
        if not data:
            return None
        return data
    
    @classmethod
    def find_or_create_by(cls,name,breed):
        sql="""
            SELECT * FROM dogs
            WHERE dogs.name=?
            AND dogs.breed=?
            LIMIT 1
        """
        data=cls.new_from_db(CURSOR.execute(sql,(name,breed)).fetchone())
        if not data:
            
            return cls.create(name=name,breed=breed)
        return data
    @classmethod
    def find_or_create_by(cls,name,breed):
        sql="""
            SELECT * FROM dogs
            WHERE dogs.name=?
            AND dogs.breed=?
            LIMIT 1
        """
        data=(CURSOR.execute(sql,(name,breed)).fetchone())
        if not data:
            
            return cls.create(name=name,breed=breed)
        return cls.new_from_db(data)
    
    def update(self):
        sql = """
            UPDATE dogs
            SET name = ?,
                breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))



        


    

    
    
    
