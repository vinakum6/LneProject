from django.test import SimpleTestCase

class TestLink(SimpleTestCase):
    def test_base_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_status_code(self):
        response = self.client.get('home/')
        self.assertEqual(response.status_code,200)

    def test_about_status_code(self):
        response = self.client.get('about/')
        self.assertEqual(response.status_code,200)
