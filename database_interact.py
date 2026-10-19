from task_module import *
from sqlite3 import *

db = connect("datatodo.db")

def add_user(name, password):
    req = "INSERT INTO User ('Username', 'Password') VALUES (?,?)"
    cur = db.cursor()
    result = cur.execute(req,(name,password))
    db.commit()
    return result
