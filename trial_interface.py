import zope.interface


class IDeveloper(zope.interface.Interface):
    def code(self):
        """Code method"""


class ITechnology(zope.interface.Interface):
    def use(self):
        """Use method"""


@zope.interface.implementer(IDeveloper)
class Developer:
    def __init__(self, name):
        self.name = name

    def code(self, task, product_details):
        if task == 'backend':
            print(f"{self.name} is coding the backend of {product_details.product_name}. Product Status: {product_details.product_status}.")
        elif task == 'frontend':
            print(f"{self.name} is coding the frontend of {product_details.product_name}. Product Status: {product_details.product_status}.")
        else:
            print("Invalid task")


@zope.interface.implementer(ITechnology)
class Technology:
    def __init__(self, technology):
        self.technology = technology

    def use(self, task):
        if task == 'backend':
            print(f"Backend Technology used is: {self.technology}.")
        elif task == 'frontend':
            print(f"Frontend Technology used is: {self.technology}.")
        else:
            print("Invalid task")


developer = Developer("Sai")
technology = Technology("Python")

class ProductDetails:
    def __init__(self, product_name, product_status):
        self.product_name = product_name
        self.product_status = product_status

product_details = ProductDetails("greenMath", "In Progress")

task = 'backend'
developer.code(task, product_details)
technology.use(task)
