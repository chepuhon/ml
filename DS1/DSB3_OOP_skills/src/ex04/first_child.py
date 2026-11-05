import sys
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
            values = line.split(',')

            if len(values) != 2:
                raise ValueError("Invalid file structure")

            first, second = values

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

            head_fraction = int((heads / total) * 10000) / 10000
            tail_fraction = int((tails / total) * 10000) / 10000

            return head_fraction, tail_fraction

    class Analytics(Calculations):
        def predict_random(self, predictions_count):
            result = []

            for _ in range(predictions_count):
                coin = randint(0, 1)

                if coin == 1:
                    result.append([1, 0])
                else:
                    result.append([0, 1])

            return result

        def predict_last(self):
            return self.data[-1]


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 first_child.py data.csv")

    research = Research(sys.argv[1])

    data = research.file_reader()

    analytics = Research.Analytics(data)

    heads, tails = analytics.counts()

    head_fraction, tail_fraction = analytics.fractions(
        heads,
        tails
    )

    print(data)
    print(heads, tails)
    print(f"{head_fraction:.4f} {tail_fraction:.4f}")
    print(analytics.predict_random(3))
    print(analytics.predict_last())


if __name__ == '__main__':
    main()
