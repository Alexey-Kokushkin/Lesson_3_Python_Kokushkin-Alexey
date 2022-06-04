# Найти НОК двух чисел
#import math

#print('Enter number A = ')
#A=int(input())
#print('Enter number B = ')
#B=int(input())

#if A>B:
    #CommonDivisor= math.gcd(A,B)
#else:
    #CommonDivisor=math.gcd(B,A)
#CommonMultiply = A*B/CommonDivisor

#print(f'Наименьшее общее кратное чисел {A} и {B} =',CommonMultiply)


#Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141. 

#from decimal import ROUND_FLOOR, Decimal
#import math

#print('Введите точность D для вычисления ПИ = ')
#D=str(input())
#ValuePI=Decimal(str(math.pi))
#print(ValuePI.quantize(Decimal(D),ROUND_FLOOR))

# Составить список простых множителей натурального числа N

#print('Введите натуральное число N = ')
#N=int(input())
#PrimeMultipliers=[]
#Multiplier=2
#while Multiplier<=N:
    #if N%Multiplier==0:
        #N=N/Multiplier
        #PrimeMultipliers.append(Multiplier)
    #else:Multiplier+=1
#print(f'Список простых множителей натурального числа =>',PrimeMultipliers)

#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

#PrimeryList=[1,2,3,5,1,5,3,10,10,5,2,2,4,4,8,12]
#PrimeryList=set(PrimeryList)
#NewList=list(PrimeryList)
#print(NewList)

#Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.


from os import remove
import random

NumberList=[]
N=10
for i in range(N):
    NumberList.append(random.randint(-N, N))

print(NumberList)
data=open('file.txt','w')
data.writelines(str(NumberList))
data.close

with open('file.txt','a') as data:
    i=0
    while i<len(NumberList):
        if int(NumberList[i]%2==0):
            NumberList.pop(i)
            data.writelines(str(NumberList))
        else:i+=1
        
print(str(NumberList))

#path='file.txt'
#data=open(path,'r')
#for numbers in data:
    #if numbers%2==0:




