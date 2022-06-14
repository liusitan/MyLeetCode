1. when traverses the linkedlist, did not write the h.next
```
while h:
    use(h)
    h = h.next!
```
2. when using fast slow pointer, to get the middle innode
index from 0
for n is odd, n//2
for n is even,n//2 - 1
```
while(fast.next!=None and fast.next.next!=None):
    fast = fast.next.next
    slow = slow.next
```