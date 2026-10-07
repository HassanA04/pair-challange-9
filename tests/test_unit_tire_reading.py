from lib.TireReading import *
from datetime import datetime

def test_initialise_tire_reading():
    tireReading = Tire_Readings(5, datetime(2026, 10, 7))

    assert tireReading.value == 5

    assert tireReading.timestamp == datetime(2026, 10, 7)