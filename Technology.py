class Technology:

    def __init__(self, dev, technology_details):
        self.dev = dev
        self.technology_details = technology_details

    def frontend_technology(self):
        print(f"Frontend Technology used by {self.dev.employee.name} is: {self.technology_details.technology}.")

    def backend_technology(self):
        print(f"Backend Technology used by {self.dev.employee.name} is: {self.technology_details.technology}.")

    def execution(self):
        if self.dev.task == 'backend':
            self.backend_technology()
        elif self.dev.task == 'frontend':
            self.frontend_technology()



    # def front_end_technology(self):
    #     print(f"Frontend Technology used by {self.dev.employee.name} is: {self.technology_details.frontend_tech}.")
    #
    # def back_end_technology(self):
    #     print(f"Backend Technology used by {self.dev.employee.name} is: {self.technology_details.backend_tech}.")
    #
    # def execution(self):
    #     self.front_end_technology()
    #     self.back_end_technology()