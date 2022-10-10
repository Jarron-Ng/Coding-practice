### Practice for permutations
# Author: Jarron Ng


#Question 1, check if a given string is a permutation of a substring in b
# Time complexity: O(ab)

def is_permutation(a, b):
    # take a and convert it a dictionary with the letters as keys and their frequency as values
    # take a and convert it to a set to check for unused letters in b and skip them
    
    a_dict = {}
    for letter in a:
        if letter in a_dict:
            a_dict[letter] += 1
        else:
            a_dict[letter] = 1

    a_set = set(a)


    # iterate through b and check if the letter is in a_dict
    b_dict = {}
    list_of_permutations = []
    count = 0

    for i in range(0, len(b)-len(a)+1):
        # checks if the letter is in a_dict, if not, skip it
        if b[i] in a_set:
            # adds each letter and its frequency to b_dict
            for j in range(i, i+len(a)):
                # another way of getting the frequency of each char in a string into a dict
                b_dict[b[j]] = b_dict.get(b[j], 0) + 1 

            # check if both dicts are equal and permutation is not repeated    
            if b_dict == a_dict and b[i:i+len(a)] not in list_of_permutations:
                list_of_permutations.append(b[i:i+len(a)])
                count += 1

            # reset b_dict
            b_dict = {} 
    
    return list_of_permutations, count

permutations, count = is_permutation("abbc", "cbabadcbbabbcbabaabccbabc")
print(permutations, count)