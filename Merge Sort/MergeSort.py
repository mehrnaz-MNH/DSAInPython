# break into lists of one item
# O(n log n ) time complexity



# takes sorted lists and combine
def merge(l_1 , l_2):
    res = []
    i = 0
    j = 0
    while i < len(l_1) and j < len(l_2):
        if l_1[i] < l_2[j]:
            res.append(l_1[i])
            i +=1
        else :
            res.append(l_2[j])
            j +=1


    while i < len(l_1):
        res.append(l_1[i])
        i +=1

    while j < len(l_2):
        res.append(l_2[j])
        j +=1

    return res


print (merge( [1,3,5,7,9,11] , [4 , 6 , 10 , 12, 13]))

def merge_sort(my_list):
    if len(my_list) == 1 :
        return my_list

    min_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:min_index])
    right = merge_sort(my_list[min_index :])

    return merge(left , right)







