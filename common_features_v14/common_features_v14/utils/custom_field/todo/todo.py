from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
def todo():
    setup_fields()
def setup_fields():
    custom_fields = {
        'ToDo':[
            dict(
                fieldname= "is_auto_repeat",
                fieldtype= "Check",
                label= "is Auto Repeat",
                insert_after= "priority",
                no_copy= 1,
                read_only_depends_on= "eval:doc.ref_auto_repeat && !doc.__islocal",
            ),
            dict(
                fieldname= "auto_repeat_section",
                fieldtype= "Section Break",
                insert_after= "allocated_to",
                label= "Auto Repeat",
                depends_on= "eval:doc.is_auto_repeat",
                collapsible= 1,
            ),
            dict(
                fieldname= "frequency",
                fieldtype= "Select",
                insert_after= "auto_repeat_section",
                label= "Frequency",
                mandatory_depends_on= "eval:doc.is_auto_repeat",
                no_copy= 1,
                options= "\nDaily\nWeekly\nMonthly\nQuarterly\nHalf-yearly\nYearly",
            ),
            dict(
                fieldname= "repeat_on_day",
                fieldtype= "Int",
                insert_after= "frequency",
                label= "Repeat on Day",
                no_copy= 1,
                depends_on= "eval: in_list([\"Monthly\", \"Quarterly\", \"Half-yearly\", \"Yearly\"], doc.frequency) && !doc.repeat_on_last_day",
            ),
            dict(
                fieldname= "repeat_on_last_day",
                fieldtype= "Check",
                insert_after= "repeat_on_day",
                label= "Repeat on Last Day of the Month",
                no_copy= 1,
                depends_on= "eval:doc.frequency === 'Monthly'",
            ),
            dict(
                fieldname= "repeat_on_days",
                fieldtype= "Table",
                insert_after= "repeat_on_last_day",
                label= "Repeat on Days",
                no_copy= 1,
                depends_on= "eval:doc.frequency==='Weekly';",
                options= "Task Auto Repeat Day",
            ),
            dict(
                fieldname= "column_break_bmj8g",
                fieldtype= "Column Break",
                insert_after= "repeat_on_days",
            ),
            dict(
                fieldname= "ref_auto_repeat",
                fieldtype= "Link",
                hidden= 1,
                insert_after= "end_date_",
                label= "Ref Auto Repeat",
                no_copy= 1,
                options= "Auto Repeat",
            ),
            dict(
                fieldname= "view_auto_repeat_details",
                fieldtype= "Button",
                insert_after= "ref_auto_repeat",
                label= "Go to Auto Repeat Document",
                depends_on= "eval:doc.ref_auto_repeat",
            ),
            dict(
                fieldname= "disabled",
                fieldtype= "Check",
                insert_after= "view_auto_repeat_details",
                label= "Disabled",
                no_copy= 1,
                depends_on= "eval:!doc.__islocal",
            ),
            dict(
                fieldname= "start_date_",
                fieldtype= "Date",
                insert_after= "column_break_bmj8g",
                label= "Start Date ",
                no_copy= 1,
                default="Today"
            ),
            dict(
                fieldname= "end_date_",
                fieldtype= "Date",
                insert_after= "start_date_",
                label= "End Date ",
                no_copy= 1,
            ),
            dict(
                fieldname= "auto_repeat_schedule",
                fieldtype= "Section Break",
                insert_after= "disabled",
                label= "Auto Repeat Schedule",
                depends_on= "eval:doc.ref_auto_repeat && !doc.disabled",
                collapsible= 1,
            ),
            dict(
                fieldname= "auto_repeat_schedule_html",
                fieldtype= "HTML",
                insert_after= "auto_repeat_schedule",
                label= "Auto Repeat Schedule Html",
                no_copy= 1,
            ),
        ]
    }
    create_custom_fields(custom_fields)