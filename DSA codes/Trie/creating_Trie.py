class Trie:
    head={}

    def add(self,word):
        cur=self.head
        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True
    
    def search(self,word):
        cur=self.head
        for ch in word:
            if ch not in cur:
                return False
            cur=cur[ch]
        
        if '*' in cur:
            return True
        else:
            return False
    
    def startswith(self,prefix):
        cur=self.head
        for ch in prefix:
            if ch not in cur:
                return False
            cur=cur[ch]
        return True



diction=Trie()
diction.add('Hi')
diction.add('Hello')
diction.add('Hey')
print(diction.search('Hi'))
print(diction.search('Hil'))
print(diction.startswith('Hel'))
print(diction.startswith('He'))
print(diction.startswith('Help'))