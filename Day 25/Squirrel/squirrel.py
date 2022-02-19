import pandas

data = pandas.read_csv(
    "Python/#100DaysOfCode/Day 25/Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# gray = 0
# cinnamon = 0
# black = 0
# for color in data["Primary Fur Color"]:
#     if color == "Gray":
#         gray += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#     elif color == "Black":
#         black += 1

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

final_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

final_data = pandas.DataFrame(final_dict)
final_data.to_csv("Python/#100DaysOfCode/Day 25/Squirrel/squirrel_color.csv")
print(final_data)
