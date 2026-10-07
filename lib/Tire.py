from lib.TireReading import *

class Tire():
    def __init__(self, position):
        # parameters -> position(str)
        # side effects -> initialise self.position == position initilise current_pressure == None  initilise current_tread_depth == None initilise self.historical_pressure == [] initilise self.historical_tread_depth == []
        pass

    def record_reading(self, value, timestamp, reading_type):
        # parameters -> value(int) timestamp -> datetime reading_type -> str
        # side effects -> historical_reading_list(current_reading_list) current_reading_list = Tire_Readings(value, timestamp)
        pass