# Create a dataclass called Student with the following attributes:
# name (str), id (int), grades (list of floats). Write a method
# called average_grade that returns the average of the student's grades.
# Instantiate an object of Student with a name of "Alice", id of 12345,
# and grades of [3.5, 4.0, 3.7], and print out their average grade.

from dataclasses import dataclass


@dataclass()
class Student:
    name: str
    id: int
    grades: list

    def average_grade(self):
        total = 0
        count = 0
        for grade in self.grades:
            total += grade
            count += 1

        average = total / count
        return average


alice = Student('Alice', 12345, [3.5, 4.0, 3.7])

print(alice.average_grade())

