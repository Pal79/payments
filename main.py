import os
import sys
from colorama import init, Fore, Style
from payments.payment_manager import PaymentManager
from payments.utils import safe_int_input

# Colorama inicializálása
init(autoreset=True)

# CSV fájl útvonala PyInstaller és .py futtatás esetén
if getattr(sys, 'frozen', False):
    data_path = os.path.dirname(sys.executable)  # exe könyvtára
else:
    data_path = os.path.abspath(".")            # .py könyvtára

filename = os.path.join(data_path, "payments.csv")
manager = PaymentManager(filename)

# Menü szöveg függvény
def show_menu():
    return (
        "\n"
        + Fore.CYAN + "=== Menü ===\n" + Style.RESET_ALL +
        "0 - Exit\n"
        "1 - Read Data\n"
        "2 - Add Data\n" +
        Fore.CYAN + "============\n" + Style.RESET_ALL +
        "Choose: "
    )

def main():
    is_on = True
    while is_on:
        choice = safe_int_input(show_menu())

        # Érvényes opciók ellenőrzése
        if choice not in (0, 1, 2):
            print(Fore.RED + f"❌ Invalid choice: {choice}" + Style.RESET_ALL)
            continue

        if choice == 1:
            manager.show_payments()

        elif choice == 2:
            # Érmék/bevételek bevitele
            value = (20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5)
            income_value = sum(safe_int_input(f"Quantity of {v}ft: ") * v for v in value)

            # Számlák bevitele
            billings_quantity = safe_int_input("Number of bills: ")
            bills_value = sum(safe_int_input("Amount of bill: ") for _ in range(billings_quantity))

            # Új bevétel hozzáadása
            manager.add_payment(income_value, bills_value)

        elif choice == 0:
            print(Fore.GREEN + "✔ Exit, goodbye! 👋" + Style.RESET_ALL)
            is_on = False

if __name__ == "__main__":
    main()
