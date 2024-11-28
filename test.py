
def rotate_array(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int):
        raise ValueError("Invalid arguments")
    if n >= 0:
        return arr[-n:] + arr[:-n]
    else:
        return arr[-n:] + arr[:-n]




