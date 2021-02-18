import csv

with open("SOCR-HeightWeight.csv", newline='') as f:
    file_object = csv.reader(f)
    data_list = list(file_object)

data_list.pop(0)

#sorting data to get height of people

new_data = []

for i in range(len(data_list)):
    n_number = data_list[i][1]

    new_data.append(float(n_number))

#mean

n = len(new_data)
total = 0

for x in new_data:
    total+=x

mean = total/n

print(mean)