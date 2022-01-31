# use prefix tree
# Brute Force Solution: every search of any words

class TrieNode:
    def __init__(self) -> None:
        # hash map 
        # a: TrieNode, b: TrieNode 2
        self.children = {}
        # whether node is end of word
        self.word = False

class WordDictionary:

    def __init__(self):
        # root of word dictionary tree is None
        self.root = TrieNode()
        
    # create Trie based on word dictionary 
    def addWord(self, word: str) -> None:
        cur = self.root
        
        # check each character of a word
        for c in word:
            # if this character is not already inserted
            if c not in cur.children:
                # create new TrieNode for character c
                cur.children[c] = TrieNode()
            
            # cur.children[c] must exist, since we already checked and created new one if it does not existed
            cur = cur.children[c]
        
        # at the end of the word, set True
        cur.word = True
        
        
    # recursive solution
    def search(self, word: str) -> bool:
        
        # j: index parameter, root: node
        def dfs(j, root):       
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                # if c is .(dot) , potentially we have to go down 27 choices
                # -> we check them iteratively easily = recursion
                if c == ".":
                    # ex) ".ab"
                    # cur.children is hash map (all children of the node)
                    for child in cur.children.values():
                        # we have to skip the dot, and shift next sub tree
                        if dfs(i+1, child): # find path
                            return True
                    return False
                # regular character
                else:
                    # c does not exist
                    if c not in cur.children:
                        return False

                    # if it does exist, shift current node
                    cur = cur.children[c]
            
            # finishing loop means we can reach at the end of the word
            # "return True" is not correct here, 
            # because we check wether word dictionary tree has the word, or not
            # if we return True, we cannot distinguish whether current node is end of word in word dictionary or middle of the word.
            return cur.word
        
        
        return dfs(0, self.root)
        
        
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
            
        

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        
                        if dfs(i+1, child): # true from c's next to leaf node
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children

            return cur.word
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)