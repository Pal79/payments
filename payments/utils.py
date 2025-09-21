from colorama import Fore, Style

def safe_int_input(prompt, default=0):
    while True:
        value = input(Fore.YELLOW + prompt + Style.RESET_ALL)  # kérdés sárgával
        if value.strip() == "":
            print(Fore.GREEN + f"✔ Default value: {default}" + Style.RESET_ALL)
            return default
        try:
            number = int(value)
            print(Fore.GREEN + f"✔ Scanned: {number}" + Style.RESET_ALL)
            return number
        except ValueError:
            print(Fore.RED + "❌ Just give me a number!" + Style.RESET_ALL)
