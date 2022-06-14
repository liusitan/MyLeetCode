class static:
    a = 0
    def __init__(self):
        return None
s1 = static()
s2 = static()
s1.a+=1
s2.a+=1
print(s1.a)