#program te print the positive difference of two numbers
num1=int(input("first number:"))
num2=int(input("second number:"))
if num1>num2:
    diff=num1-num2
else:
    diff=num2-num1
print("the diffenrece of ",num1,"and",num2,"is ",diff)
