import csv

try:
    with open("marks.csv", "r") as file:
        reader = csv.DictReader(file)
        marks = [int(row["Marks"]) for row in reader]

    average = sum(marks) / len(marks)
    print("Average Marks:", round(average, 2))

except FileNotFoundError:
    print("File not found. Please check the file name.")
except ZeroDivisionError:
    print("No data available in the file.")
