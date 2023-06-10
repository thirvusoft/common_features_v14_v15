frappe.ui.form.on('Task', {
    refresh: function(frm){
		    document.querySelectorAll("[data-fieldname='view_auto_repeat_details']")[1].style.color = 'white'
        document.querySelectorAll("[data-fieldname='view_auto_repeat_details']")[1].style.backgroundColor = '#4d79ff'
        frappe.call({
          method: "common_features_v14.common_features_v14.custom.py.task.get_auto_repeat_schedule",
          args: {
              "self": frm.doc.ref_auto_repeat,
          },
          callback: function(r) {
            console.log(r.message)
            var schedule_details = r.message
            var p = `<table class="table table-bordered small">
            <thead>
              <tr>
                <th style="width: 20%">Frequency</th>
                <th style="width: 20%">Next Scheduled Date</th>
              </tr>
            </thead>
          
            <tbody>`
            for(var i=0; i < schedule_details.length; i++) { 
              p += `<tr>
                <td>`+schedule_details[i].frequency+`</td>
                <td>`+frappe.datetime.str_to_user(schedule_details[i].next_scheduled_date)+`</td>
              </tr>`
            } 
            p += `</tbody>
          </table>`
            console.log(p)
          frm.set_df_property("auto_repeat_schedule_html","options",p)
          }
      });
    },
    view_auto_repeat_details: function(frm){
		frappe.set_route("Form", "Auto Repeat", frm.doc.ref_auto_repeat);
    },

})