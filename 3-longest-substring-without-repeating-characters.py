class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        limit=len(s)
        longest=0
        
        for i in range(len(s)):
            curr=1
            visited=[s[i]]
            for j in range(i+1,len(s)):
                if s[j] in visited:
                    break
                else:
                    visited.append(s[j])
                    curr+=1

            if (longest<curr):
                longest=curr

            #early-stopping
            if(curr+limit-i-2 <= longest):
                break

        return longest
