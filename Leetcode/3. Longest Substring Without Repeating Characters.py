class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        cal=[0 for _ in range(n)]
        if len(s)==0:
            return 0
        for i in range(n):
            substr=""
            for str in s[i:]:
                if str in substr:
                    break
                else:
                    substr+=str
            cal[i]=len(substr) #중간에 중복을만나지않고 끝까지 간 경우도 있기때문에
                                #if문이 끝난 후 현재까지 값을 넣는다.
           
                
        #print(cal)
        return max(cal)
