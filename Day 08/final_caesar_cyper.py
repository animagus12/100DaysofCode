from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    character_list = list(text)
    for position, character in enumerate(character_list):
        if (character not in alphabet):
            continue

        if (direction == "encode"):
            character_list[position] = alphabet[alphabet.index(character) + shift]
        elif (direction == "decode"):
            character_list[position] = alphabet[alphabet.index(character) - shift]
    print(f"The {direction}ed Text is {''.join(character_list)}")

print(logo)
rerun = True
while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    rerun_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if (rerun_choice == "no"):
        rerun = False
        print("Thank You for using our program.")
