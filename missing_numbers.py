def missing_number(b):
    if b:
        first_list = [*range(b[0], b[-1]+1)]
        
        new_b = set(b)
        
        return (list(new_b ^ set(first_list)))
    
    return "Empty List"

print (missing_number([10,14,20]))
print (missing_number([]))
   

