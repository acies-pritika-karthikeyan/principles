from Employee import Employee

class Analytics(Employee):
   def __init__(self, name, age, salary, project_name, project_stage):
       super().__init__(name, age, salary)
       self.project_name = project_name
       self.project_stage = project_stage

   def data_cleaning(self):
       print(f"{self.name} is cleaning data for {self.project_name}.")

   def do_eda(self):
       print(f"{self.name} is performing exploratory data analysis on {self.project_name}.")

   def perform_modelling(self):
       print(f"{self.name} is performing modeling on {self.project_name} data.")

   def do_predictions(self):
       print(f"{self.name} is making predictions for {self.project_name}.")