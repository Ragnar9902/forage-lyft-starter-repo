from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tier):
        super().__init__()
        self.engine  = engine
        self.battery = battery
        self.tier    = tier
        
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tier.needs_service()