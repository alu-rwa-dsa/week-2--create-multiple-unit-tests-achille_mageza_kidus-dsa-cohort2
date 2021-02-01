#QUESTION TEN
#THE UNIT TEST COMMENTED AT THE BOTTOM


def this_pattern(num):
    numList = []
    for x in range (1, num + 1):
        for y in range (1, x + 1):
            numList.append(x)
    print (numList)


this_pattern(3)
print("\n")
this_pattern(5)



#Showing the time and space complexity of this program:
#The time complecity (T1):
    # ==> T = O(n^2)

#The space complexity (T2):
    # ==> S = O(n^2)
