from frappe.custom.doctype.property_setter.property_setter import make_property_setter
import frappe
def custom_field():
    custom_fields()
    
def custom_fields():
    make_property_setter("Customize Form Field", "print_hide", "label", "In List Preview", "Data")
    make_property_setter("Custom Field", "print_hide", "label", "In List Preview", "Data")
    make_property_setter("Task", "", "allow_auto_repeat", "1", "Check", for_doctype=True)