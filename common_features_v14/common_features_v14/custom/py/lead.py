import frappe

def lead_captalize(doc, action):
    if doc.name:
        doc.name = (doc.name).title()
    if doc.first_name:
        doc.first_name=(doc.first_name).title()
    if doc.middle_name:
         doc.middle_name=(doc.middle_name).title()
    if doc.last_name:
         doc.last_name=(doc.last_name).title()
    if doc.lead_name:
         doc.lead_name=(doc.lead_name).title()