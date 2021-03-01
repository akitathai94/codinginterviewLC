import unittest
from city_functions import getCityCountry

class CityCountryTest(unittest.TestCase):
    """Test for 'city_functions.py' """
    def test_city_country(self):
        """Do name like 'Santiago, Chile' """
        formatted_city_country = getCityCountry("santiago", "chile")
        self.assertEqual(formatted_city_country, "Santiago, Chile")
    def test_city_country_pop(self):
        """Do name like 'Santiago, Chile - population 5000000' """
        formatted_city_country = getCityCountry("santiago", "chile", 5_000_000)
        self.assertEqual(formatted_city_country, "Santiago, Chile - population 5000000")
    

if __name__ == '__main__':
    unittest.main()