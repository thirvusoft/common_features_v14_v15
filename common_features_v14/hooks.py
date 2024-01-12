from . import __version__ as app_version

app_name = "common_features_v14"
app_title = "Common Features V14"
app_publisher = "Thirvusoft"
app_description = "Common Features"
app_email = "thirvusoft@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["common_features_v14.bundle.css"]
app_include_js = ["common_features_v14.bundle.js"]

# include js, css files in header of web template
# web_include_css = "/assets/common_features_v14/css/common_features_v14.css"
# web_include_js = "/assets/common_features_v14/js/common_features_v14.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "common_features_v14/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Task" : "/common_features_v14/custom/js/task.js",
    "ToDo" : "/common_features_v14/custom/js/todo.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "common_features_v14.utils.jinja_methods",
#	"filters": "common_features_v14.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "common_features_v14.install.before_install"
# after_install = "common_features_v14.install.after_install"
after_migrate = ["common_features_v14.install.after_install","common_features_v14.core_backup.file_override.file_override"]

# Uninstallation
# ------------

# before_uninstall = "common_features_v14.uninstall.before_uninstall"
# after_uninstall = "common_features_v14.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "common_features_v14.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Task": {
		"validate": "common_features_v14.common_features_v14.custom.py.task.auto_repeat",
	},
    "ToDo": {
		"validate": "common_features_v14.common_features_v14.custom.py.task.auto_repeat",
	},
    # "Customer": {
	# 	"autoname":"common_features_v14.common_features_v14.custom.py.customer.customer_captalize",
	# },
    "Lead":{
		"autoname":"common_features_v14.common_features_v14.custom.py.lead.lead_captalize",
	},
    "Item":{
		"autoname":"common_features_v14.common_features_v14.custom.py.item.item_captalize",
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"* * * * *": "common_features_v14.common_features_v14.doctype.version_update.version_update.update_maintenance_mode_on"
	},
#	"daily": [
#		"common_features_v14.tasks.daily"
#	],
#	"hourly": [
#		"common_features_v14.tasks.hourly"
#	],
#	"weekly": [
#		"common_features_v14.tasks.weekly"
#	],
#	"monthly": [
#		"common_features_v14.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "common_features_v14.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "common_features_v14.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "common_features_v14.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["common_features_v14.utils.before_request"]
# after_request = ["common_features_v14.utils.after_request"]

# Job Events
# ----------
# before_job = ["common_features_v14.utils.before_job"]
# after_job = ["common_features_v14.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"common_features_v14.auth.validate"
# ]
