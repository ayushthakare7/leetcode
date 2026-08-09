from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Convert list to set for O(1) lookups
        wordSet = set(wordList)
        
        # If the target word isn't in the list, no valid sequence exists
        if endWord not in wordSet:
            return 0
        
        # Queue stores tuples of (current_word, current_sequence_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, level = queue.popleft()
            
            # If target word is reached, return the sequence length
            if current_word == endWord:
                return level
            
            # Try changing each character of the current word
            for i in range(len(current_word)):
                original_char = current_word[i]
                
                # Swap character with all lowercase letters 'a' through 'z'
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                    
                    # Form the new word variant
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If variant exists in our available word pool
                    if next_word in wordSet:
                        queue.append((next_word, level + 1))
                        # Remove to prevent infinite loops and redundancy
                        wordSet.remove(next_word)
                        
        return 0
