## Create a Course object

class Course(object):
    def __init__(self, course_name, course_unit):
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
        return str(self.course.name)


class Student(object):
    
    courseTaken = 0
    
    def __init__(self, name, matric_num):
        self.name = name
        self.matric_num  = matric_num
        self.list_of_courses = []
        self.gpa = 0.0
        self.student_scores = {}
        Student.courseTaken += 1

    def get_student_name(self):
        return self.name

    def get_matric_num(self):
        return self.matric_num

    def get_num_of_coursesTaken(self):
        return Student.courseTaken

    def get_course_taken(self):
        return self.list_of_courses

    def add_course(self, Course):
        """Course is a list of tuples of course name and it units."""
        new_course = (Course.get_course_name(), Course.get_course_unit())
        self.list_of_courses.append(new_course)

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
        # You're running over a list of tuples.
        for each_course in self.get_course_taken():     
            course_title = each_course[0]
            course_unit = each_course[1]
            aCourse = Course(course_title, course_unit)
            score = self.get_score_for_course(aCourse.get_course_name())
            grade = aCourse.get_grade(score)
            points = aCourse.get_grade_point(grade)
            total_course_unit += int(aCourse.get_course_unit())
            total_points += (points * aCourse.get_course_unit())
        self.gpa = total_points/ total_course_unit
        return self.gpa

    def __str__(self):
        return str(self.get_student_name())

## A function that opens a text file and reads it to determine the
## students name, matric number, courses and the score for the courses.
## Input file format: S/N  Name Matric Num Course1, ..., Course5 Unit. 
## Output file format: S/N Name Matric Num CGPA

def main(input_file, txt_output_file):
    course_unit = 3
    project_unit = 6
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
            courses = file_lines_in_list[0].split()[4:14]
            #course_unit = file_lines_in_list[0].split()[9]
            project_code = file_lines_in_list[0].split()[15]
            #project_unit = file_lines_in_list[0].split()[11]  returns the string 'UNIT'
            
            course_obj1 = Course(courses[0], int(course_unit))
            course_obj2 = Course(courses[1], int(course_unit))
            course_obj3 = Course(courses[2], int(course_unit))
            course_obj4 = Course(courses[3], int(course_unit))
            course_obj5 = Course(courses[4], int(course_unit))
            course_obj6 = Course(courses[5], int(course_unit))
            course_obj7 = Course(courses[6], int(course_unit))
            course_obj8 = Course(courses[7], int(course_unit))
            course_obj9 = Course(courses[8], int(course_unit))
            course_obj10 = Course(courses[9], int(course_unit))
            course_proj = Course(project_code, int(project_unit))

            ## Start reading from line 2 because line 1 contains header
            for each_line in file_lines_in_list[1:]:
                student_record = each_line.split()   # Scores of five courses
                (student_sn, student_name, student_matric_num) = student_record[0], \
                                student_record[1] + ' ' + student_record[2], student_record[3]
                student_scores = student_record[4:14]
                student_project_score = student_record[15]
                student_project_unit = student_record[16]

                ## Create a student object and set scores for each course
                master_student = Student(student_name, student_matric_num)

                ## Add courses to student object
                master_student.add_course(course_obj1)
                master_student.add_course(course_obj2)
                master_student.add_course(course_obj3)
                master_student.add_course(course_obj4)
                master_student.add_course(course_obj5)
                master_student.add_course(course_obj6)
                master_student.add_course(course_obj7)
                master_student.add_course(course_obj8)
                master_student.add_course(course_obj9)
                master_student.add_course(course_obj10)
                master_student.add_course(course_proj)      # Adding project to list of courses
                
                master_student.set_score_for_course(course_obj1, int(student_scores[0]))
                master_student.set_score_for_course(course_obj2, int(student_scores[1]))
                master_student.set_score_for_course(course_obj3, int(student_scores[2]))
                master_student.set_score_for_course(course_obj4, int(student_scores[3]))
                master_student.set_score_for_course(course_obj5, int(student_scores[4]))
                master_student.set_score_for_course(course_obj6, int(student_scores[5]))
                master_student.set_score_for_course(course_obj7, int(student_scores[6]))
                master_student.set_score_for_course(course_obj8, int(student_scores[7]))
                master_student.set_score_for_course(course_obj9, int(student_scores[8]))
                master_student.set_score_for_course(course_obj10, int(student_scores[9]))
                master_student.set_score_for_course(course_proj, int(student_project_score))

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
        
filename="...\\input.txt"
output = "...\\output2.txt"
main(filename, output)



