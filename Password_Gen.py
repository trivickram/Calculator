import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '*', '+']
print("Welcome to the password generator")
length=int(input("Enter the length the password to be generated :"))
password=""
for i in range(length):
    code=random.choice(letters)
    password+=code
print(password)

'''import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_l=int(input("Enter the number of letters to included in the password :"))
num_n=int(input("Enter the number of numbers to included in the password :"))
num_s=int(input("Enter the number of numbers to included in the password :"))
password_list=[]
for i in range(num_l):
    code=random.choice(letters)
    password_list.append(code)

for i in range(num_n):
    code = random.choice(numbers)
    password_list.append(code)

for i in range(num_s):
    code=random.choice(symbols)
    password_list.append(code)
random.shuffle(password_list)

password=""
for i in password_list:
    password=password+i
print(password)
'''
