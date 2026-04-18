# removing a prime number from the list using higher order function 
def prime_removemer(l):
    count =0
    for v in range(1,l+1):
        
        if l % v==0:
            count = count +1
    if count >2:
        return True     
    else:
        return False
l1 =[1,2,3,4,5,6,7,8,9,10]
result = list(filter(prime_removemer,l1))
print(result)