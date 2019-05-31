## Read and print the line in a csv file

import os


def get_name(name_list):
    name = ""
    for each_name in name_list:
        name += (each_name + ' ')
    return name

    
def get_course_grade(score):
    if score >= 70: return 'A'
    elif score >= 60: return 'B'
    elif score >= 50: return 'C'
    elif score >= 45: return 'D'
    elif score >= 40: return 'E'
    else:             return 'F'


def get_points_for_course(grade):
    if grade == 'A':   return 5.0
    elif grade == 'B': return 4.0
    elif grade == 'C': return 3.0
    elif grade == 'D': return 2.0
    elif grade == 'E': return 1.0
    else:              return 0.0

    
def get_CGPA(list_of_scores, unit_of_course, project_score, project_unit):
    '''
        This method computes the cumulative grade point average.
    '''
    total_points = 0
    total_course_units = 0
    for score in list_of_scores:
        course_grade = get_course_grade(float(score))
        course_points = get_points_for_course(course_grade)
        total_points += (course_points * float(unit_of_course))
        total_course_units += unit_of_course

    ## For project
    project_grade = get_course_grade(project_score)
    project_points = get_points_for_course(project_grade)
    total_points += (project_points * project_unit)
    total_course_units += project_unit

    return total_points/total_course_units


def publishing_header(serial, name, matric, title, output_file):
    '''
        This method print the header of the file in the output file.
    '''
    try:
        result_file = open(output_file, 'a')
        print(serial, name.ljust(25), matric.ljust(18), title, file = result_file)
    except:
        print('Error with Header code')
    finally:
        result_file.close()

        
def publish_to_output_file(serial_num, full_name, matric_number, cgpa, output_file):
    '''
        This method print the student serial, full name, matric number and CGPA to
        the output file.
    '''
    try:
        result_file = open(output_file, 'a')
        print(serial_num.ljust(3), full_name.ljust(28), matric_number, '\t', 
                      '{:2.2f}'.format(float(cgpa)), file = result_file)
    except:
        print('Error with output file')
    finally:
        result_file.close()
                

def process_csv_file(input_file, result_file):
    '''
        This method process the input file.
        The first try block check the existence of the result file and deletes it
        if it exists. This is necessary as the publish method appends data to the
        existing file.
    '''
    try:
        file_exists = os.path.isfile(result_file)
        if file_exists:
            ## Delete the file
            os.remove(result_file)           
    except IOError as file_error:
        print(file_error)
        
    try:
        opened_file = open(input_file, 'r')
        if opened_file.mode == 'r':
            lines_in_file = opened_file.readlines()

            # Get header of titles
            header = lines_in_file[0]
            publishing_header('S/N', ' FULL NAME', 'MATRIC NUMBER', 'CGPA', result_file)
            
            # Get other lines of names, scores and course unit
            for each_line in lines_in_file[1:]:
                a_line = each_line.split(';')
                serial_num = a_line[0]
                student_name = a_line[1:4]
                matric_number = a_line[4]
                full_name = get_name(student_name)
                
                course_scores = a_line[5:15]
                course_unit = int(a_line[15])
                project_score = float(a_line[16])
                project_unit = int(a_line[17])
                
                cgpa = get_CGPA(course_scores, course_unit, project_score, project_unit)

                publish_to_output_file(serial_num, full_name, matric_number, cgpa, result_file)   
    except ValueError as error:
        print('Error in process input document:', error)
            

filename= 'C:\\...\\P_codes\\test1.csv'
result_file = 'C:\\...\\P_codes\\result.txt'
process_csv_file(filename, result_file)


