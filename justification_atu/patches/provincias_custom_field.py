import frappe

def execute():
    # Verifica si ya existe el campo personalizado en el DocType "Provincias"
    if not frappe.db.exists("Custom Field", "Provincias-ca"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Provincias",               # DocType que queremos extender
            "fieldname": "ca",                # Nombre interno del nuevo campo
            "label": "Comunidad Autonoma",                    # Etiqueta que se mostrará
            "fieldtype": "Link",              # Tipo de campo: Link
            "options": "Comunidad Autonoma",  # El DocType al que se enlaza
            "insert_after": "provincia",      # Posición: después del campo "provincia"
        }).insert(ignore_permissions=True)
        frappe.db.commit()
