from config.dbconfig import pg_config
import psycopg2

from dao.resources import ResourcesDAO


class WaterDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)
        self.select_statement = "select water_id, resource_name, water_oz, water_type, resource_id "

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterById(self, water_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources where water_id = %s;"
        cursor.execute(query, (water_id,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_supplied(self):
        cursor = self.conn.cursor()
        query = self.select_statement + "from suppliers natural inner join supplies natural inner join resources natural inner join water;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_resources_by_name(self, resource_name):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources where resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_water_by_type(self, water_type):
        cursor = self.conn.cursor()
        query = self.select_statement + "from water natural inner join resources where water_type = %s;"
        cursor.execute(query, (water_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_water(self, resource_name, water_oz, water_type, resource_date):
        resource_id = ResourcesDAO().insert_resource(resource_name, 'water', resource_date)
        cursor = self.conn.cursor()
        query = "insert into water(water_oz, water_type, resource_id) values (%s, %s, %s) returning water_id;"
        cursor.execute(query, (water_oz, water_type, resource_id))
        water_id = cursor.fetchone()[0]
        self.conn.commit()
        return water_id, resource_id
