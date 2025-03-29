class Contacto:
    def __init__(self, id, nombre, telefono, fecha_nacimiento, correo, area):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.area = area
    

class Directorio:
    def __init__(self, contactos, indice_telefonos, indice_ids, indice_areas, areas):
        self.contactos = contactos
        self.indice_telefonos = indice_telefonos
        self.indice_ids = indice_ids
        self.indice_areas = indice_areas
        self.areas = areas 