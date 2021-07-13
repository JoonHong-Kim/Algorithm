class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #classify anagrams
        anagrams=collections.defaultdict(list)
        
        #for each strs to anagrams
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        #return values of anagrams
        return list(anagrams.values())
