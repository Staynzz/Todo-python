from task_module import *

run = True
list_ListTask = [ListTask("Liste1")]
select_ListTask = None

def show_ListTask(liste:list):  #Affiche toutes les listes de tâches avec leurs indexs pour l'utilisateurs
    for element in liste:
        print(f"{liste.index(element)} : {element.get_name()}")

command = ""

while run:
    
    if select_ListTask == None:
        print("\n1) Select ListTask \n"
              "2) Create ListTask \n"
              "3) Edit ListTask \n"
              "4) Delete ListTask \n")
              
           
        command = input(">>")
        if command == "1":  #SELECTION
            show_ListTask(list_ListTask)

            print("Entrer le numéro de la liste de tâche à séléctionner")
            liste_choice = input(">>")
            if liste_choice.isdigit():
                select_ListTask = list_ListTask[int(liste_choice)]
            
        elif command == "2":  #CREATION
            print("Entrer le nom de la nouvelle liste")
            name_choice = input(">>")
            if name_choice != "":
                list_ListTask.append(ListTask(name_choice))
        
        elif command == "3":
            show_ListTask(list_ListTask)
            
            print("Entrer le numéro de la liste de tâche à renommer")
            liste_choice = input(">>")
            print("Entrer le nouveau nom de cette liste")
            name_choice = input(">>")
            
            list_ListTask[int(liste_choice)].set_name(name_choice)
            
        elif command == "4":
            show_ListTask(list_ListTask)
            
            print("Entrer le numéro de la liste à supprimer")
            liste_choice = input(">>")
            if liste_choice.isdigit():
                del list_ListTask[int(liste_choice)]
            
    else:
        command = input(f"{select_ListTask.get_name()}/>>")
        
    if command == "exit":
        run = False
    
    
