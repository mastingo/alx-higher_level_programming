#!/usr/bin/python3
result =""
for i in range(10):
    for j in range(i + 1, 10):
        result += "{:d}{:d} ,".format(i, j)
result = result.rstrip(', ')
print(result)
