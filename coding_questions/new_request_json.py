import requests

url = 'https://coderbyte.com/api/challenges/json/age-counting'

response = requests.get(url)
data = response.json()


count=0
age=[]
for key,values in data.items():
    
    values=values.split(",")
    
    for item in values:
        
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


print("Number of items with age equal to or greater than 50:", count)