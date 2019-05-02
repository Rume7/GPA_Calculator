## Create a Course object

class Course(object):
    def __init__(self, course_name, course_unit=3):
        self.course_name = course_name
        self.course_unit = course_unit

    def get_course_name(self):
        return self.course_name

    def get_course_unit(self):
        return self.course_unit

    def set_course_name(self, name):
        self.name = name

    def set_course_unit(self, unit):
        self.course_unit = unit

    def get_grade(self, score):
        if score >= 70: return 'A'
        elif score >= 60: return 'B'
        elif score >= 50: return 'C'
        elif score >= 45: return 'D'
        elif score >= 40: return 'E'
        else:             return 'F'

    def get_grade_point(self, grade):
        if grade == 'A':   return 5.0
        elif grade == 'B': return 4.0
        elif grade == 'C': return 3.0
        elif grade == 'D': return 2.0
        elif grade == 'E': return 1.0
        else:              return 0.0

    def __str__(self):
        print('Course name:', self.name)


class Student(object):
    def __init__(self, name, matric_num, num_of_courseTaken=5):
        self.name = name
        self.matric_num  = matric_num
        self.courseTaken = num_of_courseTaken
        self.list_of_courses = []
        self.gpa = 0.0
        self.student_scores = {}

    def get_student_name(self):
        return self.name

    def get_matric_num(self):
        return self.matric_num

    def get_num_of_coursesTaken(self):
        return self.num_of_courseTaken

    def get_course_taken(self):
        return self.list_of_courses

    def add_course(self, Course):
        """Course is a list of tuples of course name, score and units."""
        self.list_of_courses.append(Course.get_course_name())

    def set_score_for_course(self, Course, score):
        self.student_scores[Course.get_course_name()] = score

    def get_score_for_course(self, course):
        if course in self.student_scores:
            return self.student_scores[course]
        else:
            return 0.0

    def get_GPA(self):
        total_points = 0.0
        total_course_unit = 0
        for each_course in list(self.get_course_taken()):
            aCourse = Course(each_course)
            score = self.get_score_for_course(aCourse.get_course_name())
            grade = aCourse.get_grade(score)
            points = aCourse.get_grade_point(grade)
            print(score, grade, points)
            total_course_unit += aCourse.get_course_unit()
            total_points += (points * aCourse.get_course_unit())
        self.gpa = total_points/total_course_unit
        return self.gpa


## Create the Course objects
course_unit = 3
course1 = Course("MIT801", course_unit)
course2 = Course("MIT802", course_unit)
course3 = Course("MIT803", course_unit)
course4 = Course("MIT815", course_unit)
course5 = Course("MIT821", course_unit)

## Create a Student object
no_of_courses = 5
student1 = Student("Jerry Momodu", "MIT01012019", no_of_courses)
student1.add_course(course1)
student1.add_course(course2)
student1.add_course(course3)
student1.add_course(course4)
student1.add_course(course5)

## Set score for each course
student1.set_score_for_course(course1, 59)
student1.set_score_for_course(course2, 67)
student1.set_score_for_course(course3, 77)
student1.set_score_for_course(course4, 77)
student1.set_score_for_course(course5, 97)

print(student1.get_student_name(), ": GPA =", student1.get_GPA(), "\n")

## Write the function that opens a text file and reads it to determine the
## students name, courses and the score for the courses.
## Input file format: S/N  Name Matric Num Course1, ..., Course 5 Unit, GPA CGPA
## Output file format: S/N Name  Matric Num  CGPA

def main(filename):
    try:
        opened_file = open(filename, 'r')
        if opened_file.mode == 'r':
            file_lines_in_list = opened_file.readlines()
            ## Start reading from line 2 because line 1 contains header
            for each_line in file_lines_in_list[1:]:
                #print(each_line, each_line.split())
                print(each_line.split())

                ## Create 5 course objects and a student object
                ## Set score for each course
                ## Call the print(student.get_student_name(), student.get_GPA())
                
            
filename="C:\\Users\\E238958\\Desktop\\testing_git\\Invent with Python\\input.txt"
main(filename)




        
