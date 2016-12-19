from UI.ui import *
from CONTROLLER.studentController import *
from REPOSITORY.studentFileRepository import *

'''
STARTUP OF THE PROGRAM repository -> controller -> ui
'''

studentFileRepository = StudentFileRepository('/Users/sorynsoo/Desktop/UBB/Partial 19.12.2016/DATA/db.txt')
studentControllerObj = StudentController(studentFileRepository)

while True:
    UiObj = UI(studentControllerObj)