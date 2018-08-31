#function to sort elements according to evens, odds and characters
def list_sort(a):
    if isinstance(a, list):
        #list categories
        word_cat = ['evens','odds','chars']
        #sorted lis
        sorted_list = {}
        char_list = []
        evens_list = [] 
        odds_list = []
        for x in a:
            if isinstance(x, str):
                char_list.append(x)
                sorted_list[word_cat[2]] = char_list
                char_list.sort()
            elif x % 2 == 1:
                evens_list.append(x)
                sorted_list[word_cat[1]] = evens_list
                evens_list.sort()
            elif x % 2 == 0:
                odds_list.append(x)
                sorted_list[word_cat[0]] = odds_list
                odds_list.sort()
            else:
                return False

    else:
        return "Not a List"
        
    return sorted_list


#call function for list 
print (list_sort([2,0,6,5,1,7,'z','a']))