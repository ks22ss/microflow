class TaskGroup():
    def __init__(self):
        print("------------------")
        print("1. task initialize")
        pass

    def extract(self):
        print("2. extract")
        return self
    
    def transform_A(self):
        print("3A. transform A")
        return self

    def transform_B(self):
        print("3B. transform B")
        return self
        
    def transform_C(self):
        print("3C. transform C")
        return self

    def load(self):
        print("4. load")
        return self

'''
# Workflow Example
wf = Workflow()
wf.extract().transform_A().load()

wf = Workflow()
wf.extract().transform_B().transform_A().transform_C().load()

wf = Workflow()
wf.extract().transform_A().transform_B().transform_C().load()
'''

class Workflow():
    def __init__(self, task_group):
        self.task_group = task_group
    
    def run_workflow_X(self):
        self.task_group.extract().transform_A().load()

    def run_workflow_Y(self):
        self.task_group.extract().transform_B().transform_A().transform_C().load()

    def run_workflow_Z(self):
        self.task_group.extract().load()
