from abc import ABC

from Engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_service_mileage = current_service_mileage
    
    def needs_service(self):
        return self.current_service_mileage - self.last_service_mileage > 60000
