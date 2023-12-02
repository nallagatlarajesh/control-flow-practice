#progra to create four function calculator 
result=0
val1=float(input("enter value 1:"))
val2=float(input("enetr value 2:"))
op=input("enter any one of the operator (+,-,*,/):")
if op=="+":
    result=val1+val2
elif op=="-":
    if val1>val2:
        result=val1-val2
    else:
        result=val2-val1
elif op=="*":
    result=val1*val2
elif op=="/":
    if val2==0:
        print("error ! division by zero is not allowed .program terniated ")
    else:
        result=val1/val2
else:
    print("wrong input ,program terminated")
print("the result is ",result)
    
                
