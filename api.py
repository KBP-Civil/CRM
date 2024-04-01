import frappe

@frappe.whitelist()
def get_lead_details(lead_id=None):

    return frappe.db.sql(f"""SELECT *  FROM `tabLead` WHERE owner='Administrator';""", as_dict=True)
