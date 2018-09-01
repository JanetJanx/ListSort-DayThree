def missing_number(b):
    if len(b) != 0:
        first_list = []
        for x in range(b[0], b[-1]+1):
            first_list.append(x)
        new_b = set(b)
        
        return (list(new_b ^ set(first_list)))
    else:
        return "Empty List"

print (missing_number([]))
   

