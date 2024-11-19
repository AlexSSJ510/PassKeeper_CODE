class Contrasena:
    def __init__(self, valor):
        self.valor = valor

    def es_segura(self):
        return (
                len(self.valor) >= 8 and
                any(c.isdigit() for c in self.valor) and
                any(c.isalpha() for c in self.valor) and
                any(c in "!@#$%^&*()_+-=" for c in self.valor)
        )


class GestorContraseñas:

    def __init__(self):
        self.contrasenas = {}  # Diccionario con estructura {username: Contrasena}

    def agregar_contrasena(self, username, red, contrasena):
        if (username, red) in self.contrasenas:
            return "El usuario y la red ya tienen una contraseña registrada."
        if contrasena.es_segura():
            self.contrasenas[(username, red)] = contrasena
            return f"Contraseña añadida correctamente para {username} en {red}."
        return "La contraseña no cumple con los requisitos."

    def editar_contrasena(self, username, red, nueva_contrasena):
        if (username, red) not in self.contrasenas:
            return "El usuario y la red no existen."
        nueva_contrasena_obj = Contrasena(nueva_contrasena)
        if not nueva_contrasena_obj.es_segura():
            return "La nueva contraseña no cumple con los requisitos."
        self.contrasenas[(username, red)] = nueva_contrasena_obj
        return f"Contraseña actualizada para {username} en {red}."

    def eliminar_contrasena(self, username, red):
        if (username, red) not in self.contrasenas:
            return "El usuario y la red no existen."
        del self.contrasenas[(username, red)]
        return f"Contraseña eliminada para {username} en {red}."

    def obtener_contrasenas(self):
        return [(username, contrasena.valor) for username, contrasena in self.contrasenas.items()]
