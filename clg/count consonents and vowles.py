#count consonents and vowles
def count(str):
    countv=0
    countc=0
    v= ['a','A','e','i','o','u','E','I','O','U']
    for val in str:
        if val in v:
            countv+=1
        else:
            countc+=1
    return countv,countc
string =input("enter a string")
print(count(string))