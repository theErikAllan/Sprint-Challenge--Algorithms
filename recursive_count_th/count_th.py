'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # We receive a string of unknown length
    # First, we set a base case so the recursion will stop when we reach the end of the word
    if len(word) > 1:
        # Next, we set a variable to the string we are looking for and its length
        target = "th"
        length_of_target = 2 
        print("This is word: ", word)
    
        # Then we write an if statement that checks the first two characters of the string to see if they match the target string
        if (word[0 : length_of_target] == target): 
            # If the first two characters do match, we recursively call the count_th() function and decrease the slice of "word" by 1 so we can traverse through the remaining string 
            # We also return +1 as this if statement confirms a match between the word we're looking at and the target string we're looking for
            return count_th(word[length_of_target - 1:]) + 1
    
        # If we don't find a match, we recursively call the count_th() function and decrease the slice of "word" by 1 so we can traverse through the remaining string 
        return count_th(word[length_of_target - 1:])
    else: 
        return 0

# Driver Code 
if __name__ == '__main__':
    word = "abcthxyzth"
    print(count_th(word))