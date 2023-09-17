#collect user input about the deposit info
import random

MAX_LINES = 5
MAX_BET=100
MIN_BET=1

ROWS = 5
COLS = 5

symbol_cout= {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value= {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winning += values[symbol] * bet
                winning_lines.append(lines+1)
    return winning, winning_lines

def get_slot_machines_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_cout in symbols.items():
        for _ in range(symbol_cout):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
#    print(f"we have {len(all_symbols)} amount of lines")
        
    return columns
def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("what would you like to deposit ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"amount must be between 1 and {MAX_LINES}")
        else:
            print("please enter a number.")
    return lines
def get_bet():
    while True:
        bet = input("what would you like to bet on each line? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number.")
    return bet

def game(balance):
    lines= get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f" you are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet} \n you do not have enough to bet on your balance. your balance is ${balance} \n please enter the valid amount")
        else:
            print(f"you are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
            break
    slots = get_slot_machines_spin(ROWS, COLS, symbol_cout)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print (f"you won {winnings}")
    print(f"you won on the lines : ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current banalce is {balance}")
        answer = input ("press enter to play (q to quit).")
        if answer == "q":
            break
        else:
            balance += game(balance)
    print(f"you left with ${balance}")

            

main()
