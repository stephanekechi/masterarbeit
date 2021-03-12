from interface import implements
from db_services.interface_db import IDataBase

class DummyDB(implements(IDataBase)):
    userList = None

    def __init__(self):
        self.db_init()

    def db_init(self):
        self.userList = [
            {
                'username': 'ml_user',
                'password': 'masterarbeit21'
            },
            {
                'username': 'gast',
                'password': 'gast21'
            }
        ]

        print('Dummy Database is running!')

    def execute_query(self, str_query):
        result_query = []
        if(str_query == 'get'):
            result_query = self.userList
        elif(str_query == 'select'):
            # do something else
        return result_query