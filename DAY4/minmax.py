arr=[2,6,34,21,9,4]
arr.sort()
min_sum=sum(arr[:len(arr)-1])
max_sum=sum(arr[1:])
diff=abs(min_sum-max_sum)
print(diff)