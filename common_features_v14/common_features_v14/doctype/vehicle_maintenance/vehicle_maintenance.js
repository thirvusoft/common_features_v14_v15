
frappe.ui.form.on('Vehicle Maintenance', {
    
    vehicle_no: async function(frm){
        if  (frm.doc.vehicle_no){
            await frappe.call({
            method: "common_features_v14.common_features_v14.custom.py.vehicle_maintanence_filter.service_maintanence_details",
            args: { 
                vehicle_no:frm.doc.vehicle_no
            },
              callback: function(r){
                console.log(r.message)
                vno=r.message
            }
        })

        frm.set_query("service_type",'maintenance_details',function(){
            return{
                filters:{
                    'name1':["in",vno]
                }
            }
        })
        }},})
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
    var total_value = (child.labour_cost || 0) + (child.maintenance_cost || 0)
    console.log(total_value)
    frappe.model.set_value(cdt, cdn, 'total_value', total_value)
}


