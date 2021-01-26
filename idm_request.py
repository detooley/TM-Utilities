"""


"""
import requests
import json
import config

class IdmRequest():
    # Alllows users to set search string when instantiating
    def __init__(self, search='search-term=sex-dolls'):
        self.__queryidm(search)

    # Do a try-catch and retry wheb not 200
    def __queryidm(self, search):
        url = config.idm_api_url + '?' + search
        response = requests.get(url)
        # Set private variables used by other methods
        self.__jsonfile = response.json()
        dikt = json.loads(response.content)
        self.__dictfile = dikt['docs']

    # Returns entire JSON file
    @property
    def json(self):
        return self.__jsonfile

    # Returns entire file as a dictionary
    @property
    def dict(self):
        return self.__dictfile

# Sample usage
# idm = IdmRequest('search-term=crampons')
# print(idm.json)
