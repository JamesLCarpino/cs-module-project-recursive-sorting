

# [7 4 8 1 2 9 3]
# #for a merge sort first step: SPLIT THAT SHIT IN HALF
# [7 4 8] & [1 2 9 3]
# #then what?
# #recursion -> split that shit again
# #when splitting an uneven number as long as you're consistent
# #just be consistent all the time -> controleld by < > ifs
# [7] & [4 8] & [1 2] & [9 3]
# #recurse again splitting it down now we have single elements
# [7] [I am here becuase you cant split a list of 1 ] [4] [8] [1] [2] [9] [3]
# #now begin the mergery aka STEP TWO
# [7] [4 8] [ 1 2][3 9]

# [4 7 8] [1 2 3 9]

# [1 2 3 4 7 8 9]
# below
# are the comparables at cursors

# #compare sub values of the arrays aka is ai > ak or vise versa when the samller is true add it
# # when done with one array copy in sub array becuase it already happened in previous recurision
# #that which is compared and is less will move over becuase that array index has been delt with
#       i
# a[4 7 8]
# b[1 2 3 9]
#         k

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    #given two arrays
    #combine them into a sorted array
    #do this by..

    #setting my pointers
    a = 0
    b = 0

    for i in range(0, elements):
        #if a is done
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b+=1
        #if b is done
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a+=1
        #if a is smaller
        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            #this iterates because we used a position so we have to go to next
            a+=1

        #if b is smaller
        else:
            merged_arr[i] = arrB[b]
            b+=1

    #step 1: compare first elements of each
    

    #step 2: add the smallest to the merged array

    #step 3: iterate the pointer for the smaller value

    #if one pointer reaches the end of its array push all remaining values

    # Your code here
    
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #notes
    #this function handles the divide part
    #base case: we don't need to divide anything anymore
    #base case = arr length 0 or 1
    if len(arr) > 1:
        
        #otherwise: division
        #find middle of aray with //2
        left = merge_sort(arr[0:len(arr)//2 ])
        right = merge_sort(arr[len(arr)//2 : ])
        #then divide to let and right
        #do merge sort on left and right

        #put it back together:
        #by mergin left and right
        arr = merge(left, right)

    # Your code here
    

    
    return arr


    # ==================
    #think of recusion by solving the smallest relevant/full problem
    #[4 7 3 1]
    #[4][7][3][1]
    #[4 7][1 3]
    # ==================


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
