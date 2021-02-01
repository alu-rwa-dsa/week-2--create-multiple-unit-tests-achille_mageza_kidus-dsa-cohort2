#QUESTION EIGHT

#first I define the list A that is composed of multiple lists
list_A = [[1,2,3,4],[2,3,4,5],[4,5,6,7],[7,8,9,10,2]]

#then i will merge the sublists into one large list 
def merge_list(list_A):
    #here I add a blank list that will enable me to prevent having duplicates
    list_B = []
    for sublist in list_A:
        for value in sublist:
            if value not in list_B:
                list_B.append(value)  
    print(list_B)

#here I call the function 
merge_list(list_A)


#Here I show the time and space complexity of this program:
#The time complecity (T1):
    # ==> T = O(n^2)

#The space complexity (T2):
    # ==> S = O(n)

