address_book = {
    "Alicia Johnson": "123 Main Street, Cityville",
    "Jerry Smith": "456 Corner Avenue, Townsville",
    "Michael Jonas": "789 End Lane, Villageville"
}
get_name=[]
for key in address_book:
    first_name=key.split()[0]
    print(first_name)
    get_name.append(first_name)
    

get_value=[]
for key,value in address_book.items():
    value=value
    print(value)
    get_value.append(value)


print(get_value)
print(get_name)