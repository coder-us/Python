class Employee:
    def __init__ (self,name,id):
        self.name=name
        self.id=id
    def Showdetails(self):
        print(f"My name is {self.name} and my id is {self.id}")

class Programmer(Employee):
    def Showlanguage(self):
        print("The default language is Python")


e1=Employee("Utkarsh Srivastava",100)
e1.Showdetails()
e2=Programmer("Devansh",500)
e2.Showlanguage()
e2.Showdetails()




