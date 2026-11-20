data = [
    (749.17, "Investment Return"),
    (-11.54, "Utilities"),
    (-247.58, "Online Shopping"),
    (981.17, "Investment Return"),
    (-410.65, "Rent"),
    (310.60, "Rent"),
    (563.70, "Gift"),
    (220.79, "Salary"),
    (-49.85, "Car Maintenance"),
    (308.49, "Salary"),
    (-205.55, "Car Maintenance"),
    (870.64, "Salary"),
    (-881.51, "Utilities"),
    (518.14, "Salary"),
    (-264.66, "Groceries"),
]


def print_transactions(transactions):
    for amount, statement in transactions:
        print(f"${amount} - {statement}")


def print_summary(transactions):
    deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
    total_deposited = sum(deposits)
    withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    print(total_deposited)
    print(total_withdrawn)
    balance = total_deposited + total_withdrawn
    print(balance)


def analyze_transactions(transactions):
    deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
    total_deposit = sum(deposits)
    average_deposit = total_deposit / len(deposits) if deposits else 0
    print(average_deposit)
    withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    average_withdrawal = total_withdrawn / len(withdrawals) if withdrawals else 0
    print(average_withdrawal)
    transactions.sort()
    largest_withdrawal = transactions[0]
    largest_deposit = transactions[-1]
    print(f"Largest witdrawals: {largest_withdrawal}")
    print(f"Largest deposit: {largest_deposit}")


while True:
    print(
        "Digite print para imprimir, analyze para analisar as transações ou stop para encerrar o programa: \n"
    )
    choice = input().lower().strip()
    if choice == "print":
        print_summary(data)
    elif choice == "analyze":
        analyze_transactions(data)
    elif choice == "stop":
        break
    else:
        print("Invalid choice")
