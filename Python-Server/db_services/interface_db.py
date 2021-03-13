from interface import Interface

class IDataBase(Interface):

    def db_init(self):
        pass
    
    def execute_query(self, str_query):
        pass