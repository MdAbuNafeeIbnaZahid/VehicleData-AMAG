import os
from unittest import TestCase
import numpy
from framework import vehicle_data


class TestVehicleData(TestCase):
    def setUp(self) -> None:
        matrix = [
            [1, 0, 2, 3],
            [2, 0, 3, 2],
            [3, 1, 3, 4]
        ]
        _ = numpy.save("./file", matrix)
        self.v_data = vehicle_data.VehicleData("./file.npy")
        os.remove("./file.npy")

    def test_by_id_two_values(self):
        assert (self.v_data.by_id(0) == [(2, 3), (3, 2)])

    def test_by_id_single_id(self):
        assert (self.v_data.by_id(1) == [])  # only one datapoint. Got removed

    def test_filter_2_values(self):
        def len_is_2(trajectory):
            return len(trajectory) == 2

        assert (self.v_data.filter(len_is_2) == [[(2, 3), (3, 2)]])

    def test_filter_1_value_no_found(self):
        def len_is_1(trajectory):
            return len(trajectory) == 1

        assert (self.v_data.filter(len_is_1) == [])  # only one datapoint. Got removed
