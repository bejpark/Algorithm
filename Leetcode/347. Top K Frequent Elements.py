from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dict = sorted(Counter(nums).items(), key = lambda x:x[1], reverse=True)
        print(Counter(nums).items())
        for i in range(k):
            answer.append(dict.pop(0)[0])

        return answer