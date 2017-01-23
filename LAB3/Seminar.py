'''
Created on Oct 7, 2016

@author: Arthur
'''
import re
"""
Write an application which manages a list of students. Each student has
a unique id (string), a name (string) and a grade (integer). The application allows the following commands:
    
    1. add <student_id>, <student_name>, <student_grade> 
        - adds the student with the given id, name and grade to the list. 
        - error if giving existing id, the name or grade fields not given or empty
    
    2. delete <student_id> 
        - deletes the student with the given id from the list
        - error if non-existing id given  
        
    3. show all 
        - shows all students
    
    4. show <grade> 
        - shows students whose grade is >= to given 'grade'

    5. help
        - show a list of commands

    6. exit
        - exit the program

    e.g:
    add 1, Pop Mircea, 9
    add 2, Morar Maria, 6
    delete 1
    show 5
    delete 2

    NB!
        - This program does not perform all the required input validation
        
    Additional work:
        - Implement the test functions at the end of the source code
"""

def start():
    '''
    Entry point into the program
    '''
    studentList = []
    
    '''
    We add a few students so that we do not start from scratch
    '''
    testInit(studentList)

    while True:
        '''
        User input consist of command and parameters
        '''
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]

        '''
        Execute command
        '''
        if command == 'add':
            addStudentCommand(studentList, params)
        elif command == 'delete':
            delStudentCommand(studentList, params)
        elif command == 'show':
            showStudentCommand(studentList, params)
        elif command == 'help':
            helpCommand()
        elif command == 'exit':
            break    
        else:
            print("Invalid command!")

def readCommand():
    '''
    Read and parse user commands
    input: -
    output: (command, params) tuple, where:
            command is user command
            params are parameters
    '''
    cmd = input("command: ")
    '''
    Separate command word and parameters
    '''        
    if cmd.find(" ") == -1:
        '''
        No parameters - e.g. help, exit
        '''
        command = cmd
        params = ""
    else:
        '''
        We have parameters - e.g. add 1,A,6
        '''
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" "):]
        params = params.split(",")
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return (command, params)

def addStudentCommand(studentList, cmd):
    '''
    Adding a student
    '''
    if len(cmd) < 3:
        print("Invalid input. Student was not added")
        return
    grade = int(cmd[2])
    if len(cmd[0]) == 0 or len(cmd[1]) == 0 or grade < 1 or grade > 10:
        print("Invalid input. Student was not added") 

    '''
    Add the student
    '''
    student = (cmd[0], cmd[1], int(cmd[2]))
    if addStudent(studentList, student) == False:
        print("Invalid input. Student was not added")

def delStudentCommand(studentList, cmd):
    '''
    Delete a student
    '''
    if deleteStudent(studentList, cmd[0]) == False:
        print("Invalid Data. No student was deleted")

def showStudentCommand(studentList, cmd):
    '''
    Show students
    '''
    if cmd[0] == 'all':
        print(listToString(studentList))
    else:
        try:
          grade = int(cmd[0])
          sublist = gradesGreaterThan(studentList, grade)
          print(listToString(sublist))
        except ValueError:
          letters = cmd[0]
          sublist = namesStartingWithLetter(studentList, letters)
          print(listToString(sublist))

def helpCommand():
    print("Valid commands:")
    print("\t add <student_id>, <student_name>, <student_grade>") 
    print("\t delete <student_id>") 
    print("\t show all") 
    print("\t show <grade>") 
    print(" \t help")
    print("\t exit")

def listToString(studentList):
    """
    Build the string representation of a list of students
    input: studentList - the list of students
    output: The string
    """
    res = ""
    for s in studentList:
        res += studentToString(s)
        res += "\n"
    return res

def studentToString(s):
    """
    Build the string representation for a student
    input: s - the student
    output: The string
    """
    return s[0] + " name " + s[1] + " has grade " + str(s[2])


def findById(studentList, studentID):
    """
    Searches for a student, by id.
    Input: studentList - the list of students
           studentID - a string representing the id of the student
    Output: pos - the position of the student with the given id,
                  -1 if there is no student with the given id
    """
    pos = -1
    for i in range(0, len(studentList)):
        s = studentList[i]
        if s[0] == studentID:
            pos = i
            break
    return pos

def addStudent(studentList, student):
    """
    Adds the student 'student' to the list of students studentList, if there is no other student
    with the same id.
    Input: studentList - the list of students
           student - a tuple that represents the student'student Data
    Output: studentList' - a list of students, studentList' = studentList U {student} (student is added to the list studentList)
            Returns true if the student was added and false, otherwise.
    """
    pos = findById(studentList, student[0])  # student[0] - is the first element of the tuple student (the id)
    if pos == -1:  # if another student with this id does not exist => add
        studentList.append(student)
        return True
    return False

def deleteStudent(studentList, studentID):
    """
    Deletes the student with the given id from the list studentList
    Input: studentList - the list of students
           studentID - a string, representing the id of the student which must be deleted
    Output: True - if the student was correctly removed
            False - otherwise
    """
    # search the index of the student with the given id
    pos = findById(studentList, studentID)
    if pos == -1:  # a student with the given id does not exist
        return False
    else:
        studentList.pop(pos)
        return True

def gradesGreaterThan(studentList, grade):
    """
    Identifies the students having grades greater than 'grade'.
    Input: studentList - the list of students
    Output: gradesList - a list containing those students from studentList which have grades
                greater than or equal to 'grade'
    """
    gradesList = []
    for student in studentList:
        if student[2] >= grade:  # student[2] is the third element (the grade) of the tuple representing a student
            gradesList.append(student)            
    return gradesList


def namesStartingWithLetter(studentList, letters):
    """
    Identifies the students having grades greater than 'grade'.
    Input: studentList - the list of students
    Output: gradesList - a list containing those students from studentList which have grades
                greater than or equal to 'grade'
    """
    gradesList = []
    for student in studentList:
         if student[1].startswith(letters):  # student[2] is the third element (the grade) of the tuple representing a student
            gradesList.append(student)
    return gradesList
"""
Here be tests !
"""
def testInit(studentList):
    studentList.append(('1', "Pop Ioana", 10))
    studentList.append(('2', "Man Ionel", 5))
    studentList.append(('3', "Marian Sofia", 9))
    studentList.append(('4', "Boca Mihaela", 6))
    studentList.append(('5', "Popa Adela", 5))
    studentList.append(('6', "Costin Daniel", 7))
    studentList.append(('7', "Zaharia Vasile", 8))
    studentList.append(('8', "Mihnea Loredana", 9))

def testAddStudent(studentList):
    addStudent(studentList, ('9', "Sorin Mircea", 9))
    assert len(studentList) == 9

    addStudent(studentList, ('10', "Sorin Soo", 7))
    assert len(studentList) == 10

    addStudent(studentList, ('11', "Alex Bl", 10))
    assert len(studentList) == 11 and [item for item in studentList if item[0] == '11' and item[1] == "Alex Bl" and item[2] == 10]

    addStudent(studentList, ('9', "Andreea Lup", 10))
    assert len(studentList) == 11

    addStudent(studentList, ('9', "", 10))
    assert len(studentList) == 11



def testDeleteStudent(studentList):

    assert deleteStudent(studentList, "1") == True
    assert deleteStudent(studentList, "-1") == False
    assert deleteStudent(studentList, "19191") == False
    assert deleteStudent(studentList, "2") == True
    assert deleteStudent(studentList, "2") == False


def testFindById(studentList):
    assert  findById(studentList, "-1") == -1
    assert  findById(studentList, "2") == -1
    assert  findById(studentList, "10") == 7
    assert  findById(studentList, "8") == 5
    assert  findById(studentList, "") == -1
    assert  findById(studentList, "99999") == -1


def testGradesGreaterThan(studentList):
    assert  gradesGreaterThan(studentList, 15) == []
    assert  gradesGreaterThan(studentList, 0) == studentList
    assert  gradesGreaterThan(studentList, 10) == [('11', 'Alex Bl', 10)]
    assert  gradesGreaterThan(studentList, 9) == [('3', 'Marian Sofia', 9), ('8', 'Mihnea Loredana', 9), ('9', 'Sorin Mircea', 9), ('11', 'Alex Bl', 10)]

def runAllTests():
    studentList = []
    testInit(studentList)
    testAddStudent(studentList)
    testDeleteStudent(studentList)
    testFindById(studentList)
    testGradesGreaterThan(studentList)

start()
#runAllTests()
