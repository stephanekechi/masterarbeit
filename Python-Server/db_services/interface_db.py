from interface import Interface

class IDataBase(Interface):

    def connect(self, host_infos):
        pass
    
    def execute_query(self, str_query):
        pass