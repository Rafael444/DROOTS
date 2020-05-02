from flask import jsonify

from dao.water import WaterDAO


class WaterHandler:


    def build_water_dict(self, row):
        result = {}
        result['water_id'] = row[0]
        result['water_name'] = row[1]
        result['water_oz'] = row[2]
        result['water_type'] = row[3]
        return result

    def build_water_attributes(self, water_id, water_name, water_oz, water_type, water_description):
        result = {}
        result['water_id'] = water_id
        result['water_name'] = water_name
        result['water_oz'] = water_oz
        result['water_type'] = water_type
        return result

    def getAllWater(self):
        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)


    def getWaterById(self, water_id):
        dao = WaterDAO()
        row = dao.getWaterById(water_id)
        if not row:
            return jsonify(Error="Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water=water)