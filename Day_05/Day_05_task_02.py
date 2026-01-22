import csv

clean_data = []

try:
    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        clean_data = [
            int(row[1]) for row in reader
            if row[1].isdigit()
        ]

    print("Clean Sales Data:", clean_data)
    print("Total Sales:", sum(clean_data))

except Exception as e:
    print("Error:", e)
