#function to sort elements according to evens, odds and characters
def list_sort(a):
    #a is the provided list
    if not isinstance(a, list):
        return "Not a List"
    #list categories
    word_cat = ['evens','odds','chars']
    #sorted dictionary
    sorted_dictionary = {}
    #categorized lists
    char_list = []
    evens_list = [] 
    odds_list = []

    for x in a:
        if isinstance(x, str):
            char_list.append(x)    
        elif x % 2 == 1 and type(x) == int:
            evens_list.append(x)  
        elif x % 2 == 0 and type(x) == int:
            odds_list.append(x)

    sorted_dictionary[word_cat[2]] = sorted(char_list)
    
    sorted_dictionary[word_cat[1]] = sorted(evens_list)
    
    sorted_dictionary[word_cat[0]] = sorted(odds_list)

        
    return sorted_dictionary


#call function for list 
print (list_sort([2,0,6,5,1,7,'z','a']))
print (list_sort([4,9,7,8,False,True,'d','g','!']))
print (list_sort([]))