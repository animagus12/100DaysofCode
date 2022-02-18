with open("Python/#100DaysOfCode/Day 24/Mail Merge Project/Input/Letters/starting_letter") as initial_file:
    template = initial_file.read()

with open("Python/#100DaysOfCode/Day 24/Mail Merge Project/Input/Names/invited_names") as name_file:
    names = name_file.read()
    name_list = names.split("\n")

for i in range(0, len(name_list) - 1):
    with open(f"Python/#100DaysOfCode/Day 24/Mail Merge Project/Output/ReadyToSend/letter_for_{name_list[i]}.txt", "w") as new_file:
        new_file.write(template.replace("[name]", name_list[i]))
