#checking for palindrome 
def palindrome(list1):
    for val in list1:
        temp = str(val)
        original = temp 
        reverse = temp[::-1]
    if reverse != original:
        list1.remove(val)
    return list1

list1=list((map(int,input("enter a set of numbers").split())))
lst2 = palindrome(list1)
print(list1)
