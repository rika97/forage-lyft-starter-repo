
class Serviceable(Car):
    def needs_service(self, Car):
        return Car.needs_service()


class Car(CarFactory, Engine, Battery):

    def __init__(self):
        self.engine = Engine
        self.battery = Battery
    
    def needs_service(self):
        return (self.engine.needs_service or self.battery.needs_service)


class Engine():

    def CapuletEngine(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.needs_service = (self.current_mileage - self.last_service_mileage > 30000)
        

    def WilloughbyEngine(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.needs_service = (self.current_mileage - self.last_service_mileage > 60000)

    def SternmanEngine(self, last_service_mileage, current_mileage):
        self.warming_light_on = warming_light_on
        self.current_mileage = current_mileage
        self.needs_service = warming_light_on
        


class CarFactory():
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.model = 'calliope'
        self.service_freq = 2
        self.engine = CapuletEngine
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.model = 'glissade'
        self.service_freq = 2
        self.engine = WilloughbyEngine
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.model = 'palindrome'
        self.service_freq = 4
        self.engine = SternmanEngine
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.service_freq = 4
        self.engine = WilloughbyEngine
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.service_freq = 4
        self.engine = CapuletEngine
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage