from flask_testing import TestCase
from flask import current_app, url_for
from urllib.parse import urljoin
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        # Verifica si hubo una redirección (código de estado 302)
        if response.status_code == 302:
            # Imprime la URL de la redirección
            print(f"URL de redirección: {response.location}")

        self.assertEquals(response.location, '/hello')

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))

        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        print("response : ", response)
        print("response.location : ", response.location)
        print("url_for('index') : ", url_for('index'))

        self.assertEquals(response.location, url_for('index'))

