# Copyright (c) 2023, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_url_to_form

class VersionUpdate(Document):
	def on_update(self):
		frappe.publish_realtime('custom-version-update', {"link":get_url_to_form(self.doctype, self.name)})
