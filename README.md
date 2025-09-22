# payments
**payments** is a lightweight, biller management tool written in **Python**.  
It has been developed over the past month to support my current work needs.  
The program runs entirely in the terminal and does not have a GUI.

---

## Technologies
- Language: Python 3.11
- Libraries: Colorama, PrettyTable
- Data storage: csv

---

## Features
- Calculates the amount of banknotes
- Asks for the quantity of invoices
- Calculates total revenue and differences
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
- create virtual environment:
```bash
python3 -m venv .venv
```
- activate venv:
```bash
source .venv/bin/activate
```
- install imports:
```bash
pip install -r requirements.txt
```
4. Run program with:
```bash
python3 main.py
```
5. Exit th virtual environment:
```bash
deactivate
```
> :memo: Note: This application has been tested only on Linux. Other operating systems may require adjustments.
## Usage
Run the program:
```bash
python3 payments.py
```
Follow the on-screen instructions.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

