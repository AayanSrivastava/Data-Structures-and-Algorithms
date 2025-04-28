def max_sum_sliding_window(arr, k):
    if len(arr) < k or k <= 0:
        return "Invalid input"

    # Calculate the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window over the array
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print("Maximum sum of subarray of size", k, "is:", max_sum_sliding_window(arr, k))