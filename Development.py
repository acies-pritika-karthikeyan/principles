from Employee import Employee

class Development(Employee):
   def __init__(self, name, age, salary, product_name, product_status):
        super().__init__(name, age, salary)
        self.product_name = product_name
        self.product_status = product_status

   def code_front_end(self):
       print(f"{self.name} is coding the frontend of {self.product_name}.")


   def code_back_end(self):
       print(f"{self.name} is coding the backend of {self.product_name}.")