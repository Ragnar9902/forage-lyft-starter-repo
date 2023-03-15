import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        Battery.__init__(self)
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        return (self.current_date.year - self.last_service_date.year) > 4