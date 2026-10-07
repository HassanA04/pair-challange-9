from lib.TireReading import *

class Tire():
    def __init__(self, position):
        # parameters -> position(str)
        # side effects -> initialise self.position == position initilise current_pressure == None  initilise current_tread_depth == None initilise self.historical_pressure == [] initilise self.historical_tread_depth == []
        self.position: str = position
        self.current_pressure: Tire_Readings = None
        self.current_depth: Tire_Readings = None
        self.historical_pressure = []
        self.historical_depth = []

    def record_reading(self, value, timestamp, reading_type):
        # parameters -> value(int) timestamp -> datetime reading_type -> str
        # side effects -> historical_reading_list(current_reading_list) current_reading_list = Tire_Readings(value, timestamp)
        if reading_type == "pressure":
            if self.current_pressure != None:
                self.historical_pressure.append(self.current_pressure)

            self.current_pressure = Tire_Readings(value, timestamp)
        else:
            if self.current_depth != None:
                self.historical_depth.append(self.current_depth)

            self.current_depth = Tire_Readings(value, timestamp)