import frappe

def item_captalize(doc, action=None):
    doc.autoname()
    if doc.item_code:
        doc.item_code=(doc.item_code).title()
    if doc.name:
        doc.name = (doc.name).title()
    if doc.item_name:
         doc.item_name=(doc.item_name).title()