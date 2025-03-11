import unittest
from main.services import load_ad_platforms, search_ad_platforms


class TestAdServices(unittest.TestCase):
    def test_load_ad_platforms(self):
        file_content = """Яндекс.Директ:/ru
                        Ревдинский рабочий:/ru/svrd/revda,/ru/svrd/pervik
                        Газета уральских москвичей:/ru/msk,/ru/permobl,/ru/chelobl
                        Крутая реклама:/ru/svrd"""
        result = load_ad_platforms(file_content)
        self.assertIn('/ru', result)
        self.assertIn('/ru/svrd/revda', result)
        self.assertEqual(result['/ru'], ['Яндекс.Директ'])

    def test_search_ad_platforms(self):
        ad_platforms = {
            '/ru': ['Яндекс.Директ'],
            '/ru/svrd': ['Крутая реклама'],
            '/ru/svrd/revda': ['Ревдинский рабочий']
        }
        result = search_ad_platforms(ad_platforms, '/ru/svrd/revda')
        self.assertIn('Яндекс.Директ', result)
        self.assertIn('Крутая реклама', result)
        self.assertIn('Ревдинский рабочий', result)


if __name__ == '__main__':
    unittest.main()
