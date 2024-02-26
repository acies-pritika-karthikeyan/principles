from Employee import Employee

class HR(Employee):
   def __init__(self, name, age, salary, years_of_experience):
       super().__init__(name, age, salary)
       self.years_of_experience = years_of_experience

   def recruitment(self):
       print(f"{self.name} is handling recruitment.")

   def filing(self):
       print(f"{self.name} is handling filing.")

   def report_generate(self):
       print(f"{self.name} is generating reports.")