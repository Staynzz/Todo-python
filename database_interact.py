from sqlite3 import *
from pathlib import Path

TABLE_USER = "User"
TABLE_LISTTASK = "ListTask"
TABLE_TASK = "Task"

def create_new_database(name:str,path_schema=Path("data/schema.txt")):
    if name[-3:] != ".db":
        name += ".db"   #Ajoute la bonne extension de fichier
    newdatabase = Path("data") / name
    if name == "datatodo.db" and Path("data/datatodo.db").exists():
        return "ERROR can't reset the original database"
    
    if not newdatabase.exists():
        newdatabase.touch() #
    else:
        with open(newdatabase,"w") as f:
            f.write()
            
    with open(path_schema,"r") as f:
                temp_db = connect(newdatabase)
                for line in f.readlines():
                    cur = temp_db.cursor()
                    cur.execute(line)
                    temp_db.commit()
                temp_db.close()

class Database:
    def __init__(self,path:Path):
        self.path = path
        if not path.exists():
            create_new_database(str(path).split("/")[-1])
        self.connection = connect(path)
        
    
    #PROPRIETY
    def get_path(self):
        return self.path

    def set_path(self,new_path):
        self.path = new_path
        self.connection.close()
        self.connection = connect(self.path)
        return True
    
    def get_connection(self):
        return self.connection
    
    def close_connection(self):
        self.connection.close()
        return True
    
    #REQUEST
    def request(self,command, *args, rawoutput=False):
        cur = self.connection.cursor()
        output = cur.execute(command,args)
        self.connection.commit()
        if rawoutput:
            return output
        else:
            return tuple(output)
        
class Table():
    """
    Argument column format:
        [("Name",(is_obligatory, is_unique, is_primary_key))] with is_... = Bool
    """
    
    def __init__(self,database: Database, name,column:list):
        self.database = database
        self.name = name
        self.column = column
        self.layout = {}
        for col in column:
            self.layout[col[0]] = col[1]
            if col[1][2] == True:
                self.primarykey = col[0]
            
            
    def get_all(self, raw=False):
        req = f"SELECT * FROM {self.name}"
        return self.database.request(req,rawoutput=raw)
    
    def get_element_byID(self,id):
        req = f"SELECT * FROM {self.name} WHERE {self.primarykey} = ?"
        return self.database.request(req,id)
    
    def add_element(self,prop:dict):
        req = f"INSERT INTO {self.name} ({", ".join(f"'{e}'" for e in prop.keys())}) VALUES ({("?," * len(prop.keys()))[:-1]})"
        print(req)
        return self.database.request(req,*prop.values())
    
    def edit_element_byID(self,id,update:dict):
        req = f"UPDATE {self.name} SET {", ".join(f"'{e}' = ?" for e in update.keys())} WHERE {self.primarykey} = ?"
        return self.database.request(req,*update.values(),id)
        
    def delete_element_byID(self,id):
        req = f"DELETE FROM {self.name} WHERE {self.primarykey} = ?"
        return self.database.request(req,id)

        

db = Database(Path("data/datatodo.db"))

userdb = Table(db,TABLE_USER,[("ID",(1,1,1)),
                              ("Username", (1,1,0)),
                              ("Password", (1,0,0))])

listdb = Table(db,TABLE_LISTTASK,[["ID",(1,1,1)],
                                  ["ID User",(1,0,0)],
                                  ["Name",(1,0,0)]])

taskdb = Table(db,TABLE_TASK,[["ID",(1,1,1)],
                              ["ID ListTask",(1,0,0)],
                              ["Name", (1,0,0)],
                              ["State", (1,0,0)]])

db.close_connection()