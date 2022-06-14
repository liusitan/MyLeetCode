from typing import List


# union:merge two subset
# find: determine which subset a element is in. 
# purpose, better merge> 
class DisJointSet(object):
    
    roots:List[int]
    # set_size:List[int]
    def __init__(self,size:int):
        self.roots = list(range(size))
        # set_size = [1] * size
    def union(self, a, b):
        ar = self.find(a)
        br = self.find(b)
        if(ar > br): 
            self.roots[br] = ar
        else:
             self.roots[ar] = br
        
    def find(self,x):
        while(x != self.roots[x]):
            x = self.roots[x]
        
        return x
    
s = DisJointSet(5)
s.union(1,2)
assert s.find(1) == 2
s.union(3,4)
s.union(0,3)
assert s.find(0) == 4
