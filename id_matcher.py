"""


"""
import requests
import json
import config

# jupyter notebook location: C:\Users\jimmy\Documents\GitHub\TM-Utilities

class IDMatcher():
    def __init__(self, id = 'dildos'):
        self.id = id
        self.url = config.id_api_site + self.id + '/info.json'
        self.response = requests.get(self.url, headers=config.tsdr_api_key)
        self.text = self.response.text
        self.dikt = json.loads(self.text)

        self.serial_list = self.app_builder()

    # Build list of serial numbers with identical IDs
    def app_builder(self):
        identical_list = []

        # TODO: length seems capped at 100?
        dikt_length = len(self.dikt['response']['docs'])
        if dikt_length == 0:
            return
        # Retrieve the first serial number of identical g/s
        serial = self.dikt['response']['docs'][0]['uspto_tm_document']['trademark_case_files']['trademark_case_file']['case_file_header']['serial_number']
        # identical_list.append(serial)
        for app in range(dikt_length):
            serial = self.dikt['response']['docs'][app]['uspto_tm_document']['trademark_case_files']['trademark_case_file']['case_file_header']['serial_number']

            identical_list.append(serial)

        return identical_list


    # Allows user to change serial number
    # Do a try-catch and retry wheb not 200
#     def __setfile(self, sernum):
#         url = config.tsdr_api_url + sernum + '/info.json'
#         response = requests.get(url, headers=config.tsdr_api_key)
#         text = response.text
#         dikt = json.loads(text)
#         # Set private variables used by other methods
#         self.__jsonfile = text
#         self.__dictfile = dikt['trademarks'][0]
#
#     # Methods for accessing data
#     # Returns the complete JSON file
#     @property
#     def json(self):
#         return self.__jsonfile
#
#     # Returns the whole file in a dictionary
#     @property
#     def file(self):
#         return self.__dictfile
#
#     # Returns the descriptions of goods and services and their class numbers
#     # in a dictionary
#     @property
#     def ids(self):
#         gsids = {}
#         for x in self.__dictfile['gsList']:
#             gsids.update({x['primeClassCode']: x['description']})
#         return(gsids)
#
#     # Returns serial number
#     @property
#     def sernum(self):
#         return(str(self.__dictfile['status']['serialNumber']))
#
#     # Returns mark literal
#     @property
#     def mark(self):
#         return(self.__dictfile['status']['markElement'])
#
#     # Returns the registration status
#     @property
#     def status(self):
#         return(str(self.__dictfile['status']['status']))
#
#     @property
#     def owner_name(self):
#         return(self.__dictfile['parties']['ownerGroups']['10'][0]['name'])
#
# #Sample usage:
#
# serialnumber = '85359519'
# tm = TsdrFile(serialnumber)
# print(tm.mark)
