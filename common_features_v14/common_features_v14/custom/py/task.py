import frappe
def auto_repeat(doc,action):
    if doc.is_auto_repeat:
        if doc.frequency and not doc.ref_auto_repeat:
            auto_repeat_doc = frappe.get_doc({
                'doctype':'Auto Repeat',
                'disabled':doc.disabled,
                'reference_doctype':"Task",
                'reference_document':doc.name,
                'frequency':doc.frequency,
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
            auto_repeat_doc.repeat_on_day = doc.repeat_on_day or ''
            auto_repeat_doc.repeat_on_last_day = doc.repeat_on_last_day or 0
            auto_repeat_doc.repeat_on_days =[]
            if doc.repeat_on_days and doc.frequency == "Weekly":
                for i in doc.repeat_on_days:
                    auto_repeat_doc.append("repeat_on_days",dict(
                        day = i.day
                    ))
            auto_repeat_doc.save(ignore_permissions = True)