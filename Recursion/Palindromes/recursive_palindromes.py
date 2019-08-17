def palindrome(word): 
    if (len(word) == 1):
        return True
    
    if ((len(word) == 2) and (word[0] == word[1])):
        return True
    
    if (word[0] == word[-1]): 
        word = word[1:-1]
        print (word)
        return palindrome(word)
    else: 
        return False

potential_palindrome = (input("what word \n")).lower()

print(palindrome(potential_palindrome))
