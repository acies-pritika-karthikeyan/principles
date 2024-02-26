class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def to_work(self):
        print(f"{self.name} is working.")

    def to_pitch(self):
        print(f"{self.name} is pitching.")

    def to_present(self):
        print(f"{self.name} is presenting.")


class Development(Employee):
    def __init__(self, name, age, salary, product_name, completion_status):
        super().__init__(name, age, salary)
        self.product_name = product_name
        self.completion_status = completion_status

    def code_frontend(self):
        print(f"{self.name} is coding frontend for {self.product_name}.")

    def code_backend(self):
        print(f"{self.name} is coding backend for {self.product_name}.")


class Analytics(Employee):
    def __init__(self, name, age, salary, project_name, project_stage):
        super().__init__(name, age, salary)
        self.project_name = project_name
        self.project_stage = project_stage

    def data_cleaning(self):
        print(f"{self.name} is cleaning data for {self.project_name}.")

    def do_EDA(self):
        print(f"{self.name} is performing EDA for {self.project_name}.")

    def perform_modelling(self):
        print(f"{self.name} is performing modeling for {self.project_name}.")

    def do_predictions(self):
        print(f"{self.name} is making predictions for {self.project_name}.")


class HR(Employee):
    def __init__(self, name, age, salary, years_of_experience):
        super().__init__(name, age, salary)
        self.years_of_experience = years_of_experience

    def recruitment(self):
        print(f"{self.name} is conducting recruitment.")

    def filing(self):
        print(f"{self.name} is filing documents.")

    def report_generation(self):
        print(f"{self.name} is generating reports.")

    def training(self):
        print(f"{self.name} is conducting training sessions.")


dev = Development("Pritika", 22, 13000,"edgeCore.ai", "In Progess")
ds = Analytics("Aryan", 21, 12000, "Bose", "Analysis Phase")
hr = HR("Subhash", 25, 10000, 1)

dev.to_work()
dev.code_backend()
ds.to_pitch()
ds.data_cleaning()
hr.to_present()
hr.report_generation()
   

