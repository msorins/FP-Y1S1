class Student():
    crtId = 0
    def __init__(self, id, name, attendanceCount, grade):
        '''
        :param id: integer
        :param name:  string
        :param attendanceCount: integer
        :param grade: integer
        '''
        self.setId(id)
        self.setName(name)
        self.setAttendanceCount(attendanceCount)
        self.setGrade(grade)

    def setId(self, id):
        '''
        :param id: integer
        :return:
        '''
        self._id = int(id)

    def getId(self):
        '''
        :return: the id
        '''
        return self._id

    def setName(self, name):
        '''
        :param name: string
        '''
        try:
            auxName = name.split(' ')
        except Exception:
            raise RuntimeError("Name length must contain at least 2 words")
            return

        if len(auxName) < 2:
            raise RuntimeError("Name length must contain at least 2 words")

        for crt in auxName:
            if len(crt) < 3:
                raise RuntimeError("Each word must contain at least 3 characters")
        self._name = name



    def getName(self):
        '''
        GETTER
        :return: the name
        '''
        return self._name

    def setAttendanceCount(self, attendance):
        '''
        SETTER
        :param attendance: integer
        '''
        self._attendanceCount = int(attendance)

    def getAttendanceCount(self):
        '''
        GETTER
        :return: the attendanceCount
        '''
        return self._attendanceCount

    def setGrade(self, grade):
        '''
        SETTER
        :param grade: integer
        '''
        try:
            grade = int(grade)
        except Exception:
            raise  RuntimeError("Grade is not in the right format")

        self._grade = grade

    def getGrade(self):
        '''
        GETTER
        :return: the grade
        '''
        return self._grade