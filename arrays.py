arr = [64, 34, 25, 12, 22, 11, 90]
print("Before: ", arr)

arr.sort()
print("Sort: ", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
arr.append(199)
print("Append: ", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
arr.reverse()
print("Reverse: ", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
arr.insert(0, 199) # 2 args, index and value
print("Insert: ", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
arr.pop()
print("Pop: ", arr)

arr2 = ["Hello", "World"]
arr2.remove('World')
print("Remove: ", arr2)

arr = [64, 34, 25, 12, 22, 11, 90]
arr2 = ["Hello", "World"]
arr.extend(arr2)
print("Extend: ", arr)

arr = [64, 34, 25, 25, 12, 22, 11, 90]
n = arr.count(25)
print("Count: ", n)

arr = [64, 34, 25, 25, 12, 22, 11, 90]
l = len(arr)
print("Lengtht: ", l)

arr = [64, 34, 25, 25, 12,  12, 22, 11, 90]
print("Before: ", arr)
arrSet = set(arr)
print("Set ", arrSet)