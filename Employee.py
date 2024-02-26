class Employee:
   def __init__(self, name, age, salary):
       self.name = name
       self.age = age
       self.salary = salary

   def to_work(self):
       print(f"{self.name} is working.")

   def to_pitch(self):
       print(f"{self.name} is pitching.")

   def to_type(self):
       print(f"{self.name} is typing.")

   def to_present(self):
       print(f"{self.name} is presenting.")
