from xml import etree

# Cargar el archivo XSD en un objeto etree
xsd = etree.parse('xml-schema_irving.xsd')

# Crear un objeto validador XMLSchema
xmlschema = etree.XMLSchema(xsd)

# Cargar el archivo XML en un objeto etree
xml = etree.parse('xml_irving.xml')

# Validar el archivo XML contra el esquema XSD
if xmlschema.validate(xml):
    print('El archivo XML es válido según el esquema XSD')
else:
    print('El archivo XML no es válido según el esquema XSD')
