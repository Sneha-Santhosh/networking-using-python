from abc import ABC, abstractmethod
class GradingSystem:
    def calculate_grade(self, students):
        print('Calculating grades')
        print('==========')
        for student in students:
            print('Grades for: {student.id} - {student.name}')
            print(f'- Check grade: {student.calculate_grade()}')
            print('')

class Student(ABC):
    # class attribute
    college = "Centennial"

    # instance attribute
    def __init__(self, id, name):
        self.id = id
        self.name = name

    #polymorphism
    def campus(self):
        print("{}'s classes are at Progress Campus".format(self.name))
    
    @abstractmethod
    def calculate_grade(self):
        pass

#Inheritance
class  NonTechnicalStudent(Student):

    #Student with no practical courses
    def __init__(self, id, name, theory_marks):
        super().__init__(id, name)
        self.theory_marks = theory_marks

    def calculate_grade(self):
        if self.theory_marks > 100:
            raise Exception('Marks should not exceed 100')
        return self.theory_marks

    def campus(self):
        print("{}'s classes are at Morningside Campus".format(self.name))
    
    def __str__(self):
        return f"{self.name} has id {self.id}"

class TechnicalStudent(Student):

    #Students in technical courses have both theory and practical marks
    def __init__(self, id, name, theory_marks, practical_marks):
        super().__init__(id, name)
        self.theory_marks = theory_marks
        self.practical_marks = practical_marks

    def calculate_grade(self):
        if self.theory_marks > 100:
             raise Exception('Marks should not exceed 100')
        return (self.theory_marks + self.practical_marks)/2

class CoopStudent(TechnicalStudent):

    #Co-op students in Technical stream get extra 10 marks 
    def __init__(self, id, name, theory_marks, practical_marks):
        super().__init__(id, name, theory_marks, practical_marks)
        #private variable
        self.__coop_marks = 10

    def calculate_grade(self):
        if self.theory_marks > 100:
            raise Exception('Marks should not exceed 100')
        return (self.theory_marks + self.practical_marks + self.__coop_marks)/3

non_techie = NonTechnicalStudent(1,'Sneha',92)
techie = TechnicalStudent(2,'Maya', 50, 50)
coop = CoopStudent(3,'Surya', 80, 50)
exception_example = NonTechnicalStudent(4, 'Mike', 150)
grading_system = GradingSystem()
grading_system.calculate_grade([
    non_techie,
    techie,
    coop,
    exception_example
])

print('Campuses :-  ')
non_techie.campus()
techie.campus()
coop.campus()

#example of __str__ 
print(non_techie)
# class Pigeon:
    
#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# # instantiate the Pigeon class
# pigeon1 = Pigeon("Piggy", "grey")
# pigeon2 = Pigeon("Pam", "white")

# # access the class attributes
# print("{} is a {}".format(pigeon1.name,pigeon1.__class__.species))
# print("{} is a {}".format(pigeon2.name,pigeon2.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( pigeon1.name, pigeon1.color))
# print("{} is {} years old".format( pigeon2.name, pigeon2.color))

