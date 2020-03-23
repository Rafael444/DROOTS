from flask import Flask, jsonify, request
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
from handler.Administrator import AdministratorsHandler
from handler.Customer import CustomerHandler
from handler.HeavyEquipment import HeavyEquipmentHandler
from handler.Request import RequestHandler
from handler.Reservation import ReservationHandler
from handler.food import FoodHandler
from handler.fuel import FuelHandler
from handler.power_resources import PowerResourcesHandler
from handler.user import UserHandler
from handler.clothing import ClothingHandler
from handler.tools import ToolsHandler
from handler.resources import ResourcesHandler


app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/droots/resources/', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResourceJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().search_resource(request.args)


@app.route('/droots/resources/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(resource_id)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResource(resource_id, request.json)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResource(resource_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/food', methods=['GET', 'POST'])
def getAllFood():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            return FoodHandler().search_food(request.args)


@app.route('/droots/resources/food/<int:food_id>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(food_id):
    if request.method == 'GET':
        return FoodHandler().getFoodById(food_id)
    elif request.method == 'PUT':
        return FoodHandler().updatePart(food_id, request.json)
    elif request.method == 'DELETE':
        return FoodHandler().deletePart(food_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)

    else:
        return UserHandler().getAllUsers()


@app.route('/droots/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(user_id):
    if request.method == 'GET':
        return UserHandler().getUserById(user_id)

    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.form)

    elif request.method == 'DELETE':
        return UserHandler().deleteUser(user_id)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/powerresources', methods=['GET', 'POST'])
def getAllPowerResources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PowerResourcesHandler().insertPowerResourceJson(request.json)

    else:
        if not request.args:
            return PowerResourcesHandler().getAllPowerResources()
        else:
            return PowerResourcesHandler().searchPowerResources(request.args)


@app.route('/droots/resources/powerresources/<int:power_resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getPowerResourceById(power_resource_id):
    if request.method == 'GET':
        return PowerResourcesHandler().getPowerResourceById(power_resource_id)

    elif request.method == 'PUT':
        return PowerResourcesHandler().updatePowerResource(power_resource_id, request.form)

    elif request.method == 'DELETE':
        return PowerResourcesHandler().deletePowerResource(power_resource_id)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/fuel', methods=['GET', 'POST'])
def getAllFuels():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)

    else:
        if not request.args:
            return FuelHandler().getAllFuels()
        else:
            return FuelHandler().searchFuels(request.args)


@app.route('/droots/resources/fuel/<int:fuel_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuel_id):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fuel_id)

    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuel_id, request.form)

    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuel_id)

    else:
        return jsonify(Error="Method not allowed."), 405



@app.route('/droots/resources/clothing', methods=['GET', 'POST'])
def getAllClothes():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return ClothingHandler().insertClotheJson(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllclothes()
        else:
            return ClothingHandler().search_clothes(request.args)


@app.route('/droots/resources/clothing/<int:clothe_id>', methods=['GET', 'PUT', 'DELETE'])
def getClotheById(clothe_id):
    if request.method == 'GET':
        return ClothingHandler().getClotheById(clothe_id)
    elif request.method == 'PUT':
        return ClothingHandler().updateClothe(clothe_id, request.json)
    elif request.method == 'DELETE':
        return ClothingHandler().deleteClothe(clothe_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/droots/resources/tools', methods=['GET', 'POST'])
def getAllTools():
        if request.method == 'POST':
            # cambie a request.json pq el form no estaba bregando
            # parece q estaba poseido por satanas ...
            # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
            print("REQUEST: ", request.json)
            return ToolsHandler().insertToolJson(request.json)
        else:
            if not request.args:
                return ToolsHandler().getAllTools()
            else:
                return ToolsHandler().search_tools(request.args)

@app.route('/droots/resources/tools/<int:tool_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tool_id):
        if request.method == 'GET':
            return ToolsHandler().getToolById(tool_id)
        elif request.method == 'PUT':
            return ToolsHandler().updateTool(tool_id, request.json)
        elif request.method == 'DELETE':
            return ToolsHandler().deleteTool(tool_id)
        else:
            return jsonify(Error="Method not allowed."), 405


@app.route('/droots/administrators', methods=['GET', 'POST'])
def getAllAdministrators():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AdministratorsHandler().insertAdministratorJson(request.json)

    else:
        return AdministratorsHandler().getAllAdministrators()


@app.route('/droots/administrators/<int:administrator_id>', methods=['GET', 'PUT', 'DELETE'])
def getAdministratorById(administrator_id):
    if request.method == 'GET':
        return AdministratorsHandler().getAdministratorById(administrator_id)

    elif request.method == 'PUT':
        return AdministratorsHandler().updateAdministrator(administrator_id, request.form)

    elif request.method == 'DELETE':
        return AdministratorsHandler().deleteAdministrator(administrator_id)

    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/droots/customer/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def getCustomerById(customer_id):
    if request.method == 'GET':
        return CustomerHandler().getCustomersById(customer_id)
    elif request.method == 'PUT':
        return CustomerHandler().updateCustomers(customer_id, request.form)
    elif request.method == 'DELETE':
        return CustomerHandler().deleteCustomers(customer_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/customer', methods=['GET', 'POST'])
def getAllCustomer():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CustomerHandler().insertCustomersJson(request.json)

    else:
        return CustomerHandler().getAllCustomers()


@app.route('/droots/customer/request/<int:request_id>', methods=['GET', 'POST','PUT'])
def getRequestById(request_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestHandler().insertRequestJson(request.json)
    elif request.method == 'GET':
        return RequestHandler().getAllRequest()
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(request_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/customer/reservation/<int:reservation_id>', methods=['GET', 'POST','PUT'])
def getReservationById(reservation_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReservationHandler().insertReservationJson(request.json)
    elif request.method == 'GET':
        return ReservationHandler().getReservationById(reservation_id)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(reservation_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/heavyequipment/', methods=['GET', 'POST',])
def getAllHEquipment():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HeavyEquipmentHandler().insertHEquipmentJson(request.json)
    elif request.method == 'GET':
        return HeavyEquipmentHandler().getAllHEquipment()

    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/droots/resources/heavyequipment/<int:hequipment_id>', methods=['GET', 'POST','PUT'])
def getRequestById(hequipment_id):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HeavyEquipmentHandler().insertHEquipmentJson(request.json)
    elif request.method == 'GET':
        return HeavyEquipmentHandler().getHEquipmentById(hequipment_id)
    elif request.method == 'PUT':
        return HeavyEquipmentHandler().updateHEquipment(hequipment_id, request.form)

    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run()
