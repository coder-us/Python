class Employee:
    company = "Apple"
    def show (self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(self,newCompany):
     self.company=newCompany

e1=Employee()
e1.name="Utkarsh"
e1.show()
e1.changeCompany("Tesla")

print(Employee.company)

