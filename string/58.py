

def lengthOfLastWord(s):
    
        l,r = 0,len(s)-1
        count = 0

        while r >= l and s[r] == " " :
            r-=1

        while r >= l and s[r] != " ":
            count += 1
            r-=1

        return count 
    
s = "fly me   to   the moon  "
print(lengthOfLastWord(s))