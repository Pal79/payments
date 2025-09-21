# payments
**payments** is a lightweight, biller management tool written in **Python**.  
It has been I developed over the past month to support my current work needs.  
The program runs entirely in the terminal and does not have a GUI.

---

## Technologies
- Language: Python 3.11
- Libraries: Colorama, PrettyTable
- Database: SQLite3

---

## Features
- Calculates the amount of banknotes
- Asks for the quantity of invoices
- Calculates total revenue and difference
- Terminal-based interface, no GUI

---

## Installation
1. Clone the repository:
```bash
git clone git@github.com:Pal79/payments.git
```
2. Navigate to the project folder:
```bash
cd payments
```
3. Install dependencies:
- 1.
```bash
python3 -m venv .venv
```
- 2.
```bash
source .venv/bin/activate
```
- 3.
```bash
pip install -r requirements.txt
```
4. Run program:
```bash
python3 main.py
```
5. .venv Exit:
```bash
deactivate
```
> :memo: Note: This application has been tested only on Linux. Other operating systems may require adjustments.
## Usage
Run the program:
```bash
python3 payments.py
```
Follow the on-screen instructions to manage your addresses.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

