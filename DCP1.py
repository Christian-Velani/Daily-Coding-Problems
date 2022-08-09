#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 21

for i in numeros:
    if k - i in numeros:
        print(True)
        break
    else:
        print(False)
        break
