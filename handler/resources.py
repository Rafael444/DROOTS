from flask import jsonify


class ResourcesHandler:

    resources = [(1, "baby food","false"),
                      (2, "tool","true")]

    #----------------utils-------------------
    def give_me_resource(self):
        return self.resources

    def getById(self, resource_id):
        for f in self.resources:
            if resource_id == f[0]:
                return f

    def insert_resource(self, resource_category, resource_availability):
        self.resources.append((len(self.resources) + 1, resource_category, resource_availability))
        return len(self.resources)

    def update_resource(self, resource_id, resource_category, resource_availability):
        self.resources.pop(resource_id-1)
        self.resources.insert(resource_id-1, (resource_id, resource_category, resource_availability))

    def delete_part(self, resource_id):
        self.resources.pop(resource_id - 1)
    #--------------end utils-----------------

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['resource_category'] = row[1]
        result['resource_availability'] = row[2]
        return result

    def build_part_attributes(self, resource_id, resource_category, resource_availability):
        result = {}
        result['resource_id'] = resource_id
        result['resource_category'] = resource_category
        result['resource_availability'] = resource_availability
        return result

    def getAllResources(self):
        # dao = SupplierDAO()
        # suppliers_list = dao.getAllSuppliers()
        flist = self.give_me_resource()
        result_list = []
        for row in flist:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceById(self, resource_id):
        # dao = PartsDAO()
        # row = dao.getPartById(pid)
        row = self.getById(resource_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def insertResourceJson(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            resource_category = form['resource_category']
            resource_availability = form['resource_availability']
            if resource_category and resource_availability:
                # dao = PartsDAO()
                # pid = dao.insert(pname, pcolor, pmaterial, pprice)
                resource_id = self.insert_resource(resource_category, resource_availability)
                result = self.build_resource_attributes(resource_id,resource_category,resource_availability )
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateResource(self, resource_id, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getResourceById(resource_id):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                resource_category = form['resource_category']
                resource_availability = form['resource_availability']
                if resource_category and resource_availability:
                    # dao.update(pid, pname, pcolor, pmaterial, pprice)
                    self.update_resource(resource_id, resource_category, resource_availability)
                    result = self.build_part_attributes(resource_id, resource_category, resource_availability)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteResource(self, resource_id):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        if not self.getResourceById(resource_id):
            return jsonify(Error="Part not found."), 404
        else:
            # dao.delete(pid)
            self.delete_part(resource_id)
            return jsonify(DeleteStatus="OK"), 200