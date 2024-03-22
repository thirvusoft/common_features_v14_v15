# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt



import frappe

def execute(filters=None):
    columns = [
        {"label": "Vehicle No", "fieldname": "name", "fieldtype": "Link", "options": "Vehicle"},
        {"label": "Current Odometer" , "fieldname":"current_maintanence_odometer_value", "fieldtype":"Float"},
        {"label": "Service done at Odometer" , "fieldname":"service_done_at_odometer_value", "fieldtype":"Float"},
        {"label": "Next Maintenance Odometer", "fieldname": "next_maintanence_odometer_value", "fieldtype": "Data"},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data"}
    ]

    conditions = []
    if filters.get("name"):
        conditions.append("vehicle.name = '{0}'".format(filters.get("name")))
    if filters.get("service_type"):
        conditions.append("service_details.service_type = '{0}'".format(filters.get("service_type")))


    query = """
    SELECT
        vehicle.name AS name,
        service_details.current_maintanence_odometer_value,
        service_details.next_maintanence_odometer_value,
        vehicle_maintenance.service_done_at_odometer_value,
        service_details.service_type
    FROM
        `tabVehicle` AS vehicle
    INNER JOIN
        `tabService Details` AS service_details ON vehicle.name = service_details.parent
    LEFT JOIN
        `tabVehicle Maintenance` AS vehicle_maintenance ON vehicle.name = vehicle_maintenance.vehicle_no
    """




    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    data = frappe.db.sql(query, as_dict=True)

    return columns, data