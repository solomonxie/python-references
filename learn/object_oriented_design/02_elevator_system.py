"""
OOD: Elevator System.
Multiple elevators serving a building; each pending request is assigned to
whichever elevator can reach it with the least extra travel.
"""
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    IDLE = auto()


class Elevator:
    def __init__(self, elevator_id, current_floor=1):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = Direction.IDLE
        self.stops = set()

    def request(self, floor):
        self.stops.add(floor)
        if floor > self.current_floor:
            self.direction = Direction.UP
        elif floor < self.current_floor:
            self.direction = Direction.DOWN

    def cost_to_serve(self, floor):
        return abs(self.current_floor - floor)

    def step(self):
        if not self.stops:
            self.direction = Direction.IDLE
            return
        target = min(self.stops, key=lambda f: abs(f - self.current_floor))
        if target > self.current_floor:
            self.current_floor += 1
        elif target < self.current_floor:
            self.current_floor -= 1
        if self.current_floor == target:
            self.stops.discard(target)


class ElevatorController:
    def __init__(self, num_elevators):
        self.elevators = [Elevator(i) for i in range(num_elevators)]

    def dispatch(self, floor):
        best = min(self.elevators, key=lambda e: e.cost_to_serve(floor))
        best.request(floor)
        return best.elevator_id

    def tick(self):
        for elevator in self.elevators:
            elevator.step()


if __name__ == "__main__":
    controller = ElevatorController(2)
    controller.elevators[1].current_floor = 5

    print(f"Dispatch floor 1 -> elevator {controller.dispatch(1)}")
    print(f"Dispatch floor 8 -> elevator {controller.dispatch(8)}")

    for _ in range(6):
        controller.tick()
    for e in controller.elevators:
        print(f"Elevator {e.elevator_id} now at floor {e.current_floor}")
