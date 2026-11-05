import os
from random import randint


class Research:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def file_reader(self, has_header=True):
        with open(self.path_to_file, "r") as file:
            lines = file.read().splitlines()

        if has_header:
            lines = lines[1:]

        data = []

        for line in lines:
            first, second = line.split(',')

            if [first, second] not in [['0', '1'], ['1', '0']]:
                raise ValueError("Invalid file structure")

            data.append([int(first), int(second)])

        return data

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0

            for item in self.data:
                if item == [1, 0]:
                    heads += 1
                else:
                    tails += 1

            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails

            return (
                heads / total * 100,
                tails / total * 100
            )

    class Analytics(Calculations):
        def predict_random(self, steps):
            result = []

            for _ in range(steps):
                coin = randint(0, 1)

                if coin:
                    result.append([1, 0])
                else:
                    result.append([0, 1])

            return result

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, filename, extension):
            with open(f"{filename}.{extension}", "w") as file:
                file.write(data)
