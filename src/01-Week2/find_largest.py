

num_list1 = [1, 3, 21, 9, 88, 77, 0, 20]
num_list2 = [10, 3, 21, 9, 88, 77, 0, 1000]


# Defining/creating the function:
def romeos_version_of_max( nlst ):
    print nlst
    largest = nlst[0]

    # Find the largest, and update the variable
    for number in nlst:
        if number >= largest:
            largest = number
    
    return largest

# Calling the function
print romeos_version_of_max(num_list1)
print romeos_version_of_max(num_list2)



