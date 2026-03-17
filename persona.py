class LuisGiraldo:
    # Constructor por defecto (sin parámetros)
    def __init__(self):
        pass
    # Constructor único
    def __init__(self,id,cedula, name, last, age, sueldo):
        self.id = id
        self.cedula = cedula
        self.nombre = name
        self.apellido = last
        self.edad = age
        self.sueldo = sueldo

    # --- GETTERS (Retornan el valor) ---
    def get_id(self):
        return self.id

    def get_cedula(self):
        return self.cedula

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_sueldo(self):
        return self.sueldo

    # --- SETTERS (Cambian el valor) ---
    def set_id(self, new_id):
        self.id = new_id
    def set_cedula(self, new_cedula):
        self.cedula = new_cedula
        
    def set_nombre(self, new_name):
        self.nombre = new_name

    def set_apellido(self, new_last):        
        self.apellido = new_last

    def set_edad(self, new_age):
        if new_age > 0: # Ejemplo de validación
            self.edad = new_age

    def set_sueldo(self, new_sueldo):
        self.sueldo = new_sueldo