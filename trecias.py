import random
import string

length = int(input("Please type in length of password needed: "))
uppercase = input("Does password needs uppercase letters? [Y/N]: ")
digits = input("Does password needs digits? [Y/N]: ")
print("~~~~~~~~~")
pasw = []
password = ""

# checking if input values are valid


# Length validity check
if length in range(1, 99):
    print(f"Selected password length: {length}")
else:
    print("Value is incorrect for length")
    exit()
# Uppercase validity check
if uppercase.upper() == "Y":
    print("Password will include uppercase letters")
elif uppercase.upper() == "N":
    print("Password will not contain uppercase letters")
else:
    print("Uppercase letter value selected incorrectly")
    exit()
# Digits validity check
if digits.upper() == "Y":
    print("Password will include digits")
elif digits.upper() == "N":
    print("Password will not contain digits")
else:
    print("Digits value selected incorrectly")
    exit()
print("~~~~~~~~~")

i = 0
while i < length:
    low = random.choice(string.ascii_lowercase)
    pasw.append(low)
    i += 1
    if uppercase.upper() == "Y":
        up = random.choice(string.ascii_uppercase)
        pasw.append(up)
        i += 1
    if digits.upper() == "Y":
        num = random.randint(0, 9)  # random numbers between 0-9
        pasw.append(str(num))
        i += 1

for el in pasw:
    password += el

print(f"Your password is: {password}")

#padarytas commitas
print("Padarem commit 1 sukure faila")