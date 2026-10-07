As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


# 1: Class Design
``` python

class Car():
    def __init__(self):
        # parameters -> None
        # side effects -> initilise self.tires == [tire, tire, tire, tire]
    
    def get_details(self):
        # parameters -> None
        # side effects -> None
        # returns -> dictionary with tire details


class Tire():
    def __init__(self, position):
        # parameters -> position(str)
        # side effects -> initialise self.position == position initilise current_pressure == None  initilise current_tread_depth == None initilise self.historical_pressure == [] initilise self.historical_tread_depth == []

    def record_reading(self, value, timestamp, reading_type):
        # parameters -> value(int) timestamp -> datetime reading_type -> str
        # side effects -> historical_reading_list(current_reading_list) current_reading_list = Tire_Readings(value, timestamp)


class Tire_Readings():
    def __init__(self, value, timestamp):
        # parameters -> None
        # side effects -> initilise self.value == value initilise self.timestamp == timestamp


```