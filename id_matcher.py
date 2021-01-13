"""


"""
import requests
import json
import config

# jupyter notebook location: C:\Users\jimmy\Documents\GitHub\TM-Utilities

class IDMatcher():
    def __init__(self):
        self.id = 'dildos'
        self.url = config.id_api_site + self.id + '/info.json'


    # Allows user to change serial number
    # Do a try-catch and retry wheb not 200
    def __setfile(self, sernum):
        url = config.tsdr_api_url + sernum + '/info.json'
        response = requests.get(url, headers=config.tsdr_api_key)
        text = response.text
        dikt = json.loads(text)
        # Set private variables used by other methods
        self.__jsonfile = text
        self.__dictfile = dikt['trademarks'][0]

    # Methods for accessing data
    # Returns the complete JSON file
    @property
    def json(self):
        return self.__jsonfile

    # Returns the whole file in a dictionary
    @property
    def file(self):
        return self.__dictfile

    # Returns the descriptions of goods and services and their class numbers
    # in a dictionary
    @property
    def ids(self):
        gsids = {}
        for x in self.__dictfile['gsList']:
            gsids.update({x['primeClassCode']: x['description']})
        return(gsids)

    # Returns serial number
    @property
    def sernum(self):
        return(str(self.__dictfile['status']['serialNumber']))

    # Returns mark literal
    @property
    def mark(self):
        return(self.__dictfile['status']['markElement'])

    # Returns the registration status
    @property
    def status(self):
        return(str(self.__dictfile['status']['status']))

    @property
    def owner_name(self):
        return(self.__dictfile['parties']['ownerGroups']['10'][0]['name'])

#Sample usage:

serialnumber = '85359519'
tm = TsdrFile(serialnumber)
print(tm.mark)
