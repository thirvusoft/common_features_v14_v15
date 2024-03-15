# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt


import frappe


def execute(filters=None):
    columns = [
        {"label": "Vehicle No", "fieldname": "vehicle_no", "fieldtype": "Link", "options": "Vehicle"},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date"},
        {"label": "Service Done at Odometer Value", "fieldname": "service_done_at_odometer_value", "fieldtype": "Float"},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data"}
    ]
    
    conditions = []
    if filters and filters.get("vehicle_no"):
        conditions.append("`tabVehicle Maintenance`.`vehicle_no` = '{0}'".format(filters.get("vehicle_no")))
        
    if filters and filters.get("date"):
        conditions.append("`tabVehicle Maintenance`.`date` = '{0}'".format(filters.get("date")))


    query= """
        SELECT
            `tabVehicle Maintenance`.`vehicle_no` AS vehicle_no,
            `tabVehicle Maintenance`.`date` AS date,
            `tabVehicle Maintenance`.`service_done_at_odometer_value` AS service_done_at_odometer_value,
            `tabMaintenance Details`.`service_type` AS service_type
        FROM
            `tabVehicle Maintenance`
        LEFT JOIN
            `tabMaintenance Details` ON `tabVehicle Maintenance`.`name` = `tabMaintenance Details`.`parent`
    """
    
    if conditions:
              query+= "WHERE" + "AND".join(conditions)
    data =frappe.db.sql(query,as_dict=True)	

    return columns, data