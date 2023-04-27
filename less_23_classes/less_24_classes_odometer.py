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


my_car1 = Car("audi", "a4", 2002)
my_car2 = Car("skoda", "felicia", 1999)
my_car3 = Car("reno", "sandero", 2018)

my_car3.update_odometer(30)
my_car3.update_odometer(33)
my_car3.update_odometer(23)
my_car3.read_odometer()
my_car3.daily_odometer(100)
my_car3.read_odometer()
my_car3.daily_odometer(-10)
my_car3.read_odometer()
my_car3.daily_odometer(0)
my_car3.read_odometer()
