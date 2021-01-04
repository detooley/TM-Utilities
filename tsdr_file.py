"""


"""
import requests
import json

class TsdrFile():
    # Alllows users to set serial number when instantiating
    # Includes a demo serial number for lazy people
    def __init__(self, sernum=['88855299']):
        self.setfile(sernum)

    # Allows user to change serial number
    # Do a try-catch and retry wheb not 200
    def setfile(self, sernum):
        for x in sernum:
            url = 'https://tsdrsec.uspto.gov/ts/cd/casestatus/sn' + sernum + \
            '/info.json'
            response = requests.get(url)
            text = response.text
            dikt = json.loads(text)
            # Set private variables used by other methodsB
            self.__jsonfile = text
            self.__dictfile = dikt['trademarks'][0]

    # Methods for accessing data
    # Returns the descriptions of goods and services and their class numbers
    # Returns a dictionary
    @property
    def ids(self):
        gsIds = {}
        for x in self.__dictfile['gslist']:
            gsids.update({x['primeclasscode']: x['description']})
        return(gsids)

    # Returns serial number
    @property
    def serNum(self):
        return(str(self.__dictfile['status']['serialnumber']))

    # Returns mark literal
    @property
    def mark(self):
        return(self.__dictfile['status']['markelement'])

    # Returns the registration status
    @property
    def status(self):
        return(str(self.__dictfile['status']['status']))

class FileStatus():
    def __init__(self, sernum, cl, desc):
        self.__file = TsdrFile(serNum)
        self.__cl = cl
        self.__desc = desc

    def getregstatus(self):
        return(self.__file.status)

    def getidstatus(self):
        print(self.__file.ids)

x = '87123449'
y = '009'
z = 'shirts'

t = FileStatus(x, y, z)
t.getregstatus()
t.getidstatus()
