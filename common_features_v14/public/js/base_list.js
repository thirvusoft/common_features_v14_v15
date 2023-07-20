class BaseList extends frappe.views.BaseList {
    show_or_hide_sidebar() {
		let show_sidebar = JSON.parse(localStorage.show_sidebar || "true");
		//thirvu changes
		this.$page.find(".layout-side-section").css("display","")
		//end
		$(document.body).toggleClass("no-list-sidebar", !show_sidebar);
	}
}

frappe.views.BaseList = BaseList
