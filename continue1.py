#print values from 0 to 6 expect 3
num=0
for num in range(6):
    num=num+1
    if num==3:
        continue
    print("num has value",num)
print("end of loop")
