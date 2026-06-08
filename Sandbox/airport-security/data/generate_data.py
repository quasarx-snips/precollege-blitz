import csv
import os
import random

file_name = "airport_security_data.csv"

if os.path.exists(file_name):
    print(f"'{file_name}' already exists.")
    with open(file_name, "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
else:
    print(f"'{file_name}' not found. Creating a new file...")
    with open(file_name, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["weight", "metal_content", "organic_content", "is_threat"])
        for i in range(2500):
            l = []
            weight = random.randint(5,25)
            metal_content = random.randint(0,100)
            organic_content = random.randint(0,100)
            is_threat = 1 if metal_content > 60 or (weight > 15 and metal_content > 40) else 0
            l.extend([weight,metal_content,organic_content,is_threat])
            csv_writer.writerow(l)
            l = []

    print("New File Created.")


            
            
            
