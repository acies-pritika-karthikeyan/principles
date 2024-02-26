from Employee import Employee
from ProductDetails import ProductDetails
from ProjectDetails import ProjectDetails
from TechnologyDetails import TechnologyDetails
from HR import HR
from Analytics import Analytics
from Development import Development
from Technology import Technology
from AddDetails import AddDetails

def main():
    addDetails = AddDetails()
    emp = addDetails.addEmp(2, "Aryan", 21, 12000)
    project_details = addDetails.addProd("DS", "Clean","Analytics")
    # ds = Analytics(emp, project_details)

    emp = addDetails.addEmp(3, "Subhash", 24, 12500)
    project_details = addDetails.addProd("HR", "recuriment","HR")
    # hr = HR(emp, project_details)
if __name__ == "__main__":
    main()



