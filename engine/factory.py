import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.car import Car
from model.capulet_engine import CapuletEngine
from model.nbbattery import NubbinBattery
from model.spbattery import SpindlerBattery
from model.sternman_engine import SternmanEngine
from model.willoughby_engine import WilloughbyEngine
from model.carr_tiers import CarriganTires
from model.octo_tires import OctoprimeTires

class CarFactory():
    def __init__(self):
        self.car_list = []
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTires(tire))
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTires(tire))
    
    def create_palindrome(current_date, last_service_date, warning_light_on, tire):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), OctoprimeTires(tire))
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(tire))
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), CarriganTires(tire))