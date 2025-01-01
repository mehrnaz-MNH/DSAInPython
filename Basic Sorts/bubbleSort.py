def bubble_sort(my_list):
    for i in range(len(my_list) -1 , 0 , -1):
        print("i :" , i)
        for j in range(i) :
            print("j :" , j)
            if my_list[j] > my_list[j+1]:
                print('my_list[j]' , j , my_list[j]  )
                print('my_list[j+1]' , j+1 , my_list[j+1]  )
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j + 1] = temp

    return my_list


print(bubble_sort([2,6,4,5,1,8,2]))



