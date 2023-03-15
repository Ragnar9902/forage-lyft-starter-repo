from abc import ABC
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.Engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_service_mileage = current_service_mileage
    
    def needs_service(self):
        return self.current_service_mileage - self.last_service_mileage > 30000
