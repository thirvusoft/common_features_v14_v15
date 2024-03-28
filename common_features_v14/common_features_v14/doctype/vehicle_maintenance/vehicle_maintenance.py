# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VehicleMaintenance(Document):
	def on_submit(self):
		odometer_update(self)

	def on_cancel(self):
		odometer_cancel(self)
		  
	def validate(self):
		odometer_validate(self)

def odometer_update(self):
	if self.vehicle_no:
		vehicle = frappe.get_doc('Vehicle', self.vehicle_no) 
		for det in self.maintenance_details:
			for service_detail in vehicle.custom_service_maintanence_details:
				if service_detail.service_type == det.service_type:
					service_detail.current_maintanence_odometer_value = self.service_done_at_odometer_value
					service_detail.next_maintanence_odometer_value = self.service_done_at_odometer_value + det.next_service_odometer_frequency
					
		vehicle.save()
		frappe.db.set_value("Vehicle", self.vehicle_no, "last_odometer", self.service_done_at_odometer_value)


def odometer_cancel(self):
	if self.vehicle_no:
		vehicle = frappe.get_doc('Vehicle', self.vehicle_no)

		for details in vehicle.custom_service_maintanence_details:
			for det in self.maintenance_details:
				if details.service_type == det.service_type:
					details.current_maintanence_odometer_value= vehicle.last_odometer
					details.next_maintanence_odometer_value = det.next_service_odometer_frequency - self.service_done_at_odometer_value
		vehicle.save()
		frappe.db.set_value("Vehicle", self.vehicle_no, "last_odometer", self.service_done_at_odometer_value)

#Vehicle maintenance Doc filter

@frappe.whitelist()
def service_maintanence_details(vehicle_no):
	vehicle=frappe.get_doc('Vehicle',vehicle_no)
	ser_type=[]
	for i in vehicle.custom_service_maintanence_details:
		ser_type.append(i.service_type)
	return ser_type
	

def odometer_validate(self):
	 if self.service_done_at_odometer_value < self.current_odometer:
			 frappe.throw("Service done at Odometer value should be greater than Current Odometer")



