class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for stri in strs:
            ans += str(len(stri)) + '#' + stri
        return ans 

      
    def decode(self, s: str) -> List[str]:
       
        res = []
        i = 0
    
        while i < len(s):
            j = i
            
            # find '#'
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            
            i = j + 1 + length

        return res
            



    





            
        