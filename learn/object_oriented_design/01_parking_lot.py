"""
OOD: Parking Lot.
Multiple floors, multiple spot sizes, assign the smallest spot that fits a
vehicle, and free it up again on exit.
"""
from abc import ABC, abstractmethod
from enum import Enum, auto


class VehicleSize(Enum):
    MOTORCYCLE = auto()
    CAR = auto()
    BUS = auto()


class Vehicle(ABC):
    def __init__(self, plate):
        self.plate = plate

    @property
    @abstractmethod
    def size(self):
        ...


class Motorcycle(Vehicle):
    size = VehicleSize.MOTORCYCLE


class Car(Vehicle):
    size = VehicleSize.CAR


class Bus(Vehicle):
    size = VehicleSize.BUS


class Spot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.vehicle = None

    def fits(self, vehicle):
        return self.vehicle is None and self.size.value >= vehicle.size.value

    def park(self, vehicle):
        self.vehicle = vehicle

    def leave(self):
        self.vehicle = None


class Floor:
    def __init__(self, level, spots):
        self.level = level
        self.spots = spots

    def find_spot(self, vehicle):
        candidates = [s for s in self.spots if s.fits(vehicle)]
        return min(candidates, key=lambda s: s.size.value, default=None)


class ParkingLot:
    def __init__(self, floors):
        self.floors = floors
        self.tickets = {}

    def park(self, vehicle):
        for floor in self.floors:
            spot = floor.find_spot(vehicle)
            if spot:
                spot.park(vehicle)
                self.tickets[vehicle.plate] = spot
                return spot
        return None

    def leave(self, plate):
        spot = self.tickets.pop(plate, None)
        if spot:
            spot.leave()
        return spot is not None


if __name__ == "__main__":
    lot = ParkingLot([
        Floor(1, [Spot(f"1-{i}", VehicleSize.MOTORCYCLE if i == 0 else VehicleSize.CAR) for i in range(3)]),
        Floor(2, [Spot(f"2-{i}", VehicleSize.BUS) for i in range(2)]),
    ])

    car = Car("CAR-001")
    bus = Bus("BUS-001")
    spot = lot.park(car)
    print(f"Parked {car.plate} at {spot.spot_id}")
    spot = lot.park(bus)
    print(f"Parked {bus.plate} at {spot.spot_id}")
    print(f"Leave CAR-001: {lot.leave('CAR-001')}")
