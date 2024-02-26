class Development:

   def __init__(self, employee, product_details):
       self.employee = employee
       self.product_details = product_details

   def code_front_end(self):
       print(
           f"{self.employee.name} is coding the frontend of {self.product_details.product_name}. Product Status: {self.product_details.product_status}.")

   def code_back_end(self):
       print(
           f"{self.employee.name} is coding the backend of {self.product_details.product_name}. Product Status: {self.product_details.product_status}.")

   def execution(self, typeOfProject):
       if typeOfProject == 'backend':
           self.code_back_end()
       else:
           self.code_front_end()