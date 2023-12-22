import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

SLOT_ROWS = 3
SLOT_COLS = 3

slot_symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

slot_symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

all_symbols = []

def check_winnings (columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol == symbol_to_check:
        break

    # only runs if break doesn't happen in for loop
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
    
  return winnings, winning_lines
  

def setup_slot_machine_symbols():
  for symbol, symbol_count in slot_symbol_count.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

def get_slot_machine_spin(rows, cols):
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(all_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")

    print()

def deposit():
  while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter valid number.")

  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter valid number of lines.")
    else:
      print("Please enter valid number.")

  return lines

def get_bet():
  while True:
    amount = input("What would you like to bet? $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be greater between ${MIN_BET} - ${MAX_BET}.")
    else:
      print("Please enter valid number.")

  return amount

def spin(balance):
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You don't have enough to bet that amount. Your current balance is: ${balance}.")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

  slots = get_slot_machine_spin(SLOT_ROWS, SLOT_COLS)
  print_slot_machine(slots)

  winnings, winning_lines = check_winnings(slots, lines, bet, slot_symbol_value)
  print(f"You won ${winnings}.")
  print(f"You won on lines:", *winning_lines)
  return winnings - total_bet

def main():
  setup_slot_machine_symbols()
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}.")
    answer = input("Press enter to play (q to quit).")
    if answer == "q":
      break
    balance += spin(balance)
  
  print(f"You left with ${balance}.")

main()