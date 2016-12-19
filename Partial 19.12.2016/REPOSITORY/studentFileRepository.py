from MODEL.studentModel import *

class StudentFileRepository():
    def __init__(self, path):
        '''
        :param path: string with the absolute path
        '''
        self._path = path


    def save(self, obj):
        '''
        :param obj: a list with students object
        :return:  saves that list into the file
        '''
        res = ''
        for crt in obj:
            res = res + str(crt.getId()) + ',' + str(crt.getName()) + ',' + str(crt.getAttendanceCount()) + ',' + str(crt.getGrade())
            res += '\n'

        open(self._path, 'w').write(res)

    def load(self):
        '''
        :return: load the list of students from the files and returns it
        '''
        res = []
        with open(self._path) as file:
            for line in file:
                line = line.split(',')
                newObj = Student(line[0], line[1], line[2], line[3])
                res.append(newObj)

        return res


