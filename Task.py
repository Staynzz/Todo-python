class Task:
    def __init__(self,name,status):
        self.name = name
        self.status = status
        
    def get_name(self):
        return self.name
    
    def get_status(self):
        return self.status
    
    def done(self):
        self.status = "done"
    
    def undone(self):
        self.status = "not done"