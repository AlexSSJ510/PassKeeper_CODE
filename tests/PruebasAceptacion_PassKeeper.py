import unittest
from src.logica.Contraseñas import Contrasena, GestorContraseñas

class TestAceptacionGestorContraseñas(unittest.TestCase):

    def test_flujo_completo(self):
        gestor = GestorContraseñas()

        gestor.agregar_contrasena("user1", "app1", Contrasena("P@ssw0rd1"))
        gestor.agregar_contrasena("user2", "app2", Contrasena("Str0ng!P@ss"))

        resultado_editar = gestor.editar_contrasena("user1", "app1", "NewP@ssw0rd")
        self.assertEqual(resultado_editar, "Contraseña actualizada para user1 en app1.")

        resultado_eliminar = gestor.eliminar_contrasena("user2", "app2")
        self.assertEqual(resultado_eliminar, "Contraseña eliminada para user2 en app2.")

        self.assertEqual(len(gestor.contrasenas), 1)

if __name__ == "__main__":
    unittest.main()
