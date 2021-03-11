from db_services.interface_db import IDataBase

class MySqlDB(implements(IDataBase)):
    mysqlConnection = None

    def __init__(self, host_infos):
        this.mysqlConnection = ...