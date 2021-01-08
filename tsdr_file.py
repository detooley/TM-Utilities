"""


"""
import requests
import json
import config

class TsdrFile():
    # Alllows users to set serial number when instantiating
    # Includes a demo serial number for lazy people
    def __init__(self, sernum=['88855299']):
        self.setfile(sernum)

    # Allows user to change serial number
    # Do a try-catch and retry wheb not 200
    def setfile(self, sernum):
        for x in sernum:
            # TODO: fix url to read sernum from a list
            url = config.tsdr_api_url + sernum + '/info.json'
            response = requests.get(url, headers=config.tsdr_api_key)
            text = response.text
            # the following reads more cleanly
            dikt = json.loads(response.content)
            # Set private variables used by other methods
            self.__jsonfile = text
            self.__dictfile = dikt['trademarks'][0]

            # returning dictionary for testing purposes
            return dikt['trademarks'][0]

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

    # Returns the owner name
    # DAVE, what's with the weird ownergroup data, e.g., '10'?
    @property
    def owner_name(self):
        return(self.__dictfile['parties']['ownerGroups']['10'][0]['name'])

#Sample usage:

#serialnumber = '90100124'
#tm = TsdrFile(serialnumber)
#print(tm.ids)
