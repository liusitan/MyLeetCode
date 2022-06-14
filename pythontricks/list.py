
# List A length n
# [::-1] automatically filled with [n-1:-1:-1]
# [::1] automatically filled with [0:n:1]
print(range(10)[::-1])
print(range(10)[::1])
# convert deque to list list(deque([1,2]))