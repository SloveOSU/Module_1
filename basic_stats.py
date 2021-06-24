# Author: Steven Love
# Date: 6/24/2021
# Description: CS 162 Module 1
#   basic_stats.py, defines a Student class that takes in a name string and a grade int
#   the Student class only provides member functions to get and set the private data members.
#   There is then a function that takes a list of implemented Student objects called basic_stats.
#   basic_stats takes a list parameter and then creates a new list of the integer scores.
#   basic_states then uses the imported Statistics module to calculate the mean median and mode
#   the mean median and mode are then returned by the basic_stats in the form of a tuple
#   the tuple can be printed out to display the output of the mean median and mode of the parameter list


# importing statistics module as required
import statistics

# the student class creates an object that is used to populate a list that
# is then passed as an argument into the basic_stats function
# this class only has accessor functions
class Student:

    # initializing method for the Student object that takes a string and an integer value
    # @newStudentName: a string value
    # @newStudentGrade: an integer value
    def __init__(self, new_student_name, new_student_grade):
        self.__student_name = new_student_name
        self.__student_grade = new_student_grade

    # get the student name
    def get_name(self):
        return self.__student_name

    # get the student grade
    def get_grade(self):
        return self.__student_grade

    # set the student name
    def set_name(self, new_student_name):
        self.student_name = new_student_name

    # set the student grade
    def set_grade(self, new_student_grade):
        self.student_grade = new_student_grade


# this function takes a parameter of list and calculates the mean median and mode
# @listOfStudents: list of Student objects
# @return: a tuple value representing the mean, median, and mode
def basic_stats(list_of_students):

    list_of_student_scores = []

    for student in list_of_students:
        list_of_student_scores.append(student.get_grade())

    mean    = statistics.mean(list_of_student_scores)
    median  = statistics.median(list_of_student_scores)
    mode    = statistics.mode(list_of_student_scores)

    return_tuple = (mean, median, mode)

    return return_tuple

# test values that assume string and integer

#s1 = Student("John Dallas"  ,55)
#s2 = Student("John Grimes"  ,70)
#s3 = Student("John Hicks"   ,80)
#s4 = Student("John Wright"  ,90)
#s5 = Student("John Catz"    ,90)
#s6 = Student("John Rogers"  ,100)

#student_list = [s1, s2, s3, s4, s5, s6]
#print(basic_stats(student_list))


