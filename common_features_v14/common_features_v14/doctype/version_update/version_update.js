// Copyright (c) 2023, Thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Version Update', {
	refresh_indicator: function(frm) {
		if (frm.doc.refresh_indicator) {
			frm.set_value('maintenance_mode', 0)
		}
	},
	maintenance_mode: function(frm) {
		if (frm.doc.maintenance_mode) {
			frm.set_value('refresh_indicator', 0)
		}
	}
});
