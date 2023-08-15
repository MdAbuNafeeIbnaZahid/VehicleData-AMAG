import os
from unittest import TestCase
import numpy
from framework import vehicle_data



class TestVehicleData(TestCase):
    class TestById(TestCase):
        matrix = [
            [1, 0, 2, 3],
            [2, 0, 3, 2],
            [3, 1, 3, 4]
        ]
        file = numpy.save("./file", matrix)
        vehicle_data = vehicle_data.VehicleData("./file.npy")
        os.remove("./file.npy")

        assert(vehicle_data.by_id(0) == [(2, 3), (3, 2)] )
        assert(vehicle_data.by_id(1) == []) # only one datapoint. Got removed

        def len_is_2(trajectory):
            return len(trajectory) == 2

        def len_is_1(trajectory):
            return len(trajectory) == 1

        assert (vehicle_data.filter(len_is_2) == [ [(2, 3), (3, 2)] ])

        assert (vehicle_data.filter(len_is_1) == []) # only one datapoint. Got removed