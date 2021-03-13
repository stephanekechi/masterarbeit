from interface import implements
import mysql.connector
from db_services.interface_db import IDataBase

class MySqlDB(implements(IDataBase)):
    mysqlConnection = None
    myslq_cursor = None

    """
    templateDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password123",
        database = "mldb"
    )"""

    def __init__(self, host_infos):
        self.mysqlConnection = mysql.connector.connect(
            host = host_infos["host"],
            user = host_infos["user"],
            passwd = host_infos["passwd"]
        )
        self.myslq_cursor = this.mysqlConnection.cursor()
        self.db_init()

    def execute_query(self, str_query, query_type=''):
        if(query_type == 'insert'):
            self.myslq_cursor.execute(str_query)
            self.mysqlConnection.commit()

        elif(query_type == 'select'):
            self.myslq_cursor.execute(str_query)
            result = self.myslq_cursor.fetchall()
            result_array = []

            for row in result:
                json = {
                    "id" : row[0],
                    "username" : row[1]
                }
                result_array.append(json)
            
            return result_array

        else: self.myslq_cursor.execute(str_query)

    def db_init(self):
        new_db_query = "CREATE database IF NOT EXISTS `mldb`;"
        self.execute_query(new_db_query)
        self.execute_query("USE `mldb`")

        new_table_query = "CREATE TABLE IF NOT EXISTS `users` ( \
        `id` int(5) NOT NULL AUTO_INCREMENT PRIMARY KEY (`id`), \
        `username` VARCHAR(250)  NOT NULL, \
        `password` VARCHAR(250)  NOT NULL )"
        
        self.execute_query(new_table_query)

        insert_users_query = "INSERT INTO `users` (`username`, `password`) \
        SELECT 'admin','admin2021' \
        WHERE NOT EXISTS (Select `username` From `users` WHERE `username` ='admin') LIMIT 1;"
        this.execute_query(insert_users_query, 'insert')

