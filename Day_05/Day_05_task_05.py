import csv

def analyze_expenses(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            expenses = [float(row["Amount"]) for row in reader]

        return {
            "Total": sum(expenses),
            "Max": max(expenses),
            "Min": min(expenses),
            "Average": round(sum(expenses) / len(expenses), 2)
        }

    except FileNotFoundError:
        return "Expense file not found"
    except ValueError:
        return "Invalid data found in file"

result = analyze_expenses("expenses.csv")
print("Expense Analysis:", result)
