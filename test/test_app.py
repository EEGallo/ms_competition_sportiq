import unittest
from flask import current_app
from app import create_app

# Esta clase contiene métodos para realizar pruebas en la aplicación Flask.Hereda de unittest
class AppTestCase(unittest.TestCase):

    #Este método se ejecuta antes de cada prueba. Se crea una instancia de la aplicación Flask
    def setUp(self):
        self.app = create_app()
        # se crea una instancia de la aplicación Flask usando la función create_app(),
        self.app_context = self.app.app_context()
        # y se empuja un contexto de aplicación (app_context) para asegurarse de que la aplicación esté lista para ser probada.
        self.app_context.push()
    
    #Este método se ejecuta después de cada prueba. En este caso, se quita el contexto de la aplicación
    def tearDown(self):
        self.app_context.pop()
    
    #Se verifica que la instancia de la aplicación (current_app) no sea None, es decir, que la aplicación esté inicializada correctamente.
    def test_app(self):
        self.assertIsNotNone(current_app)
        
    # def test_user(self):
    #     user1 = User
    #     user1.name = 'admin'
    #     user2 = User
    #     user2.name = 'admin'
    #     self.assertEqual(user1.name, 'admin')
    #     self.assertEqual(user2.name, 'usuario comun')
    #     self.assertEqual(user1, user2)

# def test_create_user(self):
#     user = User('')
#     self.user_service.create(User)

        

#verifica si el script está siendo ejecutado directamente (no importado como un módulo). 
# Si es así, ejecuta el conjunto de pruebas utilizando unittest.main().        
if __name__ == '__main__':
    unittest.main()