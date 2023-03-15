from model.car import Car
from Engine import Engine
from battery import Battery
from model.capulet_engine import CapuletEngine
from model.nbbattery import NubbinBattery
from model.spbattery import SpindlerBattery
from model.sternman_engine import SternmanEngine
from model.willoughby_engine import WilloughbyEngine

class CarFactory():
    def __init__(self):
        self.car_list = []
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))