'''
Created on Oct 14, 2016

@author: Arthur
'''

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
        - sort them descending by grade

    4. show name, <start name>, <end name>
        - show all students whose name is lexicographically
          between 'start name' and 'end name'
        - sort them descending by grade

    5. show grade, <grade>, < + | - >
        - show all students whose grade is:
          '+' higher than 'grade'
          '-' lower than 'grade' 
        - sort them descending by grade

    7. help
        - show a list of commands

    8. exit
        - exit the program

    e.g:
    add 1, Pop Mircea, 9
    add 2, Morar Maria, 6
    delete 1
    show grade, 5, +
    show name, Pop, Vizitiu
    delete 2
    
    NB!
        - This program does not perform all the required input validation
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
    Show student command
    '''
    if cmd[0] == 'all':
        print(listToString(sortStudentListByGrade(studentList)))
    elif cmd[0] == 'name':
        print(listToString(showStudentByNameCommand(studentList, cmd[1:])))
    elif cmd[0] == 'grade':
        print(listToString(showStudentByGradeCommand(studentList, cmd[1:])))
    elif cmd[0][:7] == 'average':
        words = cmd[0].split()
        print(listToString(showStudentByAverageCommand(sortStudentListByGrade(studentList), words[1:])))
    else:
        print('Invalid show command!')  

def showStudentByNameCommand(studentList, cmd):
    '''
    Show students by name command
    '''
    if len(cmd) < 2:
        print('Invalid command!')
    
    startName = cmd[0]
    endName = cmd[1]
    
    return sortStudentListByGrade(studentNameFilter(studentList, startName, endName))

def showStudentByGradeCommand(studentList, cmd):
    '''
    Show students by grade command
    '''
    if len(cmd) < 2:
        print('Invalid command!')

    grade = cmd[0].strip()
    sign = cmd[1].strip()
    
    try:
        grade = int(grade)
    except ValueError:
        print('Invalid command!')
    
    if sign not in ['+', '-']:
        print('Invalid command!')

    return sortStudentListByGrade(studentGradeFilter(studentList, grade, sign))

def showStudentByAverageCommand(studentList, cmd):
    '''
    Show students by average between two indexes
    '''
    if len(cmd) < 2:
        print('Invalid command!')

    i1 = int(cmd[0])
    i2 = int(cmd[2])
    if i1 < 0 or i2 < 0 or i2 < i1 or i2 > len(studentList):
        print('Invalid command!')
        return

    n = 0
    sum = 0
    for i in range(i1, i2):
        sum = sum + int(studentList[i][2])
        n = n + 1

    print("The average between positions " + str(i1) + " and " +str(i2) + " is " + str(sum / n))


def helpCommand():
    print("Valid commands:")
    print("\t add <student_id>, <student_name>, <student_grade>") 
    print("\t delete <student_id>") 
    print("\t show all") 
    print("\t show name, <start name>, <end name>")
    print("\t show grade, <grade>, < + | - >") 
    print(" \t help")
    print("\t exit")

def listToString(studentList):
    """
    Build the string representation of a list of students
    input: studentList - the list of students
    output: The string
    """
    res = ""
    
    if studentList == None or len(studentList) == 0:
        return res

    res = "\nID  | "
    mxSpaces = 0
    for s in studentList:
        if len(s[1]) > mxSpaces:
            mxSpaces = len(s[1])

    mxSpaces -= 3
    for i in range(0, int(mxSpaces/2)):
        res = res + " "

    res = res + "NAME"

    for i in range(int(mxSpaces/2)):
        res = res + " "

    res = res + "| GRADE\n"
    length = len(res)
    for i in range(length):
        res = res + "-"
    res = res + "\n"

    for s in studentList:
        res += studentToString(s, mxSpaces + 4)
        res += "\n"
    return res

def studentToString(s, spacesLength):
    """
    Build the string representation for a student
    input: s - the students
    output: The string
    """
    returnMsg = s[0]
    if int(s[0]) < 1000:
        returnMsg = returnMsg + " "
    if int(s[0]) < 100:
        returnMsg = returnMsg + " "
    if int(s[0]) < 10:
        returnMsg = returnMsg + " "

    returnMsg = returnMsg + "| " + s[1]
    for i in range(len(s[1]), spacesLength):
        returnMsg = returnMsg + " "

    returnMsg = returnMsg + "|  " + str(s[2])
    return returnMsg



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

def studentNameFilter(studentList, startName, endName):
    '''
    Returns the sublist of students whose name is lexicographically 
    between startName and endName
    Input: studentList - the list of students
           startName, endName - filter parameters
    Output: a list of students whose names are lexicographically 
            between startName and endName  
    '''
    result = []
    
    for s in studentList:
        if startName <= s[1] and s[1] <= endName:
            result.append(s)
    return result

def studentGradeFilter(studentList, grade, sign):
    '''
    Returns the sublist of students whose grade is 
    larger/smaller than the given value 
    Input: studentList - the list of students
           grade - the grade used for filter
           sign - One of '+' or '-'
    Output: a list of students whose grade is >= (in case of '+')
            or <= (in case of '-') than 'grade'
    '''
    result = []

    for s in studentList:
        if s[2] >= grade and sign == '+':
            result.append(s) 
        if s[2] <= grade and sign == '-':
            result.append(s)
    return result

def sortStudentListByGrade(studentList):
    '''
    Sort the list of students in descending order of grade
    Input: studentList - the list of students
    Output: a copy of the input list, where students appear sorted 
    '''
    result = studentList[:]
    
    srt = False
    while srt == False:
        srt = True
        for i in range(0, len(result) - 1):
            if result[i][2] < result[i + 1][2]:
                result[i], result[i + 1] = result[i + 1], result[i]
                srt = False
    return result


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

def testAddStudent():
    pass

def testDeleteStudent():
    pass

def testFindById():
    pass

def testStudentNameFilter():
    pass

def testStudentGradeFilter():
    pass

def testSortStudentListByGrade():
    pass

def runAllTests():
    studentList = []
    testInit(studentList)
    testAddStudent()
    testDeleteStudent()
    testFindById()
    testSortStudentListByGrade()
    testStudentNameFilter()
    testStudentGradeFilter()

start()

