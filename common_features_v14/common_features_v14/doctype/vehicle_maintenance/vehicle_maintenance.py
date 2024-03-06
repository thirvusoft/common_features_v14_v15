# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VehicleMaintenance(Document):
	def validate(self):
		odometer_update(self)


def odometer_update(self):
	if self.vehicle_no and self.service_done_at_odometer_value:
		vehicle = frappe.get_doc('Vehicle', self.vehicle_no)
		
		for service_detail in vehicle.custom_service_maintanence_details:
			service_detail.updated_odometer = self.service_done_at_odometer_value
			vehicle.save()