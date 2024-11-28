
def rotate_array(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int):
        raise ValueError("Invalid arguments")
    if not arr:
        return arr
    if n >= 0:
        return arr[-n % len(arr):] + arr[:-n % len(arr)]
    else:
        return arr[-n % len(arr):] + arr[:-n % len(arr)]



