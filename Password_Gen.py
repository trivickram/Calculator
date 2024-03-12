import random
import string

def generate_strong_password():
    
    length = int(input("Enter the desired length of the password: "))
    strength = input("Enter the desired strength of the password (weak, medium, strong): ").lower()

    if strength == 'weak':

        all_characters = string.ascii_letters
    elif strength == 'medium':

        all_characters = string.ascii_letters + string.digits
    elif strength == 'strong':
   
        all_characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid strength input. Please enter 'weak', 'medium', or 'strong'.")
        return


    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
print(f"Generated Password: {generate_strong_password()}")
