import csv 
import os

filename = "employeeData_Lab9 - Sheet1.csv"
salaries =[]

if os.path.exists(filename):
        
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)    # Skip the header row
        salaryIndex = headers.index("Annual_Salary")  
        
        print(headers)
        for row in reader:
            print(row) 
            salaries.append(float(row[salaryIndex]))


    print(salaries)
    if (salaries):
        averageSalary = sum(salaries) / len(salaries)
        print(f"Average_Salary: {averageSalary:.2f}")
        maxSalary = max(salaries)
        print(f"Max Salary: {maxSalary:.2f}")
        minSalary = min(salaries)
        print(f"Min Salary: {minSalary:.2f}")
    else:
        print("No salary data found.")
else:
    print(f"Error: File {filename} does not exist.")