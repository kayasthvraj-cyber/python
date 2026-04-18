#writing a function to reverse the words inside a string '
def rev(str):
    list2= list(str.split())
    list3=""
    for val in list2:
        rev = val[::-1]
        list3+=rev+" "
    
    return list3
string = input("enter the words ")
print(rev(string))