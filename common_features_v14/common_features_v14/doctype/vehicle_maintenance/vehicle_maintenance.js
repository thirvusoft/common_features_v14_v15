
frappe.ui.form.on('Maintenance Details', {
    labour_cost: function(frm, cdt, cdn) {
        calculateTotalValue(frm, cdt, cdn)
    },
    maintenance_cost: function(frm, cdt, cdn) {
        calculateTotalValue(frm, cdt, cdn)
    }
});

function calculateTotalValue(frm, cdt, cdn) {
    var child = locals[cdt][cdn]
    var total_value = child.labour_cost + child.maintenance_cost
    console.log(total_value)
    frappe.model.set_value(cdt, cdn, 'total_value', total_value)
}
