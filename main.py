import sys

from framework import vehicle_data, input_function

if __name__ == '__main__':
    print(sys.argv)

    data_file = sys.argv[1]
    obj = vehicle_data.VehicleData(data_file)


    segments = obj.filter(input_function.input_function)
    obj.plot(segments)
