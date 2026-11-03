import frappe

# thinkNXG: existing sites keep the upstream defaults that were stored at install time.
# Replace them only while they still hold the untouched upstream value, so anything an
# administrator set on purpose is left alone.
DEFAULTS = {
	("System Settings", "app_name"): ("Frappe", "thinkNXG"),
	("System Settings", "otp_issuer_name"): ("Frappe Framework", "thinkNXG Framework"),
	("Website Settings", "app_name"): ("Frappe", "thinkNXG"),
}


def execute():
	for (doctype, fieldname), (old, new) in DEFAULTS.items():
		if frappe.db.get_single_value(doctype, fieldname) == old:
			frappe.db.set_single_value(doctype, fieldname, new, update_modified=False)
