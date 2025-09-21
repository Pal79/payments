import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            return list(csv.reader(file))

    def append_row(self, row):
        with open(self.filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
