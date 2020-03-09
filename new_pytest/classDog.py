#using object in python, In a new Python file, create a class of students.
#It should contain the following attributes: name, age, and class with default value "student".
#It should also contain a method which takes in 3 test scores and prints the students average test score.

class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

score1 = (input("enter your score here "))
score2 = (input("enter your score here "))
score3 = (input("enter your score here "))

average_score = (score1 + score2 + score3 / 3)
print(average_score)






