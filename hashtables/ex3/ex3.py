def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    #list/array

    list1=[1,2,3,4,5,3,4] 
    list2=[1,5,4,2,8,2,3]
    outputlist =[] 
    for item in list1:
        if item in list2 and not in outputlist :
            outputlist.append(item) 
    print(outputlist) 


    #return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
