#QUESTION SEVEN

#Here I assign the varibale any_word
word1 = "Mageza"
word2 = "DSA"

#Then i define the function to count occurences of each element of the string
def occurence_count(any_word):
    print(any_word, ":")
    for i in any_word:
        n = any_word.count(i)

        print(i, ":", n)

occurence_count(word1)
print("\n")
occurence_count(word2)



#Here I show the time and space complexity of this program:
#The time complecity (T1):
    # ==> T = O(n)

#The space complexity (T2):
    # ==> S = O(n)


