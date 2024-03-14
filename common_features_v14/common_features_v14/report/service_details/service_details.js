// Copyright (c) 2024, Thirvusoft and contributors
// For license information, please see license.txt


frappe.query_reports["Service Detailss"] = {
	"filters": [{
		fieldname:"name",
		label: __("ID"),
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
