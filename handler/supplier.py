from flask import jsonify

from dao.address import AddressDAO
from dao.email import EmailDAO
from dao.phone import PhoneDAO
from dao.supplier import SupplierDAO
from dao.users import UsersDAO


class SupplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['user_id'] = row[1]
        result['supplier_fname'] = row[2]
        result['supplier_lname'] = row[3]
        result['supplier_uname'] = row[4]
        result['supplier_passwd'] = row[5]
        result['supplier_country'] = row[6]
        result['supplier_city'] = row[7]
        result['supplier_street_address'] = row[8]
        result['supplier_zipcode'] = row[9]
        result['supplier_phone'] = row[10]
        result['supplier_email'] = row[11]
        return result

    def build_supplier_attributes(self, supplier_id, user_id, user_fname, user_lname,
                                  user_uname, user_passwd, supplier_country, supplier_city,
                                  supplier_street_address, supplier_zipcode, supplier_phone,
                                  supplier_email):
        result = {}
        result['supplier_id'] = supplier_id
        result['user_id'] = user_id
        result['supplier_fname'] = user_fname
        result['supplier_lname'] = user_lname
        result['supplier_uname'] = user_uname
        result['supplier_passwd'] = user_passwd
        result['supplier_country'] = supplier_country
        result['supplier_city'] = supplier_city
        result['supplier_street_address'] = supplier_street_address
        result['supplier_zipcode'] = supplier_zipcode
        result['supplier_phone'] = supplier_phone
        result['supplier_email'] = supplier_email
        return result

    def getAllSupplier(self):
        sdao = SupplierDAO()
        result_list = []
        for row in sdao.getAllSuppliers():
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)

    def getSupplierById(self, supplier_id):
        sdao = SupplierDAO()
        row = sdao.getSupplierById(supplier_id)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)

    def insertSupplierJson(self, json):
        print("json: ", json)
        if len(json) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            supplier_fname = json['supplier_fname']
            supplier_lname = json['supplier_lname']
            supplier_uname = json['supplier_uname']
            supplier_passwd = json['supplier_passwd']
            supplier_country = json['supplier_country']
            supplier_city = json['supplier_city']
            supplier_street_address = json['supplier_street_address']
            supplier_zipcode = json['supplier_zipcode']
            supplier_phone = json['supplier_phone']
            supplier_email = json['supplier_email']
            if supplier_fname and supplier_lname and supplier_uname and supplier_passwd and supplier_country \
                    and supplier_city and supplier_street_address and supplier_zipcode and supplier_phone and \
                    supplier_email:
                udao = UsersDAO()
                sdao = SupplierDAO()
                addao = AddressDAO()
                pdao = PhoneDAO()
                edao = EmailDAO()
                user_id = udao.insert(supplier_fname, supplier_lname, supplier_uname, supplier_passwd)
                supplier_id = sdao.insert(user_id)
                addao.insert(supplier_country, supplier_city, supplier_street_address,
                             supplier_zipcode, user_id)
                pdao.insert(supplier_phone, user_id)
                edao.insert(supplier_email, user_id)
                result = self.build_supplier_attributes(supplier_id, user_id, supplier_fname, supplier_lname,
                                                        supplier_uname, supplier_passwd, supplier_country,
                                                        supplier_city, supplier_street_address, supplier_zipcode,
                                                        supplier_phone, supplier_email)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
