def counting_sort(arr):

    if not arr:
        return []  

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        
        sorted_arr.extend([i] * count[i])

    return sorted_arr

if __name__ == "__main__":

    numbers = [4, 2, 2, 8, 3, 3, 1]
   
    print("Original array:", numbers)

    sorted_numbers = counting_sort(numbers)
    print("Sorted array:", sorted_numbers)
