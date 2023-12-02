#find the sum of all the positive numbers enterd by 
# the user till the user enetrs a negative number
entry=0
sum1=0
print("enter numbers to find their sum ,negative  number ends the loop:")
while True:
    entry=int(input())
    print(entry)
    if (entry<0):
        break
    sum1+=entry
print("sum=",sum1)
