class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for x in range(numRows)]
        i=0
        while i < len(s):
            #go-down
            for j in range(numRows):
                if i < len(s):
                    rows[j]=rows[j] + s[i]
                    i+=1
                else:
                    break
            #go-upper-right
            for j in range(numRows-2):
                if i < len(s):
                    rows[numRows-j-2] = rows[numRows-j-2] + s[i]
                    i+=1
                else:
                    break
        res=''
        for i in rows:
            res+=i
        return res
            
