from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora se puede importar el módulo.
from engine.factory import CarFactory

last_service_date = datetime.today().date()
current_mileage = 30000
today = datetime.today().date()
last_service_mileage = 0

car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
service = car.needs_service()
print(service)