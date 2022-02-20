with open("Python/#100DaysOfCode/Day 26/file1.txt") as file:
    contents_1 = file.read()
    contents_1_list = contents_1.split("\n")

with open("Python/#100DaysOfCode/Day 26/file2.txt") as file:
    contents_2 = file.read()
    contents_2_list = contents_2.split("\n")

results = [int(content) for content in contents_1_list if content in contents_2_list]

# Write your code above 👆

print(results)
