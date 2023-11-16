import random
import csv

values = []
with open("medium_data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        values.append(row[7])

print(values)

sample_2 = [[values[0]]]

for i in range(100):
    sample_2.append([random.choice(values)])

with open("sample_2.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_2)
