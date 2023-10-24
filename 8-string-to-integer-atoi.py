class Solution:
    def myAtoi(self, s: str) -> int:
        #words before digits check:
        num=''
        numbersNow=False
        signNow=False
        for i in s:
            if i==' ':
                if numbersNow:
                    break
                if signNow:
                    return 0
            elif i.isdigit():
                num+=i
                numbersNow=True
                
            elif i=='+' or i=='-':
                if numbersNow:
                    break
                if signNow:
                    break
                num+=i
                signNow=True
            else:
                if not numbersNow:
                    num=0
                break
        try:
            num=int(num)
        except:
            return 0

        if num>=2**31:
            num=(2**31) -1
        if num<-2**31:
            num=-2**31
        return num
