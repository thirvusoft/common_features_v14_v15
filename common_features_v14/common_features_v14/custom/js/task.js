frappe.ui.form.on('Task', {
    refresh: function(frm){
		document.querySelectorAll("[data-fieldname='view_auto_repeat_details']")[1].style.color = 'white'
        document.querySelectorAll("[data-fieldname='view_auto_repeat_details']")[1].style.backgroundColor = '#4d79ff'
    },
    view_auto_repeat_details: function(frm){
		frappe.set_route("Form", "Auto Repeat", frm.doc.ref_auto_repeat);
    },

})