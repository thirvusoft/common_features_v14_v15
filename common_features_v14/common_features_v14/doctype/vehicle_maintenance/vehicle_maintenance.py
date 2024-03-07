# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VehicleMaintenance(Document):
	def on_submit(self):
		odometer_update(self)

	def on_cancel(self):
		odometer_cancel(self)


def odometer_update(self):
	if self.vehicle_no and self.service_done_at_odometer_value:
		vehicle = frappe.get_doc('Vehicle', self.vehicle_no)
		frappe.errprint(vehicle.custom_service_maintanence_details)
		for service_detail in vehicle.custom_service_maintanence_details:
			for det in self.maintenance_details:
				if service_detail.service_type == det.service_type:
					service_detail.updated_odometer = self.service_done_at_odometer_value
					vehicle.save()

def odometer_cancel(self):
	if self.vehicle_no:
		vehicle = frappe.get_doc('Vehicle', self.vehicle_no)

		for details in vehicle.custom_service_maintanence_details:
			for det in self.maintenance_details:
				if details.service_type == det.service_type:
					details.updated_odometer= vehicle.last_odometer
					vehicle.save()







