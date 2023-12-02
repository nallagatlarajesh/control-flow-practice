      
#find the factors of a number using while loop
num=int(input("enter  a number to find its facteor "))
print(1,end=" ")#1 is a factor for every number
factor =2
while factor <=num/2:
    if num%factor==0:
        print(factor ,end=" ")
    factor+=1
print(num,end=" ")#every number is afactor of itself

