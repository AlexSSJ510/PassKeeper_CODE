import unittest
import json

from src.logica.Contraseñas import GestorContraseñas
from src.logica.Contraseñas import Contrasena


#Pruebas de Integracion
class TestIntegracionGestorBackup(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorContraseñas()

    def test_backup_y_restauracion(self):
        self.gestor.agregar_contrasena("user1", "app1", Contrasena("P@ssw0rd1"))
        self.gestor.agregar_contrasena("user2", "app2", Contrasena("Str0ng!P@ss"))

        contrasenas_backup = {
            f"{usuario} - {red}": contrasena.valor
            for (usuario, red), contrasena in self.gestor.contrasenas.items()
        }
        with open("test_backup.json", "w") as f:
            json.dump(contrasenas_backup, f)

        self.gestor.contrasenas.clear()
        with open("test_backup.json", "r") as f:
            contrasenas_restauradas = json.load(f)

        for usuario_red, contrasena in contrasenas_restauradas.items():
            usuario, red = usuario_red.split(" - ")
            self.gestor.agregar_contrasena(usuario, red, Contrasena(contrasena))

        self.assertEqual(len(self.gestor.contrasenas), 2)


if __name__ == '__main__':
    unittest.main()
