class person :
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person("Utkarsh","Developer")
b=person("Devansh","HR")
a.info()
b.info()

   