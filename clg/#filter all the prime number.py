#filter all the prime number 
def pn(n):
    if n%2==0:
        return True
    else:
        return False
inpt=list(map(int,input("enter the list and give space between the numbers : ").split()))
filtered = list(filter(pn,inpt))
print(filtered)