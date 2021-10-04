from GeneralHashFunctions import BKDRHash as HashFuc
"""
经过比较 BKDRHash算法速度最快
"""

class HashTable(object):
    def __init__(self,b=14):
        self.b=b
        self.table=self.make_hashtable()

    def make_hashtable(self):
        return [set() for i in range(self.b)] # 采用set()更快

    def hash_string(self,keyword):
        return HashFuc(keyword)%self.b

    def hashtable_get_bucket(self,keyword):
        return self.table[self.hash_string(keyword)]

    def hashtable_lookup(self,keyword):
        return keyword in self.hashtable_get_bucket(keyword)

    def hashtable_add(self,keyword):
        self.table[self.hash_string(keyword)].add(keyword)
    
    def check(self):
        for bucket in self.table:
            print(len(bucket))