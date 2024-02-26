from ProjectDetails import ProjectDetails
from Employee import Employee
class AddDetails:
    def addProd(name, stage, team):
        project_details = ProjectDetails(name, stage,team)
        return project_details

    def addEmp(empId, empName, age, salary):
        employee = Employee(empId, empName, age, salary)
        return employee