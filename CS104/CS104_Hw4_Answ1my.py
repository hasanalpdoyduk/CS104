def sum_of_the_same_valeus_on_two_lists():
    input_string1 = input("Enter elements of a list separated by space: ")
    list1 = input_string1.split()
    input_string2 = input("Enter elements of a list separated by space: ")
    list2 = input_string2.split()

    sum_list = []

    for i in range(len(list1)):
        list1[i] = int(list1[i])
    for i in range(len(list2)):
        list2[i] = int(list2[i])

    print("list1: ", list1)
    print("list2: ", list2)

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                sum_list.append(list1[i])

    print(sum(sum_list))
    return(sum(sum_list))

sum_of_the_same_valeus_on_two_lists()

