#find prime factor of number and return a list
def pf(num):
    list1=[]
    for v in range(2,num+1):
        if num % v ==0:
            count=0
            for a in range(1,v+1):
                if v%a==0:
                    count+=1
            if count<3 and v not in list1:
                list1.append(v)
    return list1
num = int(input("enter a number"))
print(pf(num))