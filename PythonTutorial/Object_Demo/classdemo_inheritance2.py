class Car(object):

    def __init__(self):
        print("You are just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just create the BMW instance")

    def drive(self):
        super().drive()
        print("You are driving a BMW, enjoy")

    def headup_display(self):
        print("This is the unique feature")

"""
c = Car()
c.drive()
c.stop()
"""
b = BMW()
b.drive()
b.stop()
b.headup_display()