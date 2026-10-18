import tabulate

class Task:
    """
    !! Pour ajouter une propriété sur les tâches, bien penser à modifier la sequence des attributs, ainsi que dans le get_attributes !!
    """
    
    SEQUENCE = ["ID","List link","Name","Status"]
    
    def __init__(self,name,status="not done"):
        self.name = name
        self.status = status
        self.id = 0
        self.list_link = None
    
    #GETS
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_status(self):
        return self.status
    
    def get_list_link(self):
        return self.list_link
    
    def get_attribute(self):
        return (self.get_id(), self.get_list_link().get_name(),self.get_name(),self.get_status())
    
    #SETS
    def set_id(self,id: int):
        self.id = id
        
    def set_list_link(self,list: ListTask):
        self.list_link = list
        
    #OTHERS
    def done(self):
        self.status = "done"
    
    def undone(self):
        self.status = "not done"
        
    def show_attribute(self):
        print(tabulate.tabulate([Task.SEQUENCE,self.get_attribute()]))
        
class ListTask:
    def __init__(self,name):
        self.name = name
        self.tasks = []
        
    #GETS
    def get_name(self):
        return self.name

    def get_tasks(self):
        return self.tasks
    
    def get_task_by_id(self,id):
        return self.tasks[id]
    
    #OTHERS
    def add_tasks(self,task: Task):
        self.tasks.append(task)
        task.set_id(self.tasks.index(task))
        task.set_list_link(self)
        
    def show_all_task(self):
        tab = [Task.SEQUENCE]
        for task in self.tasks:
           tab.append(task.get_attribute())
        print(tabulate.tabulate(tab))
    