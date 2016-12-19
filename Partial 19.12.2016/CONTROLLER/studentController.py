class StudentController():

    def __init__(self, studentRepository):
        '''
        :param studentRepository: the repository
        '''
        self._studentRepository = studentRepository

    def add(self, studentObj):
        '''
        :param studentObj: Student type object to be added
        :return: saves the file
        '''
        obj = self._studentRepository.load()
        obj.append(studentObj)

        self._studentRepository.save(obj)

    def giveBonus(self, p, b):
        '''
        :param p: integer number
        :param b: integer number
        :return:  saves the file
        '''
        obj = self._studentRepository.load()
        for i in range(len(obj)):
            if obj[i].getAttendanceCount() >= p:
                newGrade = obj[i].getGrade() + b
                if newGrade > 10:
                    newGrade = 10
                obj[i].setGrade(newGrade)

        self._studentRepository.save(obj)

    def getNumberOfStudents(self):
        '''
        :return: Getter, returns an integer
        '''
        obj = self._studentRepository.load()
        return len(obj)

    def displayStudentsSelective(self, str):
        '''
        :param str: string
        :return: an object with all the students that meet the requirements
        '''
        obj = self._studentRepository.load()
        newObj = []

        for crt in obj:
            if crt.getName().find(str) != -1:
                newObj.append(crt)

        return newObj

    def displayStudentsSorted(self):
        '''
        :return: a sorted object by the name
        '''
        obj = self._studentRepository.load()
        obj = sorted(obj, key=lambda x: x.getGrade(), reverse=True)
        return obj

