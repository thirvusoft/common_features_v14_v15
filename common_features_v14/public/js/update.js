frappe.provide('common_features_v14');

common_features_v14.remove_update_indicator = function () {
    if (document.querySelector("[role='thirvu-update-indicator']")) {
        var r = document.querySelector(':root');
        document.querySelector("[role='thirvu-update-indicator']").remove();
        r.style.setProperty('--navbar-height', '0');
        r.style.setProperty('--top-navhi', '0');
    }
}

common_features_v14.update_indicator = function (message, refresh_button, indicator) {
    common_features_v14.remove_update_indicator();

    let header = document.querySelector(".main-section header[role='navigation']").parentElement;
    
    var r = document.querySelector(':root');
    r.style.setProperty('--navbar-height', '95px');
    r.style.setProperty('--top-navhi', '40px');

    header.prepend($(`
            <div class="app-update-container" role="thirvu-update-indicator">
                <div class="app-update app-update-transform-css ${indicator}">
                    <div class="app-update-refresh">
                        <div>
                            ${message || ''}
                        </div>
                        <button class="btn btn-primary" style="${refresh_button?'':'display:none;'}" onclick=frappe.ui.toolbar.clear_cache()>Refresh</button>
                    </div>
                </div>
            </div>`)[0]
    );

    let ele = document.querySelector("[role='thirvu-update-indicator'] .app-update.app-update-transform-css");
    if (ele) {
        setTimeout(() => {
            ele.classList.remove('app-update-transform-css')
        }, 300)
        
    }
}

$(document).ready(function (frm) {
    frappe.realtime.on("custom-version-update", function ({message, refresh_button, indicator}) {
        common_features_v14.update_indicator(message, refresh_button, indicator)
    });
    frappe.realtime.on("clear-custom-version-update", function () {
        common_features_v14.remove_update_indicator()
    });
   
    frappe.call({
        method: "common_features_v14.common_features_v14.doctype.version_update.version_update.check_maintenance_mode",
        callback: function (r) { 
            if (r.message) {
                common_features_v14.update_indicator(...(r.message))
            }
        }
    });
});

frappe.db.get_single_value("Thirvu System Settings", "toggle_full_width").then((enabled) => {
    if(enabled){
        if(localStorage.container_fullwidth != "true"){
            frappe.ui.toolbar.toggle_full_width()
        }
    }
});

frappe.db.get_single_value("Thirvu System Settings", "hide_toggle_sidebar_in_list").then((enabled) => {
    if(enabled){
        localStorage.show_sidebar = false
    } else{
        localStorage.show_sidebar = true
    }
});
