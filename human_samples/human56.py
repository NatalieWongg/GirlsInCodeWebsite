word=input()
def palindrome(wordd, n): 
    if n==len(wordd)-1: 
        if wordd[0]==wordd[-1]: 
            return 1
    else: 
        if palindrome(wordd, n+1)==1 and wordd[n]==wordd[len(wordd)-1-n]: 
                return 1
        else: 
            return 0
            
print(palindrome(word, 0))
