// Copyright (c) 2024, Thirvusoft and contributors
// For license information, please see license.txt

frappe.query_reports["Maintenance Details"] = {
	"filters": [{
		fieldname:"vehicle_no",
		label: __("ID"),
		fieldtype: "Link",
		options: "Vehicle"
	},
	{
		fieldname:"date",
		label: __("Date"),
		fieldtype: "Date"

	}

	]
};
