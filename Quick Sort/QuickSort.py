def swap(ls, si, i):
    temp = ls[si]
    ls[si] = ls[i]
    ls[i] = temp



def pivot(ls , pi , ei):
    si = pi
    for i in range(pi+1 , ei+1):
        if ls[i] < ls[pi]:
            si  +=1
            swap(ls , si , i )

    swap(ls , pi , si)
    return si

def quick_sort_h(ls , l , r):
    if l < r :
      pi = pivot(ls , l , r)
      quick_sort_h(ls , l , pi-1)
      quick_sort_h(ls , pi + 1, r)

    return ls

def quick_sort(my_list):
    quick_sort_h(my_list , 0 , len(my_list) -1 )


# worst case , all sorted . O(n2)
# not in order : O(n log n )












ls = [4,6,1,7,3,2,5]
print(ls)
pivot(ls , 0 , 6)
print(ls)

