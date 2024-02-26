from Analytics import Analytics
from HR import HR
from Employee import Employee
class ProjectDetails(Employee):
    def __init__(self, projectName, projectStage, team):
        self.project_name = projectName
        self.project_stage = projectStage
        self.team = team

    def addteam(self,):
        if self.team == "Analytics":
            Analytics(self,Employee)
        elif self.team == 'HR':
            HR(self, Employee)

            

