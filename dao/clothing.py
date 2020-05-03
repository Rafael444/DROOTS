from config.dbconfig import pg_config
import psycopg2


class ClothingDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select clothe_id, resource_name, clothe_type, clothe_description " \
                "from clothing natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingById(self, clothe_id):
        cursor = self.conn.cursor()
        query = "select clothe_id, resource_name, clothe_type, clothe_description " \
                "from clothing natural inner join resources where clothe_id = %s;"
        cursor.execute(query, (clothe_id,))
        result = cursor.fetchone()
        return result

    def get_available_resources(self):
        cursor = self.conn.cursor()
        query = "select clothe_id, resource_name, clothe_type, clothe_description " \
                "from clothing natural inner join resources;"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result