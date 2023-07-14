def liner_search(list,target):
    for x in range(0,len(list)):
        if list[x]==target:
            return x
    return None

def verify(index):
    if index is not None:
        return False
    else :
        return True
    
    
barry=[1,2,3,4,6,7,8,9,0,2,1,5,14,56]

result=liner_search(barry,14)

print(result)

