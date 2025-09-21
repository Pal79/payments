from prettytable import PrettyTable
from colorama import Fore, Style

class Display:
    def show_table(self, data):
        table = PrettyTable()
        table.field_names = ["Date", "Income", "Bills", "Difference"]
        
        for row in data:
            # Date
            date_str = str(row[0])
            
            # Income zöld
            try:
                income = float(row[1])
            except (ValueError, IndexError):
                income = 0
            income_str = Fore.GREEN + str(income) + Style.RESET_ALL

            # Bills sárga
            try:
                bills = float(row[2])
            except (ValueError, IndexError):
                bills = 0
            bills_str = Fore.YELLOW + str(bills) + Style.RESET_ALL

            # Difference színezése
            try:
                difference = float(row[3])
            except (ValueError, IndexError):
                difference = 0

            if difference > 0:
                diff_str = Fore.GREEN + str(difference) + Style.RESET_ALL
            elif difference < 0:
                diff_str = Fore.RED + str(difference) + Style.RESET_ALL
            else:  # 0 érték halvány szürke
                diff_str = Style.DIM + Fore.WHITE + str(difference) + Style.RESET_ALL

            table.add_row([date_str, income_str, bills_str, diff_str])

        table.align = "l"
        print(table)
