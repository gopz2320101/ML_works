def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return print(arr)

list1=[1,4,3,2]
list2=[3,2,1]

add=lambda list:bubble_sort(list)

add(list1)
add(list2)