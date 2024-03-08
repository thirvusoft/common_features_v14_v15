import frappe

def send_notification(doc,method):

    if doc.is_new():
        return

    users = frappe.get_all("User", filters={
        "enabled": 1,
        "role": ["in", ['Fleet Manager']]
    })


    vehicles = frappe.get_all("Vehicle", fields=['name', 'last_odometer'])


    for vehicle in vehicles:
        vehicle_doc = frappe.get_doc("Vehicle", vehicle['name'])
        maintenance_details = vehicle_doc.get("custom_service_maintanence_details")

        if maintenance_details:
            for maintenance in maintenance_details:
                if vehicle.last_odometer == maintenance.updated_odometer:
			
                    if users:
                        for user in users:
                            notification_log = frappe.new_doc("Notification Log")
                            notification_log.subject = f"{vehicle.name}Vehicle Service Due"
                            notification_log.for_user = user.name
                            notification_log.type = "Alert"
                            notification_log.email_content = f"Vehicle Service Due date has arrived {vehicle.name}"
                            notification_log.from_user = "Administrator"
                            notification_log.save(ignore_permissions=True)
                        frappe.db.commit()






       
