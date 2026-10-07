from lib.Tire import *

def test_initialise_tire():
    tire = Tire("front left")

    assert tire.position == "front left"

    assert tire.current_pressure == None

    assert tire.current_tread_depth == None

    assert tire.historical_pressure == []

    assert tire.historical_tread_depth == []
