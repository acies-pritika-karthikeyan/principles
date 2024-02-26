from Development import Development
from Analytics import Analytics
from Employee import Employee
from HR import HR

if __name__ == "__main__":

   dev = Development("Pritika", 22, 13000,"edgeCore.ai", "In Progess")
   ds = Analytics("Aryan", 21, 12000, "Bose", "Analysis Phase")
   hr = HR("Subhash", 25, 10000, 1)
   
   dev.to_work()
   dev.code_back_end()
   ds.to_pitch()
   ds.data_cleaning()
   hr.to_present()
   hr.report_generate()


