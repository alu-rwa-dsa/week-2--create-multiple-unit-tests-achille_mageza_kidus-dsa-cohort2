#QUESTION SIX


#first I import the module re(regural expression)
import re

#here I assign a variable anyword as a strin with blanks
any_sentence = "Good  Day!  I   am  a        2nd year   student     at     ALU."

def one_space(any_word):
    #then remove the blanks and replace each by one space
    print (re.sub("\s\s+" , " ", any_word))

one_space(any_sentence)



#Here I show the time and space complexity of this program:
#The time complecity (T1):
    # ==> T = O(1)

#The space complexity (T2):
    # ==> S = O(1)

