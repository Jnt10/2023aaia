class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) # 課本第2章的字串, 有教 .split() 和 .join()
        b = ''.join(word2) #單單.join
        
        if a==b: return True
        else: return False