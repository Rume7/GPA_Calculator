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
        print(self.course.name)


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
        for each_course in self.get_course_taken():
            aCourse = Course(each_course)
            score = self.get_score_for_course(aCourse.get_course_name())
            grade = aCourse.get_grade(score)
            points = aCourse.get_grade_point(grade)
            total_course_unit += aCourse.get_course_unit()
            total_points += (points * aCourse.get_course_unit())
        self.gpa = total_points/ total_course_unit
        return self.gpa

    def __str__(self):
        print(self.get_student_name())

## A function that opens a text file and reads it to determine the
## students name, matric number, courses and the score for the courses.
## Input file format: S/N  Name Matric Num Course1, ..., Course5 Unit. 
## Output file format: S/N Name Matric Num CGPA

def main(input_file, txt_output_file):
    course_unit = 3
    try:
        opened_file = open(input_file, 'r')
        output_file = open(txt_output_file, 'w')
        if opened_file.mode == 'r':
            file_lines_in_list = opened_file.readlines()
            ## Read line one of the input file to create student data
            ## index 0 to 3
            student_data = file_lines_in_list[0].split()[0:4]
            student_serial = student_data[0]
            first_name = student_data[1]
            last_name = student_data[2]
            full_name = first_name + ' ' + last_name
            matric_num = student_data[3]

            # Print header to output file
            print(student_serial, '\t', 'FULL  NAME', '\t\t', matric_num, '\t', 'GPA',\
                   file=output_file)
            
            ## Reading line one of the input file to create course object
            ## index 4 to 9
            courses = file_lines_in_list[0].split()[4:9]
            course_unit = file_lines_in_list[0].split()[9]
            
            course_obj1 = Course(courses[0], course_unit)
            course_obj2 = Course(courses[1], course_unit)
            course_obj3 = Course(courses[2], course_unit)
            course_obj4 = Course(courses[3], course_unit)
            course_obj5 = Course(courses[4], course_unit)

            ## Start reading from line 2 because line 1 contains header
            for each_line in file_lines_in_list[1:]:
                student_record = each_line.split()   # Scores of five courses
                (student_sn, student_name, student_matric_num) = student_record[0], \
                                student_record[1] + ' ' + student_record[2], student_record[3]
                student_scores = student_record[4:9]

                ## Create a student object and set scores for each course
                master_student = Student(student_name, student_matric_num, len(courses))

                ## Add courses to student object
                master_student.add_course(course_obj1)
                master_student.add_course(course_obj2)
                master_student.add_course(course_obj3)
                master_student.add_course(course_obj4)
                master_student.add_course(course_obj5)
                
                master_student.set_score_for_course(course_obj1, int(student_scores[0]))
                master_student.set_score_for_course(course_obj2, int(student_scores[1]))
                master_student.set_score_for_course(course_obj3, int(student_scores[2]))
                master_student.set_score_for_course(course_obj4, int(student_scores[3]))
                master_student.set_score_for_course(course_obj5, int(student_scores[4]))

                ## Add tabs and indent properly and send to output file.
                print(student_sn, '\t', master_student.get_student_name().ljust(20), '\t',\
                      master_student.get_matric_num().rjust(10), '\t', '{:2.2f}'.format(float(master_student.get_GPA())),\
                      file = output_file)
                
                ## Close out.
            output_file.close()
    except ZeroDivisionError as f:
        print(f)
    except ValueError as e:
        print("Problem with code:", e)
        
filename="Choose input file"
output = "Choose output file"
main(filename, output)

