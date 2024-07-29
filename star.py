from itertools import permutations

def generate_permutations(arr, n):
    perm = permutations(arr)
    
    result = []
    count = 0
    for p in perm:
        num_str = ''.join(map(str, p))
        result.append(num_str)
        print(num_str)
        count += 1
        if count >= n:
            break
    
    return result
arr = [2, 4, 8]
n = 1000

print(f"Generating permutations using digits: {arr}")
print("Output:")
generate_permutations(arr, n)
