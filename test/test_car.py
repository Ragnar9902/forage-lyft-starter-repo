import unittest
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar el módulo.
from engine.factory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]
        
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]
        
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.9, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.8, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.9, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.1, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire = [0, 0, 0]

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire = [0, 0, 0]

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        today = datetime.today().date()
        tire = [0, 0, 0]

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        today = datetime.today().date()
        tire = [0, 0, 0]

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        today = datetime.today().date()
        tier_wear = [0.92, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tier_wear)
        self.assertFalse(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        today = datetime.today().date()
        tier_wear = [0.5, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on, tier_wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.91, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        today = datetime.today().date()
        last_service_mileage = 0
        tire = [0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire)
        print(car.needs_service())
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.9, 1, 0.8, 0.8]
        
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertTrue(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_milaege = 0       
        today = datetime.today().date()
        tier_wear = [0.4, 0.5, 0.5, 0.5]
        
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_milaege, tier_wear)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
    
