class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter

        # Count frequencies
        freq_map = Counter(arr)
        
        # Check for unique frequencies
        freq_set = set(freq_map.values())
        
        return len(freq_map) == len(freq_set)