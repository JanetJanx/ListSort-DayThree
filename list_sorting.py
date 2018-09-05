#function to sort elements according to evens, odds and characters
def list_sort(a):
    #a is the provided list
    if isinstance(a, list):
        #list categories
        word_cat = ['evens','odds','chars']
        #sorted dictionary
        sorted_dictionary = {}
        #categorized lists
        char_list = []
        evens_list = [] 
        odds_list = []

        for x in a:
            if isinstance(x, str) and x is not False and x is not True:
                char_list.append(x)    
            elif x % 2 == 1 and x is not False and x is not True:
                evens_list.append(x)  
            elif x % 2 == 0 and x is not False and x is not True:
                odds_list.append(x)
            else:
                return "List contains boolean values"

        sorted_dictionary[word_cat[2]] = char_list
        char_list.sort()
        sorted_dictionary[word_cat[1]] = evens_list
        evens_list.sort()
        sorted_dictionary[word_cat[0]] = odds_list
        odds_list.sort()

    else:
        return "Not a List"
        
    return sorted_dictionary


#call function for list 
print (list_sort([2,0,6,5,1,7,'z','a']))
print (list_sort([4,9,7,8,False,True,'d','g','!']))
print (list_sort([]))