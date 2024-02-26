from abc import ABC, abstractmethod

class Developer(ABC):
    @abstractmethod
    def code(self):
        pass

class FrontendDeveloper(Developer):
    def code(self):
        print("Frontend developer is coding.")

class BackendDeveloper(Developer):
    def code(self):
        print("Backend developer is coding.")

class Product:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class Technology(ABC):
    @abstractmethod
    def use(self):
        pass

class Python(Technology):
    def use(self):
        print("Python is used.")

class JavaScript(Technology):
    def use(self):
        print("JavaScript is used.")

class Project:
    def __init__(self, developer, technology):
        self.developer = developer
        self.technology = technology

    def develop(self):
        self.developer.code()
        self.technology.use()

frontend_dev = FrontendDeveloper()
backend_dev = BackendDeveloper()
python_tech = Python()
js_tech = JavaScript()

project1 = Project(frontend_dev, python_tech)
project1.develop()

project2 = Project(backend_dev, js_tech)
project2.develop()
