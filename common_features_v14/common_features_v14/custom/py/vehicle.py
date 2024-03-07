
import frappe

def send_notification():
    users = frappe.get_all("User", filters={
        "enabled": 1,
        "role": ["in", ['Fleet Manager']]
    })
    frappe.errprint("ednend")
    vehicle = frappe.get_all("Vehicle",fields=['last_odometer'])
    # for v in vehicle.custom_service_maintanence_details:
    #     if vehicle.last_odometer == v.updated_odometer:
			
	#         if users:
    #                 for user in users:
    #                     notification_log = frappe.new_doc("Notification Log")
    #                     notification_log.subject = "Vehicle Service Due"
    #                     notification_log.for_user = user.name
    #                     notification_log.type = "Alert"
    #                     notification_log.email_content = f"Vehicle Service Due date has arrived {vehicle}"
    #                     notification_log.from_user = "Administrator"
    #                     notification_log.save(ignore_permissions=True)
    #                 frappe.db.commit()