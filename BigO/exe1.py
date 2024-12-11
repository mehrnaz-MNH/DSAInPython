def print_items(n):
    for i in range(n):
        print(i)

def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

def add_items(n):
    return n+n



print_items(10)
# BigO is O(n) here which is proportional
# How to simplify ? drop constants 2n ? n

print_items_2(10)
#BigO is O(n**2) here
# How to simplify ? n**2 + n ? n**2 ( Drop non-dominant )

print(add_items(10))
# this is O(1) or constant time
# as n increases number of operations doesn't increase