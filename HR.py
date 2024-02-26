class HR:

    def __init__(self, employee3, task):
        self.employee = employee3
        self.task = task

    def recruitments(self):
        print(f"{self.employee.name} is handling {self.task}.")

    def filing(self):
        print(f"{self.employee.name} is handling {self.task}.")

    def generating_reports(self):
        print(f"{self.employee.name} is {self.task}.")

    def execution(self):
        if self.task == 'Recruitments':
            self.recruitments()
        elif self.task == 'Filing':
            self.filing()
        elif self.task == 'Generating Reports':
            self.generating_reports()
        else:
            print("Invalid")
