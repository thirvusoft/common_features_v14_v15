# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt


import frappe


def execute(filters=None):
    columns = [
        {"label": "Vehicle No", "fieldname": "vehicle_no", "fieldtype": "Link", "options": "Vehicle"},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date"},
        {"label": "Service Done at Odometer Value", "fieldname": "service_done_at_odometer_value", "fieldtype": "Float"},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data"},
        {"label": "Labour Cost", "fieldname": "labour_cost", "fieldtype": "Float"},
        {"label": "Maintenance Cost", "fieldname": "maintenance_cost", "fieldtype": "Float"},
        {"label": "Total Value", "fieldname": "total_value", "fieldtype": "Float"},
        {"label": "Serviced By", "fieldname": "serviced_by","fieldtype": "Data" }
    ]
    
    conditions = []
    if filters and filters.get("vehicle_no"):
        conditions.append("`tabVehicle Maintenance`.`vehicle_no` = '{0}'".format(filters.get("vehicle_no")))
        
    if filters and filters.get("date"):
        conditions.append("`tabVehicle Maintenance`.`date` = '{0}'".format(filters.get("date")))

    if filters and filters.get("service_type"):
          conditions.append("`tabMaintenance Details`.`service_type` = '{0}'".format(filters.get("service_type")))

    query= """
        SELECT
            `tabVehicle Maintenance`.`vehicle_no` AS vehicle_no,
            `tabVehicle Maintenance`.`date` AS date,
            `tabVehicle Maintenance`.`service_done_at_odometer_value` AS service_done_at_odometer_value,
            `tabMaintenance Details`.`service_type` AS service_type,
            `tabMaintenance Details`.`labour_cost` AS labour_cost,
            `tabMaintenance Details`.`maintenance_cost` AS maintenance_cost,
            `tabMaintenance Details`.`total_value` AS total_value,
            `tabMaintenance Details`.`serviced_by` AS serviced_by

        FROM
            `tabVehicle Maintenance`
        LEFT JOIN
            `tabMaintenance Details` ON `tabVehicle Maintenance`.`name` = `tabMaintenance Details`.`parent`
    """
    
    if conditions:
              query+= "WHERE" + "AND".join(conditions)
    data =frappe.db.sql(query,as_dict=True)	

    return columns, data