import unittest
from unittest.mock import patch, mock_open

from PassKeeper.src.logica.Contraseñas import Contrasena
from PassKeeper.src.logica.Contraseñas import GestorContraseñas


class TestContrasena(unittest.TestCase):

    def test_contrasena_segura(self):
        contrasena = Contrasena("Passw0rd!")
        self.assertTrue(contrasena.es_segura())

    def test_contrasena_no_segura_longitud(self):
        contrasena = Contrasena("Pass1!")
        self.assertFalse(contrasena.es_segura())

    def test_contrasena_no_segura_sin_digitos(self):
        contrasena = Contrasena("Password!")
        self.assertFalse(contrasena.es_segura())

    def test_contrasena_no_segura_sin_letras(self):
        contrasena = Contrasena("12345678!")
        self.assertFalse(contrasena.es_segura())

    def test_contrasena_no_segura_sin_especiales(self):
        contrasena = Contrasena("Password123")
        self.assertFalse(contrasena.es_segura())

    def test_contrasena_no_segura_sin_mayusculas(self):
        contrasena = Contrasena("password123!")
        self.assertFalse(contrasena.es_segura())


class TestGestorContraseñas(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba para configurar el entorno
        self.gestor = GestorContraseñas()

    def test_agregar_contrasena(self):
        contrasena = Contrasena("Password123!")
        resultado = self.gestor.agregar_contrasena("usuario1", "facebook", contrasena)
        self.assertEqual(resultado, "Contraseña añadida correctamente para usuario1 en facebook.")
        self.assertIn(("usuario1", "facebook"), self.gestor.contrasenas)

    def test_agregar_contrasena_existente(self):
        contrasena1 = Contrasena("Password123!")
        contrasena2 = Contrasena("NewPassword1!")
        self.gestor.agregar_contrasena("usuario2", "gmail", contrasena1)
        resultado = self.gestor.agregar_contrasena("usuario2", "gmail", contrasena2)
        self.assertEqual(resultado, "El usuario y la red ya tienen una contraseña registrada.")

    def test_editar_contrasena(self):
        contrasena_original = Contrasena("OldPassword123!")
        contrasena_nueva = Contrasena("NewPassword1!")
        self.gestor.agregar_contrasena("usuario3", "twitter", contrasena_original)
        resultado = self.gestor.editar_contrasena("usuario3", "twitter", "NewPassword1!")
        self.assertEqual(resultado, "Contraseña actualizada para usuario3 en twitter.")
        self.assertEqual(self.gestor.contrasenas[("usuario3", "twitter")].valor, "NewPassword1!")

    def test_editar_contrasena_no_existente(self):
        resultado = self.gestor.editar_contrasena("usuario_no_existente", "facebook", "NewPassword123!")
        self.assertEqual(resultado, "El usuario y la red no existen.")

    def test_eliminar_contrasena(self):
        contrasena = Contrasena("Password123!")
        self.gestor.agregar_contrasena("usuario4", "linkedin", contrasena)
        resultado = self.gestor.eliminar_contrasena("usuario4", "linkedin")
        self.assertEqual(resultado, "Contraseña eliminada para usuario4 en linkedin.")
        self.assertNotIn(("usuario4", "linkedin"), self.gestor.contrasenas)

    def test_eliminar_contrasena_no_existente(self):
        resultado = self.gestor.eliminar_contrasena("usuario_no_existente", "facebook")
        self.assertEqual(resultado, "El usuario y la red no existen.")



if __name__ == '__main__':
    unittest.main()
