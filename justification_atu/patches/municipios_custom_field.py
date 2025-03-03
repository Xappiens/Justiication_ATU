import frappe

def execute():
    # 1. Agregar el campo custom "rprovincia" en Municipios, si no existe
    if not frappe.db.exists("Custom Field", "Municipios-rprovincia"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Municipios",
            "fieldname": "provincia",
            "label": "Provincia",
            "fieldtype": "Link",
            "options": "Provincias",
            "insert_after": "cod_municipio"
        }).insert(ignore_permissions=True)
    
    # 2. Actualizar el campo "cod_prov" para que obtenga su valor desde la Provincia seleccionada en rprovincia
    docfield = frappe.get_doc("DocField", {"parent": "Municipios", "fieldname": "cod_prov"})
    if docfield:
        # Si el fetch_from no está configurado, se actualiza
        if docfield.fetch_from != "provincia.cod_prov":
            docfield.fetch_from = "provincia.cod_prov"
            docfield.save(ignore_permissions=True)
            frappe.db.commit()
