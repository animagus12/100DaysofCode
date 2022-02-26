# # FileNotFound

# try:
#     file = open("Python/#100DaysOfCode/Day 30/a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     open("Python/#100DaysOfCode/Day 30/a_file.txt", "w")
#     file.write("Something")
# except KeyError as e: 
#     print(f"That key {e} does not exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was Closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)