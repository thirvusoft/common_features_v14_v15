# Copyright (c) 2023, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_url_to_form,now_datetime
from datetime import datetime
class VersionUpdate(Document):
	def on_update(self):
		if self.message_display == 1:
			frappe.publish_realtime('custom-version_pre', {"link1":self.alert_message,"time":self.message_start_at})

		if self.maintenance_check == 1:
			frappe.publish_realtime('custom-version_maintenance', {"link2":self.maintenance_message})	
		if self.close_the_maintenance_mode == 1:
			frappe.publish_realtime('custom-version_success', {"link3":self.success_message})

# def on_update():
# 	# frappe.publish_realtime('custom-version-update', {"link":get_url_to_form(self.doctype, self.name)})
	
# 	doc_all = frappe.get_all("Version Update",{"maintenance_check":0,"message_start_at":["<=",now_datetime()]},pluck = "name")
# 	for i in doc_all:
# 		doc = frappe.get_doc("Version Update",i)
# 		if doc.close_the_maintenance_mode == 0:	
# 			frappe.publish_realtime('custom-version_maintenance', {"link2":doc.maintenance_message})
# 			doc.maintenance_check = 1
# 			doc.message_display = 0
# 			doc.save()
# 			doc.reload()

@frappe.whitelist()
def refresh_warning():
	doc = frappe.get_all("Version Update",{"message_display":1},["alert_message","message_start_at"])
	if doc:
		return doc[0].alert_message,doc[0].message_start_at

@frappe.whitelist()
def refresh_mainteance():
	doc = frappe.get_all("Version Update",{"maintenance_check":1},["maintenance_message"])
	if doc:
		return doc[0].maintenance_message
# @frappe.whitelist()
# def refresh_success():
# 	doc = frappe.get_all("Version Update",{"close_the_maintenance_mode":1},["success_message"])
# 	if doc:
# 		return doc[0].success_message