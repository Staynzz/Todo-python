from task_module import *
from sqlite3 import *

TABLE_USER = "User"
TABLE_LISTTASK = "ListTask"
TABLE_TASK = "Task"

db = connect("datatodo.db")
db.cursor()
def request(command, *args, connection=db, rawoutput=False):
    cur = connection.cursor()
    output = cur.execute(command,args)
    connection.commit()
    if rawoutput:
        return output
    else:
        return tuple(output)

def add_user(name, password):
    req = f"INSERT INTO {TABLE_USER} ('Username', 'Password') VALUES (?,?)"
    return request(req,name,password)

def get_all_table(table):
    req = f"SELECT * FROM {table}"
    return request(req)

def get_user_byID(id):
    req = f"SELECT * FROM {TABLE_USER} WHERE ID = ? "
    return request(req,id)

def delete_user_byID(id):
    req = f"DELETE FROM {TABLE_USER} WHERE ID = ?"
    return request(req,id)

def update_user_byID(id,column,new_value):
    """
    Column Index:
        0: ID
        1: Username
        2: Password
    """
    
    column_index = {0:"ID",1:"Username",2:"Password"}
    req = f"UPDATE {TABLE_USER} SET {column_index[column]} = ? WHERE ID = ?"
    return request(req,new_value,id)

db.close()