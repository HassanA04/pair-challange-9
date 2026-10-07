from lib.Car import *
from datetime import datetime

def test_initialise_car():
    car = Car()

    assert car.tires[0].position == "front left"

    assert car.tires[1].position == "front right"

    assert car.tires[2].position == "back left"

    assert car.tires[3].position == "back right"


def test_tire_record_one_reading():
    tire = Tire("")

    tire.record_reading(5, datetime(2009, 12, 5), "pressure")

    assert tire.current_pressure.value == 5

    assert tire.current_pressure.timestamp == datetime(2009, 12, 5)

def test_tire_record_historical_reading():
    tire = Tire("")

    pressures_dates = [datetime(year, 8, 12,) for year in range(2010, 2025)]

    for date in pressures_dates:
        tire.record_reading(28, date, "pressure")

    pressures = tire.historical_pressure

    for i in range(len(pressures)):
        assert pressures[i].timestamp == pressures_dates[i]

def car_get_details():
    car = Car()

    pressure = 20
    depth = 5
    for tire in car.tires:
        tire.record_pressure(pressure, datetime(2060, 9, 4), "pressure")
        pressure += 20
        depth += 5
    

    details = car.get_details()

    assert details[0]['position'] == "front left"
    assert details[0]['pressure'] == 20
    assert details[0]['depth'] == 5

    assert details[1]['position'] == "front right"
    assert details[1]['pressure'] == 40
    assert details[1]['depth'] == 10
    
    assert details[2]['position'] == "back left"
    assert details[2]['pressure'] == 60
    assert details[2]['depth'] == 15
    
    assert details[3]['position'] == "back right"
    assert details[3]['pressure'] == 80
    assert details[3]['depth'] == 20

    print(details)

    