from HR import HR

class Training(HR):
   def __init__(self, name, age, salary, years_of_experience, topic):
       super().__init__(name, age, salary, years_of_experience)
       self.topic = topic

   def train_skill(self):
       print(f"{self.name} is tracking {self.topic} training.")