class person:
    name="Utkarsh"
    age=19
    occupation="Student"

    def info(self):
        print(f"{self.name} is a {self.occupation} and his age is {self.age}")

a=person()
b=person()
a.name="Devansh"
a.age=22
a.occupation="Software Developer"
a.info()
b.info()

# Where a and b are the objects
