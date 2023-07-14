def recursive_search(list,target):
    if len(list)==0:
        return False
    else:
        midpoint=(len(list))//2
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint]<target:
                return recursive_search(list[midpoint+1:],target)
            else:
                return recursive_search(list[:midpoint],target)
            

number=[1,2,3,4,5,6,7,8]
result=recursive_search(number,6)

print(result)