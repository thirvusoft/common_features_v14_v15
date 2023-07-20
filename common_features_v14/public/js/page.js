
class Page extends frappe.ui.Page {
    setup_scroll_handler() {
		let last_scroll = 0;
		$(window).scroll(
			frappe.utils.throttle(() => {
				$(".page-head").toggleClass("drop-shadow", !!document.documentElement.scrollTop);
				let current_scroll = document.documentElement.scrollTop;
				// if (current_scroll > 0 && last_scroll <= current_scroll) {
				// 	$(".page-head").css("top", "-15px");
				// } else {
					$(".page-head").css("top", "var(--navbar-height)");
				// }
				last_scroll = current_scroll;
			}, 500)
		);
	}
    async setup_sidebar_toggle() {
		let sidebar_toggle = $(".page-head").find(".sidebar-toggle-btn");
		let sidebar_wrapper = this.wrapper.find(".layout-side-section");
		//thirvu change
		await frappe.db.get_single_value("Thirvu System Settings", "hide_toggle_sidebar_in_document").then((enabled) => {
			if(enabled){
				sidebar_wrapper.css("display","none")
			}
		})
		//end
		if (this.disable_sidebar_toggle || !sidebar_wrapper.length) {
			sidebar_toggle.remove();
		} else {
			sidebar_toggle.attr("title", __("Toggle Sidebar")).tooltip({
				delay: { show: 600, hide: 100 },
				trigger: "hover",
			});
			sidebar_toggle.click(() => {
				if (frappe.utils.is_xs() || frappe.utils.is_sm()) {
					this.setup_overlay_sidebar();
				} else {
					sidebar_wrapper.toggle();
				}
				$(document.body).trigger("toggleSidebar");
				this.update_sidebar_icon();
			});
		}
	}
}
frappe.ui.Page = Page
