import numpy


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
        for id in self.segments:
            if len(self.segments[id]) == 0:
                del self.segments[id]

    def by_id(self, id):
        if id not in self.segments:
            return None
        return self.segments[id]


