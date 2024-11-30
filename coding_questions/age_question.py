def get_age(tem:dict):
    count=0
    age=[]
    for key,values in tem.items():
        print(key)
        print(values)
        values=values.split(",")
        print(values)
        for item in values:
            print(item)
            i=item.split("=")
            if i[0] =='age':
                age.append(int(i[1]))
                
            
            # for item in i:
            #     age.append(item)
                # if item[0]=="age":
                #     age.append(item[1])
    print(age)
    for i in age: 
        if i >= 50:
            count+=1
            
            
    print(count)
        
            
        
        
            
            
 
   
                # if item[0] == "age" and item[1]>=50:
                #     count+=1
                #     print(count)
                # else:continue
                    
                    
temp={"data":"key=igpfk,age=58,key=uhggs,age=64"}
get_age(temp)