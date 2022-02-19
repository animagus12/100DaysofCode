# with open("Python/#100DaysOfCode/Day 25/weather_data.csv") as file:
#     contents = file.read()

# content_list = contents.split("\n")
# print(content_list)

# import csv

# with open("Python/#100DaysOfCode/Day 25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temp.append(int(row[1]))

#     print(temp)

import pandas

data= pandas.read_csv("Python/#100DaysOfCode/Day 25/weather_data.csv")
# print(data["temp"])
# avg = data["temp"].mean()
# maxi = data["temp"].max()
# print(avg)

# # Get data in conditions
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# Create a Dataframe from Scratch
data_dict= {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("Python/#100DaysOfCode/Day 25/new_csv.csv")
print(data)