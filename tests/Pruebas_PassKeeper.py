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


if __name__ == '__main__':
    unittest.main()
