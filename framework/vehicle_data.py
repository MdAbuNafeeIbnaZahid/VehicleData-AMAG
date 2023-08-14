import numpy


class VehicleData:
    def __init__(self, string):
        data = numpy.load(string)
        print(data)

