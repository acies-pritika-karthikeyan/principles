class Analytics:

    def __init__(self, employee2, project_details):
        self.employee = employee2
        self.project_details = project_details

    def data_cleaning(self):
        print(f"{self.employee.name} is cleaning data for project {self.project_details.project_name}. Project Stage: {self.project_details.project_stage}.")

    def do_eda(self):
        print(f"{self.employee.name} is performing exploratory data analysis in project {self.project_details.project_name}. Project Stage: {self.project_details.project_stage}.")

    def perform_modelling(self):
        print(f"{self.employee.name} is performing modeling for project {self.project_details.project_name}. Project Stage: {self.project_details.project_stage}.")

    def do_predictions(self):
        print(f"{self.employee.name} is making predictions for project {self.project_details.project_name}. Project Stage: {self.project_details.project_stage}.")

    def execution(self):
        if self.project_details.project_stage == 'Data cleaning':
            self.data_cleaning()
        elif self.project_details.project_stage == 'EDA':
            self.do_eda()
        elif self.project_details.project_stage == 'Modeling':
            self.perform_modelling()
        elif self.project_details.project_stage == 'Prediction':
            self.do_predictions()
        else:
            print("Invalid")
