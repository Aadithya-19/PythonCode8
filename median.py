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

#median

n = len(new_data)
new_data.sort()

if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
    print(median)

else:
    median = new_data[n//   2]
    print(median)