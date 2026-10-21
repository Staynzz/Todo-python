import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("PyTask")
app.geometry("820x460")

style = ttk.Style(app)
style.theme_use("clam")

Taskside = tk.Frame(app,padx=10,pady=10)
Actionside = tk.Frame(app,padx=10,pady=10)

#Taskside -->
ListTask_management = tk.Frame(Taskside)

#Actionside -->
Userside = tk.Frame(Actionside)
Buttonside = tk.Frame(Actionside)

#Actionside --> Buttonside -->
Positive_action = tk.Frame(Buttonside)
Negative_action = tk.Frame(Buttonside)

#Actionside -->
Account_management = tk.Frame(Actionside)

#Widget

#TASKSIDE =>
list_choice = ttk.Combobox(ListTask_management,width=30)
list_choice.pack(side=tk.LEFT,ipady=5,padx=5,pady=5)

manage_list_button = ttk.Button(ListTask_management,text="Gérer",width=12)
manage_list_button.pack(side=tk.RIGHT,padx=5,pady=5)

Tasklist = ttk.Treeview(Taskside,height=18,columns=["Nom","Date de fin","Statut"],show="headings")
Tasklist.heading("Nom", text="Nom")
Tasklist.heading("Date de fin", text="Date de fin")
Tasklist.heading("Statut", text="Statut")

Tasklist.column("Nom",width=200)
Tasklist.column("Date de fin",width=150)
Tasklist.column("Statut",width=100)


Tasklist.pack(side=tk.BOTTOM,pady=20)





#Packaging
Positive_action.pack()
Negative_action.pack()

ListTask_management.pack()

Userside.pack()
Buttonside.pack()
Account_management.pack()

Taskside.pack(side=tk.LEFT,padx=10)
Actionside.pack(side=tk.RIGHT,padx=10)

app.mainloop()