// frappe.provide('common_features_v14');
frappe.provide('common_features_pre');
frappe.provide('common_features_success');
frappe.provide('common_features_maintenance');

// common_features_v14.update_indicator = function (link) {
//     if (document.querySelector("[role='thirvu-update-indicator']")) {
//         return
//     }
//     let header = document.querySelector(".main-section header[role='navigation']").parentElement
//     var r = document.querySelector(':root');
//     r.style.setProperty('--navbar-height', '95px');
//     r.style.setProperty('--top-navhi', '40px');
//     let update_version_txt = `<a class='version-update-link' href='${link}'>updated version</a>`
//     header.prepend($(`
//             <div class="app-update" role="thirvu-update-indicator">
//                 <div class="app-update-refresh">
//                     <div>
//                         The application has been updated, please refresh this page to get a ${link?update_version_txt:'updated version'}
//                     </div>
//                     <button class="btn btn-primary" onclick=frappe.ui.toolbar.clear_cache()>Refresh</button>
//                 </div>
//             </div>`)[0]
//     );
// }

common_features_pre.update_indicator_pre = function (link1,time) {
    if (document.querySelector("[role='thirvu-update-indicator']")) {
        return
    }
    let header = document.querySelector(".main-section header[role='navigation']").parentElement
    var r = document.querySelector(':root');
    r.style.setProperty('--navbar-height', '140px');
    r.style.setProperty('--top-navhi', '40px');
    header.prepend($(`
            <div class="app-update" role="thirvu-update-indicator">
                <div class="app-update-refresh">
                    <div>
                        ${link1} ${time}
                    </div>
                </div>
            </div>`)[0]
    );
}

common_features_maintenance.update_indicator_maintenance = function (link2) {
    if (document.querySelector("[role='thirvu-update-indicator']")) {
        return
    }
    let header = document.querySelector(".main-section header[role='navigation']").parentElement
    var r = document.querySelector(':root');
    r.style.setProperty('--navbar-height', '140px');
    r.style.setProperty('--top-navhi', '40px');
    header.prepend($(`
            <div class="app-update" role="thirvu-update-indicator">
                <div class="app-update-refresh">
                    <div>
                        ${link2}
                    </div>
                </div>
            </div>`)[0]
    );
}

common_features_success.update_indicator_success = function (link3) {
    if (document.querySelector("[role='thirvu-update-indicator']")) {
        return
    }
    let header = document.querySelector(".main-section header[role='navigation']").parentElement
    var r = document.querySelector(':root');
    r.style.setProperty('--navbar-height', '140px');
    r.style.setProperty('--top-navhi', '40px');
    header.prepend($(`
            <div class="app-update" role="thirvu-update-indicator">
                <div class="app-update-refresh">
                    <div>
                        ${link3}
                    </div>
                    <button class="btn btn-primary" onclick=frappe.ui.toolbar.clear_cache()>Refresh</button>
                </div>
            </div>`)[0]
    );
}
$(document).ready(function (frm) {
    // frappe.realtime.on("custom-version-update", function ({ link }) {
    //     common_features_v14.update_indicator(link)
    // });
    frappe.realtime.on("custom-version_pre", function ({ link1,time }) { 
        common_features_pre.update_indicator_pre(link1,time)
    });
    frappe.realtime.on("custom-version_maintenance", function ({ link2 }) { 
        common_features_maintenance.update_indicator_maintenance(link2)
    });
    frappe.realtime.on("custom-version_success", function ({ link3 }) { 
        common_features_success.update_indicator_success(link3)
        (`
            <div class="app-update" role="thirvu-update-indicator">
                <div class="app-update-refresh">
                    <div>
                        ${link3}
                    </div>
                    <button class="btn btn-primary" onclick=frappe.ui.toolbar.clear_cache()>Refresh</button>
                </div>
            </div>`)[0]
    });
    frappe.call({
        method: "common_features_v14.common_features_v14.doctype.version_update.version_update.refresh_warning",
        callback: function (r) { 
            if (r.message[0]) {
                common_features_pre.update_indicator_pre(r.message[0],r.message[1])
            }
        }
    })
    // frappe.call({
    //     method: "common_features_v14.common_features_v14.doctype.version_update.version_update.refresh_success",
    //     callback: function (r) { 
    //         if (r.message) {
    //             common_features_success.update_indicator_success(r.message)   
    //         }
    //     }
    // })
    frappe.call({
        method: "common_features_v14.common_features_v14.doctype.version_update.version_update.refresh_mainteance",
        callback: function (r) { 
            if (r.message) {
                common_features_maintenance.update_indicator_maintenance(r.message)   
            }
        }
    })
});


frappe.db.get_single_value("Thirvu System Settings", "toggle_full_width").then((enabled) => {
    if(enabled){
        if(localStorage.container_fullwidth != "true"){
            frappe.ui.toolbar.toggle_full_width()
        }
    }
})
frappe.db.get_single_value("Thirvu System Settings", "hide_toggle_sidebar_in_list").then((enabled) => {
    if(enabled){
        localStorage.show_sidebar = false
    } else{
        localStorage.show_sidebar = true
    }
})



