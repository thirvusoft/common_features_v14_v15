# Copyright (c) 2023, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VersionUpdate(Document):
	def validate_maintenance_mode(self):
		active_maint_modes = frappe.db.sql(f"""
			SELECT 
				vu.name
			FROM `tabVersion Update` vu
			WHERE
				vu.name != '{self.name}' AND
				vu.close_the_maintenance_mode = 0 AND
				(	
				    vu.under_maintenance_mode = 1 OR
				    vu.maintenance_mode_warning_message = 1
				)
		""" ,as_dict = True)

		if active_maint_modes:
			frappe.throw(f"""
					Please Close the active maintenance mode before opening new maintenance mode<br>
					<ul>
						{"".join([f'''<li><a href="/app/version-update/{mm.name}">{mm.name}</a></li>''' for mm in active_maint_modes])}
					</ul>
					""")

	def validate(self):
		if self.maintenance_mode_warning_message or self.under_maintenance_mode or self.close_the_maintenance_mode:
			self.validate_maintenance_mode()

		if not frappe.db.exists(self.doctype, self.name):
			self.publish_update = True
			return
		
		org_doc = frappe.get_doc(self.doctype, self.name)
		if self.maintenance_mode_warning_message != org_doc.maintenance_mode_warning_message or self.under_maintenance_mode!=org_doc.under_maintenance_mode or self.close_the_maintenance_mode != org_doc.close_the_maintenance_mode:
			self.publish_update = True
		
		elif self.pre_warning_message != org_doc.pre_warning_message or self.maintenance_mode_message!=org_doc.maintenance_mode_message:
			self.publish_update = True
		elif self.details != org_doc.details:
			self.publish_update = True
		else:
			self.publish_update = False

	def on_update(self):
		if self.publish_update:
			self.update_maintenance_mode()
			frappe.db.set_value(self.doctype, self.name, 'publish_update', 0, update_modified=False)
			self.reload()

	def on_trash(self):
		if not self.close_the_maintenance_mode and (self.under_maintenance_mode or self.maintenance_mode_warning_message or self.details):
			self.clear_maintenance_mode()
			frappe.msgprint("Maintenance mode message cleared.")

	def update_maintenance_mode(self):
		css_indicators = {
			'green': 'indicator-pill green',
			'orange': 'indicator-pill orange',
			'red': 'indicator-pill red',
			'blue': 'indicator-pill blue'
		}
		if self.close_the_maintenance_mode:
			frappe.publish_realtime('custom-version-update', {'message': self.success_message, 'refresh_button': True, 'indicator': css_indicators.get('green')})
		
		elif self.under_maintenance_mode:
			frappe.publish_realtime('custom-version-update', {'message': self.maintenance_mode_message, 'refresh_button': False, 'indicator': css_indicators.get('red')})
		
		elif self.maintenance_mode_warning_message:
			frappe.publish_realtime('custom-version-update', {'message': self.pre_warning_message, 'refresh_button': False, 'indicator': css_indicators.get('orange')})
		
		elif self.details:
			frappe.publish_realtime('custom-version-update', {'message': self.details, 'refresh_button': True, 'indicator': css_indicators.get('blue')})
		
		else:
			self.clear_maintenance_mode()
	
	def clear_maintenance_mode(self):
		frappe.publish_realtime('clear-custom-version-update')

def update_maintenance_mode_on():
	docs = frappe.db.sql("""
		SELECT
		    vu.name
		FROM `tabVersion Update` vu
		WHERE
			vu.maintenance_mode_warning_message = 1 AND
			IFNULL(vu.maintenance_mode_on_at, '') != '' AND
			vu.maintenance_mode_on_at <= NOW() AND
			vu.under_maintenance_mode = 0 AND
			vu.close_the_maintenance_mode = 0
	""", as_dict=True)

	for doc in docs:
		doc = frappe.get_doc('Version Update', doc.name)
		doc.under_maintenance_mode = True
		try:
			doc.save()
		except:
			frappe.log_error()

@frappe.whitelist()
def check_maintenance_mode():
	active = []
	try:
		css_indicators = {
				'green': 'indicator-pill green',
				'orange': 'indicator-pill orange',
				'red': 'indicator-pill red',
				'blue': 'indicator-pill blue'
			}
		active = frappe.db.sql(f"""
				SELECT 
					CASE 
						WHEN vu.under_maintenance_mode = 1
							THEN IFNULL(vu.maintenance_mode_message, '')
						ELSE IFNULL(vu.pre_warning_message, '')
					END as message,
					0 as refresh_button,
					CASE 
						WHEN vu.under_maintenance_mode = 1
							THEN "{css_indicators.get('red') or ''}"
						ELSE "{css_indicators.get('orange') or ''}"
					END as indicator
				FROM `tabVersion Update` vu
				WHERE
					vu.close_the_maintenance_mode = 0 AND
					(	
						vu.under_maintenance_mode = 1 OR
						vu.maintenance_mode_warning_message = 1
					)
				LIMIT 1
			""" ,as_list = True)
	except:
		frappe.log_error()
	if active:
		return active[0]
	