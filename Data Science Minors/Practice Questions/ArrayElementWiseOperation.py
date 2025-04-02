arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [9,8,7,6,5,4,3,2,1]

add = [i + j for i, j in zip(arr1, arr2)]
subtract = [i - j for i, j in zip(arr1, arr2)]
multiply = [i * j for i, j in zip(arr1, arr2)]
divide = [i / j for i, j in zip(arr1, arr2)]

print(add, subtract, multiply, divide, sep="\n")