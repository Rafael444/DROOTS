from flask import jsonify

from dao.food import FoodDAO


class FoodHandler:


    def build_food_dict(self, row):
        result = {}
        result['food_id'] = row[0]
        result['food_name'] = row[1]
        result['food_exp_date'] = row[2]
        result['food_type'] = row[3]
        result['food_description'] = row[4]
        result['resource_id'] = row[5]
        return result

    def build_food_attributes(self, food_id, food_name, food_exp_date, food_type, food_description, resource_id, food_date):
        result = {}
        result['food_id'] = food_id
        result['food_name'] = food_name
        result['food_exp_date'] = food_exp_date
        result['food_type'] = food_type
        result['food_description'] = food_description
        result['resource_id'] = resource_id
        result['food_date'] = food_date
        return result

    def getAllFood(self):
        dao = FoodDAO()
        food_list = dao.getAllFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)


    def getFoodById(self, food_id):
        dao = FoodDAO()
        row = dao.getFoodById(food_id)
        if not row:
            return jsonify(Error="Food Not Found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food=food)

    def getResourceById(self, resource_id):
        dao = FoodDAO()
        row = dao.getResourceById(resource_id)
        if row:
            result = self.build_food_dict(row)
        # jsonify(Food=food)
            return result

    def get_available_resources(self):
        dao = FoodDAO()
        resources_list = dao.get_available_resources()
        result_list = []
        for row in resources_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_supplied(self):
        dao = FoodDAO()
        resources_list = dao.get_resources_supplied()
        result_list = []
        for row in resources_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return result_list

    def get_resources_by_name(self, resource_name):
        dao = FoodDAO()
        food_list = []
        food_list = dao.get_resources_by_name(resource_name)
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return result_list

    def get_food_by_type(self, food_type):
        dao = FoodDAO()
        food_list = []
        food_list = dao.get_food_by_type(food_type)
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)


#----------------inserts------------------------------------------
    def insertFoodJson(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            food_name = form['food_name']
            food_exp_date = form['food_exp_date']
            food_type = form['food_type']
            food_description = form['food_description']
            food_date = form['food_date']
            if food_name and food_exp_date and food_type and food_description and food_date:
                dao = FoodDAO()
                food_and_resource_id = dao.insert_food(food_name, food_exp_date, food_type, food_description, food_date)
                result = self.build_food_attributes(food_and_resource_id[0], food_name, food_exp_date, food_type,
                                                    food_description, food_and_resource_id[1], food_date)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateFood(self, food_id, form):
        if not self.getFoodById(food_id):
            return jsonify(Error = "Food not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                food_name = form['food_name']
                food_quantity = form['food_quantity']
                food_exp_date = form['food_exp_date']
                food_type = form['food_type']
                food_description = form['food_description']
                if food_name and food_quantity and food_exp_date and food_type  and food_description:
                    self.update_food(food_id, food_name, food_quantity, food_exp_date, food_type, food_description)
                    result = self.build_food_attributes(food_id, food_name, food_quantity, food_exp_date, food_type,
                                                        food_description)
                    return jsonify(food=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteFood(self, food_id):
        if not self.getFoodById(food_id):
            return jsonify(Error="Food not found."), 404
        else:
            self.delete_food(food_id)
            return jsonify(DeleteStatus="OK"), 200

