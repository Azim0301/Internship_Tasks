employees = {
    "E101": 25000,
    "E102": 32000,
    "E103": 28000,
    "E104": 40000
}

# Give 10% hike to employees earning less than 30000
for emp_id in employees:
    if employees[emp_id] < 30000:
        employees[emp_id] += employees[emp_id] * 0.10

print("Updated Employee Salaries:")
for emp_id, salary in employees.items():
    print(emp_id, ":", int(salary))
