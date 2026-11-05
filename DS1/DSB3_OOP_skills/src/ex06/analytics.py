import logging
import json
import requests
from random import randint

logging.basicConfig(
    filename='analytics.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)


class Research:
    def __init__(self, path_to_file):
        logging.info('Research instance has been created')
        self.path_to_file = path_to_file

    def file_reader(self, has_header=True):
        logging.info('Reading file')

        with open(self.path_to_file, 'r') as file:
            lines = file.read().splitlines()

        if has_header:
            lines = lines[1:]

        data = []

        for line in lines:
            first, second = line.split(',')

            if [first, second] not in [['0', '1'], ['1', '0']]:
                raise ValueError('Invalid file structure')

            data.append([int(first), int(second)])

        return data

    def send_telegram_message(self, url, message):
        logging.info('Sending telegram notification')

        if not url:
            return

        try:
            requests.post(
                url,
                data=json.dumps(
                    {
                        "text": message
                    }
                ),
                headers={
                    "Content-Type": "application/json"
                }
            )
        except Exception:
            pass

    class Calculations:
        def __init__(self, data):
            logging.info('Calculations instance has been created')
            self.data = data

        def counts(self):
            logging.info('Calculating the counts of heads and tails')

            heads = 0
            tails = 0

            for item in self.data:
                if item == [1, 0]:
                    heads += 1
                else:
                    tails += 1

            return heads, tails

        def fractions(self, heads, tails):
            logging.info('Calculating fractions')

            total = heads + tails

            return (
                heads / total * 100,
                tails / total * 100
            )

    class Analytics(Calculations):
        def predict_random(self, steps):
            logging.info('Making random prediction')

            result = []

            for _ in range(steps):
                if randint(0, 1):
                    result.append([1, 0])
                else:
                    result.append([0, 1])

            return result

        def predict_last(self):
            logging.info('Getting last observation')

            return self.data[-1]

        def save_file(self, data, filename, extension):
            logging.info('Saving report')

            with open(f'{filename}.{extension}', 'w') as file:
                file.write(data)
