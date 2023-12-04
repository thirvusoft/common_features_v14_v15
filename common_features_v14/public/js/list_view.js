class ListView extends frappe.views.ListView {
    async render_list() {
        // clear rows
        await frappe.db.get_single_value("Thirvu System Settings", "view_button").then((enabled) => {
            this.view_button = enabled
        })
        this.$result.find(".list-row-container").remove();
        if (this.data.length > 0) {
            // append rows
            this.$result.append(
                this.data
                    .map((doc, i) => {
                        doc._idx = i;
                        return this.get_list_row_html(doc);
                    })
                    .join("")
            );
        }
    }
    get_meta_html(doc) {
        //thirvu changes
        let html = "";

        let settings_button = '';
        if (this.settings.button && this.settings.button.show(doc)) {
            settings_button = `
				<span class="list-actions">
					<button class="btn btn-action btn-default btn-xs"
						data-name="${doc.name}" data-idx="${doc._idx}"
						title="${this.settings.button.get_description(doc)}">
						${this.settings.button.get_label(doc)}
					</button>
				</span>
			`;
        }

        if (this.view_button) {
            settings_button += `
					<span class="list-actions">
						<button class="btn btn-action-view btn-default btn-xs"
							data-name="${doc.name}" data-idx="${doc._idx}" data-type="view"
							title="View Doc">
							${frappe.utils.icon("unhide", "sm", "like-icon")}
						</button>
					</span>
				`;
        }
        //end
        const modified = comment_when(doc.modified, true);

        let assigned_to = `<div class="list-assignments">
			<span class="avatar avatar-small">
			<span class="avatar-empty"></span>
		</div>`;

        let assigned_users = JSON.parse(doc._assign || "[]");
        if (assigned_users.length) {
            assigned_to = `<div class="list-assignments">
					${frappe.avatar_group(assigned_users, 3, { filterable: true })[0].outerHTML}
				</div>`;
        }

        const comment_count = `<span class="comment-count">
				${frappe.utils.icon("small-message")}
				${doc._comment_count > 99 ? "99+" : doc._comment_count || 0}
			</span>`;

        html += `
			<div class="level-item list-row-activity hidden-xs">
				<div class="hidden-md hidden-xs">
					${settings_button || assigned_to}
				</div>
				${modified}
				${comment_count}
			</div>
			<div class="level-item visible-xs text-right">
				${this.get_indicator_dot(doc)}
			</div>
		`;

        return html;
    }
    setup_action_handler() {
        this.$result.on("click", ".btn-action", (e) => {
            const $button = $(e.currentTarget);
            const doc = this.data[$button.attr("data-idx")];
            this.settings.button.action(doc);
            e.stopPropagation();
            return false;
        });
        //thirvu changes
        this.$result.on("click", ".btn-action-view", async (e) => {
            const $button = $(e.currentTarget);
            e.stopPropagation();
            const doc = this.data[$button.attr("data-idx")];
            var cur_data = []
            var is_col_break = 1
            var cur_doc = await frappe.db.get_doc(this.doctype, doc.name).then(r => {
                frappe.get_meta(this.doctype).fields.forEach(function (df) {
                    if (df.fieldtype != "Table" && df.fieldtype != "Time" && df.print_hide) {
                        cur_data.push({
                            "label": df.label,
                            "fieldname": df.fieldname,
                            "fieldtype": df.fieldtype,
                            "options": df.options,
                            "default": r[df.fieldname],
                            "read_only": 1
                        })
                        if (df.fieldtype == "Column Break") {
                            is_col_break = 0
                        }
                    }
                });
            })
            if (is_col_break) {
                cur_data.splice(2, 0, {
                    "fieldname": "cb1",
                    "fieldtype": "Column Break",

                });
            }

            cur_data.push({
                "fieldname": "sb1",
                "fieldtype": "Section Break",

            });
            var cur_doc = await frappe.db.get_doc(this.doctype, doc.name).then(r => {
                frappe.get_meta(this.doctype).fields.forEach(function (df) {
                    if (df.fieldtype == "Table" && df.fieldtype != "Time" && df.print_hide) {
                        cur_data.push({
                            "label": df.label,
                            "fieldname": df.fieldname,
                            "fieldtype": df.fieldtype,
                            "fields": child_table(df.options),
                            "read_only": 1,
                            'data': r[df.fieldname],
                            'in_place_edit': true,
                            'cannot_add_rows': true,
                            'get_data': () => {
                                return r[df.fieldname];
                            },
                        })
                    }
                });
            })
            var d = new frappe.ui.Dialog({
                size: 'large',
                title: __(doc.name),
                fields: cur_data,
                primary_action: function () {
                    var data = d.get_values();
                    d.hide()

                },
                primary_action_label: __('Close')
            });
            d.show();
            e.stopPropagation();
            return false;
        });
        //end
    }
    get_menu_items() {
		const doctype = this.doctype;
		const items = [];

		if (frappe.model.can_import(doctype, null, this.meta)) {
			items.push({
				label: __("Import", null, "Button in list view menu"),
				action: () =>
					frappe.set_route("list", "data-import", {
						reference_doctype: doctype,
					}),
				standard: true,
			});
		}

		if (frappe.model.can_set_user_permissions(doctype)) {
			items.push({
				label: __("User Permissions", null, "Button in list view menu"),
				action: () =>
					frappe.set_route("list", "user-permission", {
						allow: doctype,
					}),
				standard: true,
			});
		}

		if (frappe.user_roles.includes("System Manager")) {
			items.push({
				label: __("Role Permissions Manager", null, "Button in list view menu"),
				action: () =>
					frappe.set_route("permission-manager", {
						doctype,
					}),
				standard: true,
			});
		}

		if (
			frappe.model.can_create("Custom Field") &&
			frappe.model.can_create("Property Setter")
		) {
			items.push({
				label: __("Customize", null, "Button in list view menu"),
				action: () => {
					if (!this.meta) return;
					if (this.meta.custom) {
						frappe.set_route("form", "doctype", doctype);
					} else if (!this.meta.custom) {
						frappe.set_route("form", "customize-form", {
							doc_type: doctype,
						});
					}
				},
				standard: true,
				shortcut: "Ctrl+J",
			});
		}

		items.push({
			label: __("Toggle Sidebar", null, "Button in list view menu"),
			action: () => this.toggle_side_bar(),
			condition: () => this.hide_sidebar,
			standard: true,
			shortcut: "Ctrl+K",
		});

		if (frappe.user.has_role("System Manager") && frappe.boot.developer_mode === 1) {
			// edit doctype
			items.push({
				label: __("Edit DocType", null, "Button in list view menu"),
				action: () => frappe.set_route("form", "doctype", doctype),
				standard: true,
			});
		}

		if (frappe.user.has_role("System Manager")) {
			if (this.get_view_settings) {
				items.push(this.get_view_settings());
			}
		}

		return items;
	}
}

function child_table(child_doc){
	var cur_data =[]
	frappe.get_meta(child_doc).fields.forEach(function (df) {
		if (df.in_list_view) {
			cur_data.push({
				"label" : df.label,
				"fieldname": df.fieldname,
				"fieldtype": df.fieldtype,
				"options": df.options,
				"in_list_view": 1,
				"read_only": 1,
				"columns":df.columns
			})
		} 
	});
	return cur_data
}

frappe.views.ListView =ListView
