#QUESTION NINE
#THE UNIT TEST COMMENTED AT THE BOTTOM


#First define the function for finding the difference btn the lists
def difference(list_A, list_B):
    return (list(list(set (list_A) - set (list_B))))
    
#Here I define the list A and the list B
list_A = [1,9,2,3,4,5]
list_B = [1,2,3,4,5]


print (difference(list_A, list_B))


#Showing the time and space complexity of this program:
#The time complecity (T1):
    # ==> T = O(1)

#The space complexity (T2):
    # ==> S = O(1)




