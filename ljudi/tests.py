from django.test import SimpleTestCase


class RadeStranice(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_sredstva_za_rad_page_status_code(self):
        response = self.client.get('sredstva_za_rad/')
        self.assertEqual(response.status_code, 200)

    def test_projekti_page_status_code(self):
        response = self.client.get('projekti/')
        self.assertEqual(response.status_code, 200)

    def test_zaposleni_page_status_code(self):
        response = self.client.get('zaposleni/')
        self.assertEqual(response.status_code, 200)

    def test_odsustva_page_status_code(self):
        response = self.client.get('odsustva/')
        self.assertEqual(response.status_code, 200)
