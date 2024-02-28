from ProjectDetails import ProjectDetails
from Employee import Employee
class AddDetails(empId,empName, age, salary, projectName, team):
    def __init__(self, empId,empName, age, salary, projectName, team):
        self.empId = empId
        self.empName = empName
        self.age = age
        self.salary = salary
        self.projectName = projectName
        self.team = team

    def addProd(name, stage, team):
        project_details = ProjectDetails(name, stage,team)
        return project_details

    def addEmp(empId, empName, age, salary):
        employee = Employee(empId, empName, age, salary)
        return employee