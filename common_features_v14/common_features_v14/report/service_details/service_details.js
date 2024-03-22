// Copyright (c) 2024, Thirvusoft and contributors
// For license information, please see license.txt


frappe.query_reports["Service Details"] = {
	"filters": [{
		fieldname:"name",
		label: __("Vehicle No"),
		fieldtype: "Link",
		options: "Vehicle",
	},
	{
		fieldname:"service_type",
		label: __("Service Type"),
		fieldtype: "Link",
		options:"Service Type"
	}
	]
};
