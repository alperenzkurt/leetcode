class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp=str(x)
            temp=temp[1:]
            temp='-' + temp[::-1]
            temp=int(temp)
        else:
            temp=int(str(x)[::-1])
        if temp>2**31 or temp<=(-2**31):
            return 0
        return temp
