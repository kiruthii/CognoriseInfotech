import random
print("Welcome to randon code generator!")
randomchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$^&*1234567890=-+/"
numpass=int(input("Please enter the number of password to be generated:"))
lenpass=int(input("please entr the length of the password needed:"))
print("Here are your random password")
for x in range(numpass):
    pwd=""
    for chars in range(lenpass):
        pwd=pwd+random.choice(randomchar)
    print(pwd)
