frappe.provide('common_features_v14');

common_features_v14.update_indicator = function (link) {
    if (document.querySelector("[role='thirvu-update-indicator']")) {
        return
    }
    let header = document.querySelector(".main-section header[role='navigation']").parentElement
    var r = document.querySelector(':root');
    r.style.setProperty('--navbar-height', '95px');
    r.style.setProperty('--top-navhi', '40px');
    let update_version_txt = `<a class='version-update-link' href='${link}'>updated version</a>`
    header.prepend($(`
            <div class="app-update" role="thirvu-update-indicator">
                <div class="app-update-refresh">
                    <div>
                        The application has been updated, please refresh this page to get a ${link?update_version_txt:'updated version'}
                    </div>
                    <button class="btn btn-primary" onclick=frappe.ui.toolbar.clear_cache()>Refresh</button>
                </div>
            </div>`)[0]
    );
}

$(document).ready(function () {
    frappe.realtime.on("custom-version-update", function ({ link }) {
        common_features_v14.update_indicator(link)
    });
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



