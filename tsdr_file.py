"""


"""
import requests
import json

class TsdrFile():
    # Alllows users to set serial number when instantiating
    # Includes a demo serial number for lazy people
    def __init__(self, serNum=['88855299']):
        self.setFile(serNum)

    # Allows user to change serial number
    # Do a try-catch and retry wheb not 200
    def setFile(self, serNum):
        for x in serNum:
            url = 'https://tsdrsec.uspto.gov/ts/cd/casestatus/sn' + serNum + \
            '/info.json'
            response = requests.get(url)
            text = response.text
            dikt = json.loads(text)
            # Set private variables used by other methodsB
            self.__jsonFile = text
            self.__dictFile = dikt['trademarks'][0]

    # Methods for accessing data
    # Returns the descriptions of goods and services and their class numbers
    # Returns a dictionary
    @property
    def ids(self):
        gsIds = {}
        for x in self.__dictFile['gsList']:
            gsIds.update({x['primeClassCode']: x['description']})
        return(gsIds)

    # Returns serial number
    @property
    def serNum(self):
        return(str(self.__dictFile['status']['serialNumber']))

    # Returns mark literal
    @property
    def mark(self):
        return(self.__dictFile['status']['markElement'])

    # Returns the registration status
    @property
    def status(self):
        return(str(self.__dictFile['status']['status']))

class FileStatus():
    def __init__(self, serNum, cl, desc):
        self.__file = TsdrFile(serNum)
        self.__cl = cl
        self.__desc = desc

    def getRegStatus(self):
        return(self.__file.status)

    def getIdStatus(self):
        print(self.__file.ids)

class ListHandler():
    def __init__(self, fileLoc):
        pass

    def parseFile():
        self.__file = {}
        for x in serNum:
            self.__file[x] = tsdrFile(x)

class IdComparison():
    def __init__(fileId, compTerm, cl):
        self.__fileId = fileId
        self.__compTerm = compTerm
        self._cl = cl

    def __formatId():
        pass

    def compareId():
        pass


x = '87123449'
y = '009'
z = 'shirts'

t = FileStatus(x, y, z)
t.getRegStatus()
t.getIdStatus()
