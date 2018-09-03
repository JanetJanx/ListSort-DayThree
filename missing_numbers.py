#function that finds the missing numbers in the sequence
def missing_number(sequence):
    if len(sequence) != 0:
        first_list = [*range(sequence[0], sequence[-1]+1)]
            
        #filter duplicates in sequence
        new_sequence = set(sequence)
            
        return (list(new_sequence ^ set(first_list)))
    
    return sequence

print (missing_number([10,14,20]))
print (missing_number([]))