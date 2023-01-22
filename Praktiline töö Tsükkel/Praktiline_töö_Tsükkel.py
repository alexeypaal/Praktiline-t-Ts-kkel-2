#1
from math import *
from random import *
sum = 0
i = 0
while i < 10:
    num = input("Sisestage number: ")
    if num == "":
        break
    sum += int(num)
    i += 1
print("Arvude summa on:", sum)
print()

#2
sum = 0
for i in range(10):
    num = input("Sisestage number: ")
    if num == "":
        break
    sum += int(num)
print("Arvude summa on:", sum)
print()


#3
sum = 0
while True:
    num = input("Sisestage number või vajutage väljumiseks sisestusklahvi: ")
    if num == "":
        break
    sum += int(num)
print("Arvude summa on:", sum)
print()