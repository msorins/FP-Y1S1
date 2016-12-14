class Settings():
    def __init__(self):
        self._settings = {}
        self.readSettings()

    def readSettings(self):
        '''
        Reads the settings folder and puts its attribute in _settings dictionary
        '''
        try:
            path = str(__file__).replace("/appsettings.py", "/settings.properties")
            with open(path) as file:
                for line in file:
                    line = line.replace(" ", "")
                    line = line.split("=")
                    self._settings[line[0]] = line[1].rstrip('\n')

        except IOError as e:
            print(e)

    def getSettings(self, str):
        '''
        :param str: a string containing the name of the setting attribute you want to get
        :return: the value or -1 if it is nout found
        '''
        if str not in self._settings:
            return -1

        return self._settings[str]


#/Users/sorynsoo/Desktop/UBB/FP/movieRental/Utils/settings.properties