#string simple leetcode 

def string_replace(comand:str)->str:
    comand=comand.replace("()","o").replace("G","g")
    return comand


a="G()al"

st=string_replace(a)
print(st)