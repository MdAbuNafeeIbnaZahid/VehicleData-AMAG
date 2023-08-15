from framework import vehicle_data, input_function

if __name__ == '__main__':
    data_file = './data.npy'  # pass by command line interface
    obj = vehicle_data.VehicleData(data_file)


    segments = obj.filter(input_function.input_function)
    obj.plot(segments)
