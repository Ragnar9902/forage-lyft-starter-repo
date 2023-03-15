from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery
        
    def needs_service(self):
        return self.engine.needs_service() & self.battery.needs_service