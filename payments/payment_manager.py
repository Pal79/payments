from datetime import datetime
from .csv_handler import CSVHandler
from .display import Display
from colorama import Fore, Style

class PaymentManager:
    def __init__(self, filename):
        self.filename = filename
        self.csv_handler = CSVHandler(filename)
        self.display = Display()

    def add_payment(self, income_values, bills_values):
        now = datetime.now()
        current_date = now.strftime('%Y-%m-%d')
        difference = income_values - bills_values
        new_row = [current_date, income_values, bills_values, difference]
        self.csv_handler.append_row(new_row)
        print("\n" + Fore.GREEN + "✔ New data added!" + Style.RESET_ALL)

    def show_payments(self):
        data = self.csv_handler.read_csv()
        self.display.show_table(data)
