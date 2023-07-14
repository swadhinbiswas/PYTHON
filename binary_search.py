def binary_search(list,terget):
    frist=0
    last=len(list)-1
     
    while frist <= last:
         midpoint=(frist+last)//2
         
         if list[midpoint]==terget:
             return midpoint
         elif list[midpoint]< terget:
              frist=midpoint+1
         else:
             last=midpoint-1
             
    return None
 
list=[1,2,3,4,5,6,7,8,9]

result=binary_search(list,9)
print(result)
