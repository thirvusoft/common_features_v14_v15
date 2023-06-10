import json
import frappe
def auto_repeat(doc,action):
    if doc.is_auto_repeat:
        if doc.frequency and not doc.ref_auto_repeat:
            auto_repeat_doc = frappe.get_doc({
                'doctype':'Auto Repeat',
                'disabled':doc.disabled,
                'reference_doctype':doc.doctype,
                'reference_document':doc.name,
                'frequency':doc.frequency,
                'start_date' : doc.start_date_,
                'end_date' : doc.end_date_,
                'repeat_on_day':doc.repeat_on_day or '',
                'repeat_on_last_day':doc.repeat_on_last_day or 0,
            })
            if doc.repeat_on_days:
                for i in doc.repeat_on_days:
                    auto_repeat_doc.append("repeat_on_days",dict(
                        day = i.day
                    ))
            auto_repeat_doc.save(ignore_permissions = True)

            doc.ref_auto_repeat = auto_repeat_doc.name
        elif doc.ref_auto_repeat:
            auto_repeat_doc = frappe.get_doc('Auto Repeat',doc.ref_auto_repeat)
            auto_repeat_doc.disabled = doc.disabled
            auto_repeat_doc.frequency = doc.frequency
            auto_repeat_doc.start_date = doc.start_date_
            auto_repeat_doc.end_date = doc.end_date_
            auto_repeat_doc.repeat_on_day = doc.repeat_on_day or ''
            auto_repeat_doc.repeat_on_last_day = doc.repeat_on_last_day or 0
            auto_repeat_doc.repeat_on_days =[]
            if doc.repeat_on_days and doc.frequency == "Weekly":
                for i in doc.repeat_on_days:
                    auto_repeat_doc.append("repeat_on_days",dict(
                        day = i.day
                    ))
            auto_repeat_doc.save(ignore_permissions = True)
from frappe.utils import (
	getdate
)
@frappe.whitelist()
def get_auto_repeat_schedule(self = None):
    if(self):
        self= frappe.get_doc("Auto Repeat",self)
        schedule_details = []
        start_date = getdate(self.start_date)
        end_date = getdate(self.end_date)

        if not self.end_date:
            next_date = self.get_next_schedule_date(schedule_date=start_date)
            row = {
                "reference_document": self.reference_document,
                "frequency": self.frequency,
                "next_scheduled_date": next_date,
            }
            schedule_details.append(row)

        if self.end_date:
            next_date = self.get_next_schedule_date(schedule_date=start_date, for_full_schedule=True)

            while getdate(next_date) < getdate(end_date):
                row = {
                    "reference_document": self.reference_document,
                    "frequency": self.frequency,
                    "next_scheduled_date": next_date,
                }
                schedule_details.append(row)
                next_date = self.get_next_schedule_date(schedule_date=next_date, for_full_schedule=True)

        return schedule_details