class Car():
    """cars creation"""

    def __init__(self, made, model, year):
        """initialization cars attributes"""
        self.made = made
        self.model = model
        self.year = year
        self.odometer = 0

    def description(self):
        """return description of the car"""
        desc = str(self.year) + ' ' + self.model + ' ' + self.made
        return desc.title()

    def read_odometer(self):
        """it shows the odometer mileage"""
        print("mileage of " + self.made + " is " + str(self.odometer) + " km")

    def update_odometer(self, km):
        """Plus mileage on the odometer"""
        if km >= self.odometer:
            self.odometer = km
        else:
            print("You shouldn't do that!")

    def daily_odometer(self, km):
        if km >= 0:
            self.odometer = self.odometer + km
        else:
            print("You shouldn't do that daily!")


class Battery:
    """simple battery info"""

    def __init__(self, battery=100):
        self.battery = battery

    def battery_screening(self):
        """print information about health of the battery"""
        print("Car has " + str(self.battery) + " percent health its battery")


class El_car(Car):
    """aspects for the electric car"""

    def __init__(self, made, model, year):
        """initialisation of attributes of el.car from parents(super) class - Car"""
        super().__init__(made, model, year)
        self.battery_life = Battery()

    def description(self):
        """return description of the car"""
        desc = str(self.year) + ' ' + self.model + ' ' + self.made + str(self.battery_life)
        return desc.title()




