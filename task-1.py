from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} {model} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} {model} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} {model} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} {model} (EU Spec)", model)


us_factory: VehicleFactory = USVehicleFactory()
eu_factory: VehicleFactory = EUVehicleFactory()

vehicle1: Vehicle = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2: Vehicle = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
