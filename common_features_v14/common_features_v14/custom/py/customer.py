import frappe

def customer_captalize(doc, action):
    doc.autoname()
    if doc.name:
        doc.name = (doc.name).title()
    if doc.customer_name:
        doc.customer_name=(doc.customer_name).title()