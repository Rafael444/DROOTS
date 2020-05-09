from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class HealthDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)
        self.select_statement = "select health_id, resource_name, health_exp_date, health_type, health_description, resource_id " \


    def getAllHealth(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from health natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHealthById(self, health_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from health natural inner join resources where health_id = %s;"
        cursor.execute(query, (health_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from health natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from health natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join health;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from health natural inner join resources where resource_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    #---------------inserts---------------------------------------------------------------------

    # def insert_resource(self, resource_category, resource_quantity):
    #     cursor = self.conn.cursor()
    #     query = "insert into resources(resource_category, resource_availability) values (%s, %s) returning resource_id;"
    #     cursor.execute(query, (resource_category, resource_quantity,))
    #     resource_id = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return resource_id

    def insert_health(self, resource_name, health_exp_date, health_type, health_description):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'health')
        cursor = self.conn.cursor()
        query = "insert into health(health_name, health_exp_date, health_type, health_description, resource_id) values (%s, %s, %s, %s) returning health_id;"
        cursor.execute(query, (health_exp_date, health_type, health_description, resource_id))
        health_id = cursor.fetchone()[0]
        self.conn.commit()
        return health_id, resource_id
    #
    # def get_available_resources(self):
    #     cursor = self.conn.cursor()
    #     query = "select health_id, health_name, health_exp_date, health_type, health_description, resource_availability " \
    #             "from health natural inner join resources " \
    #             "where resource_availability > 0;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

