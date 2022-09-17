#This problem was asked by Apple.
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

from time import sleep

def timer(tempo):
    sleep(int(tempo)/1000)
    somador()

def somador():
    a = int(input('Digite o primeiro termo da soma: '))
    b = int(input('Digite o segundo termo da soma: '))
    return print(a + b)

tempo = input('Digite o tempo de espera(milisegundo): ')
timer(tempo)
