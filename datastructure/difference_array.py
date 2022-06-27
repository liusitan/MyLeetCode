'''
Range Update, The key of difference array is to maintain a
d[i] = A[i] - A[i-1], in this way we can recvoer A[i] from A[i-1] + d[i]
moreover, if we wnat to update a range during in A from l to r, we update it 
d[l] += c d[r+1] -= c, why? 
Because A[l] = d[l] + A[l-1] since d'[l] = d[l] + c thus, A'[l] is c greater tHAN
A[l], since A[l+1] = d[l+1] + A[l] the A[l+1] is also c greater. However, when 
A[r+1] should not be increased, A'[r+1] = d[r+1] + A'[r], since A'[r] is c greater than 
the A[r] thus d[r+1] should be smaller
'''


from typing import List


class DifferenceArray:
    def __init__(self,A:List[int]) -> None:
        self.D = [0]* (len(A) + 1)
        self.D[0] = A[0]
        self.A = A
        for i in range(1,len(A)):
            self.D[i] = A[i] - A[i-1]
    def update(self,l,r,k): 
        self.D[l] += k
        self.D[r+1] -= k
    def print(self):
        # Actually I do not need an another p, since all the values are generated from D.
        p  = self.A.copy()
        p[0] = self.D[0]
        for i in range(1,len(self.A)):
            p[i] = self.D[i] + p[i-1]
        print(p)
t = [1,2,3,4,5]
da = DifferenceArray(t)
da.update(1,3,4)
da.print()
da.update(1,3,2)
da.print()