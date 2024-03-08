import frappe

def send_notification(doc,method):

    if doc.is_new():
        return

    users = frappe.get_all("User", filters={
        "enabled": 1,
        "role": ["in", ['Fleet Manager']]
    })


    maintenance_details = doc.custom_service_maintanence_details

    if maintenance_details:
        for maintenance in maintenance_details:
            if doc.last_odometer == maintenance.current_maintanence_odometer_value:
        
                if users:
                    for user in users:
                        notification_log = frappe.new_doc("Notification Log")
                        notification_log.subject = f"{doc.name}Vehicle Service Due"
                        notification_log.for_user = user.name
                        notification_log.type = "Alert"
                        notification_log.email_content = f"Vehicle Service Due date has arrived {doc.name}"
                        notification_log.from_user = "Administrator"
                        notification_log.save(ignore_permissions=True)
                    frappe.db.commit()






       
