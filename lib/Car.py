from lib.Tire import Tire

class Car():
    def __init__(self):
        self.tires = [Tire("front left"), Tire("front right"),
                         Tire("back left"), Tire("back right")]

    
    def get_details(self):
        # parameters -> None
        # side effects -> None
        # returns -> list of dictionaries with tire details
        dictList = []
        for tire in self.tires:
            dictionary = {
                "position": tire.position,
                "pressure": {"value": tire.current_pressure.value,
                                "timestamp": tire.current_pressure.timestamp},
                "depth": {"value": tire.current_depth.value,
                            "timestamp": tire.current_depth.timestamp}
            }

            dictList.append(dictionary)

        return dictList