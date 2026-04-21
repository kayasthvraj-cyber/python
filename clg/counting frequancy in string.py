#counting frequancy in string 
def count(st):
    ls= st.split( )
    dic={}
    
    for val in ls:
        count=0
        for v in ls:
            if val == val:
                count+=1
            else:
                continue
    if val not in dic:
        dic.update({val:count})
        count=0
    
             
    return dic

st=input("enter the string")
print(count(st))