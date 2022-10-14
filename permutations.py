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


#Question 2, generate permutations of a string using recursion

def permute(string):
    permute_recurse(string, "")


def permute_recurse(string, prefix):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            permute_recurse(rem, prefix + string[i])


# Qn3, count the number of character occurrences in a string and appen the letter and the count
# O(n) time complexity
def count_letters(string):
    count = 0
    out = ""
    for i in range(len(string)-1):
        count += 1
        if string[i] != string[i+1]:
            out = f"{out}{string[i]}{count}"
            count = 0
    if string[-1] != string[-2]:
        out = f"{out}{string[-1]}1"
    else:
        out = f"{out}{string[-1]}{count+1}"

    return out

print(count_letters("aabcccccaab"))

# Qn4, check if a string is a reverse of another
def check_reverse(string1, string2):
    if len(string1) != len(string2):
        return False
    else: 
        return string1[-1:-len(string1)-1:-1] == string2

print(check_reverse("hello", "olleh"))
print(check_reverse("hello", "ollew"))
    