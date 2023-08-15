import numpy
from matplotlib import pyplot


class VehicleData:
    def __init__(self, file_name):
        matrix = numpy.load(file_name)
        self._build_segments(matrix)

    def _build_segments(self, matrix):
        self.segments = dict()
        for row in matrix:
            idx = row[0]
            id = row[1]
            x = row[2]
            y = row[3]
            if id not in self.segments:
                self.segments[id] = []
            self.segments[id].append((x, y))
        for id in list(self.segments.keys()):
            if len(self.segments[id]) == 1:
                del self.segments[id]

    def by_id(self, id):
        if (id not in self.segments) or len(self.segments[id]) == 1:
            return []
        return self.segments[id]

    def filter(self, input_func):
        to_return_segment_list = []
        for id in self.segments:
            if input_func(self.segments[id]):
                to_return_segment_list.append(self.segments[id])
        return to_return_segment_list

    def plot(self, list_of_segments):
        pyplot.title("demo AMAG")
        for seg in list_of_segments:
            x = list(zip(*seg))[0]
            y = list(zip(*seg))[1]
            pyplot.plot(x, y)
        pyplot.show()
