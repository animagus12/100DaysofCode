def my_function():
    result = 3 * 2
    return result

print(my_function())

# Function with Outputs
def format_name(f_name, l_name):
    full_name = f_name + " " + l_name
    return full_name.title()

f_name = input()
l_name = input()
print(format_name(f_name, l_name))

# Multiple Returns 
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"Blank Space Given"
    full_name = f_name + " " + l_name
    return full_name.title()

f_name = input()
l_name = input()
print(format_name(f_name, l_name))
