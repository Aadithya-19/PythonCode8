from collection import Counter

with open("SOCR-HeightWeight.csv", newline='') as f:
    file_object = csv.reader(f)
    data_list = list(file_object)

data_list.pop(0)

#sorting data to get height of people

new_data = []

for i in range(len(data_list)):
    n_number = data_list[i][1]

    new_data.append(float(n_number))


data = Counter(new_data)
modeDataOfRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}

for height, occurance in data.items():
    if 50<float(height)<60:
        modeDataOfRange["50-60"]+=occurance
    elif 60<float(height)<70:
        modeDataOfRange["60-70"]+=occurance
    elif 70<float(height)<80:
        modeDataOfRange["70-80"]+=occurance
        
mode_range, mode_occurance = 0,0

for range,occurance in modeDataOfRange.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance = int[int(range.split("-")[0]), int(range.split("-")[1], occurance)]

mode = float(mode_range[0]+mode_range[1]/2)
print(mode)
#mode