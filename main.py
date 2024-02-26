from Employee import Employee
from ProductDetails import ProductDetails
from ProjectDetails import ProjectDetails
from TechnologyDetails import TechnologyDetails
from HR import HR
from Analytics import Analytics
from Development import Development
from Technology import Technology


if __name__ == "__main__":

    employee1 = Employee(1, "Pritika", 22, 13000)
    product_details = ProductDetails("edgeCore.ai", "In Progress")
    dev = Development(employee1, product_details, "backend")

    employee2 = Employee(2, "Aryan", 21, 12000)
    project_details = ProjectDetails("Bose", "Modeling")
    ds = Analytics(employee2, project_details)

    employee3 = Employee(3, "Subhash", 24, 12500)
    hr = HR(employee3, "Filing")

    # technology_details = TechnologyDetails("React.js", "Python")
    technology_details = TechnologyDetails("Python")
    tech = Technology(dev, technology_details)

    dev.execution()
    tech.execution()
    ds.execution()
    hr.execution()



