"""
Among the first 370 thousand square numbers, what is the sum of all the odd squares?
"""
result = 0
n = 0

for i in range(370000):
    if not i % 2 == 0:
        result = i * i
        n += result
print("n :" , n)

## Answer : n = 8442166666605000


        