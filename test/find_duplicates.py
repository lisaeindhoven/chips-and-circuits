import csv

all_lists = []
with open("TEST/output_06.24.2020_23.28.19.csv", mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        aaaa = row[1].strip("[]")
        list_of_coordinates = aaaa.split("),(")
        all_lists.append(list_of_coordinates)

for row in all_lists:
    for second_row in all_lists:
        if row != second_row:
            if (set(row[1:-1]).intersection(second_row[1:-1])):
                zelfde = (set(row[1:-1]).intersection(second_row[1:-1]))
                for coordinate in zelfde:
                    print(f"gelijk coordinaat: {zelfde}")
                    print(f"eerst {row}")
                    print(f"tweede {second_row}")
                    print()