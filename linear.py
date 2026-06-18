#Linear Search

arr = [10, 25, 30, 45, 50]
key = 30

position = -1

for i in range(len(arr)):
    if arr[i] == key:
        position = i
        break

if position != -1:
    print("Element found at index:", position)
else:
    print("Element not found")
