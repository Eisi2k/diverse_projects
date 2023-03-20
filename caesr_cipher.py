alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

#tet, shift and direction to code/decode
direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
if direction not in ["encode", "decode"]:
    print("please only endeo or decode")
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(start_text, shift_amount, cipher_direction):
    print(logo)
    end_text = ""

    #left shift for decode
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:

        if letter not in alphabet:
            end_text += letter
            continue

        position = alphabet.index(letter)

        new_position = position + shift_amount

        #if position out of range or shift very high to use the alphabet-list
        while new_position > 25:
            new_position = new_position - 26
        while new_position < 0:
            new_position = new_position + 26

        end_text += alphabet[new_position]
    print(f"The {direction}d text is {end_text}")


    #restart cipher
    restart = input("Want du restart: Type Yes or No.\n")
    if restart.lower() == "yes":
        direction_w = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
        if direction_w not in ["encode", "decode"]:
            print("please only endeo or decode")
            direction_w = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
        text_w = input("Type your message:\n").lower()
        shift_w = int(input("Type the shift number:\n"))
        caesar(start_text=text_w, shift_amount=shift_w, cipher_direction=direction_w)


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
