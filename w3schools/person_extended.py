class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    self.dna = {'name':self.firstname,'last_name':self.lastname}

  def printname(self):
    print(self.firstname, self.lastname)
    return self.dna

class Student(Person):
    def __init__(self, fname, lname, year, attributes = 'clever'):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.attrib = attributes
    
    def better_printname(self):
        print(self.firstname,self.lastname,self.attrib)
        self.dna['is'] : self.attrib
        return self.dna
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
alumno = x.printname()
print (alumno)
alumno = x.better_printname()
print(alumno)