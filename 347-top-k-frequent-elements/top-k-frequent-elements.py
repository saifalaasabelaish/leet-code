class Solution:
    def topKFrequent(self, arr, k):
        count_map = Counter(arr)
        
        frequencies = list(count_map.values())
        frequencies.sort(reverse=True)
        
        top_k_frequencies = frequencies[:k]
        
        result = []
        for i, j in count_map.items():
            if j in top_k_frequencies:
                result.append(i)
        
        return result