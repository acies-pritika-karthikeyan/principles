class Development:

   def __init__(self, employee1, product_details, task):
       self.employee = employee1
       self.product_details = product_details
       self.task = task

   def code_front_end(self):
       print(
           f"{self.employee.name} is coding the frontend of {self.product_details.product_name}. Product Status: {self.product_details.product_status}.")


   def code_back_end(self):
       print(
           f"{self.employee.name} is coding the backend of {self.product_details.product_name}. Product Status: {self.product_details.product_status}.")


   def execution(self):
       if self.task == 'backend':
           self.code_back_end()
       elif self.task == 'frontend':
           self.code_front_end()
       else:
           print("Invalid")
