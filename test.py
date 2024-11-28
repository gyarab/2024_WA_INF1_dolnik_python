
def rotate_array(arr, n):
    if not isinstance(arr, list) or not isinstance(n, int):
        raise ValueError("Invalid arguments")
    if not arr:
        return arr
    if n >= 0:
        return arr[-n % len(arr):] + arr[:-n % len(arr)]
    else:
        return arr[-n % len(arr):] + arr[:-n % len(arr)]


def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument: text must be a string")
    if len(text) % 3 == 0:
        return [text[i:i+3] for i in range(0, len(text), 3)]
    else:
        last_string_length = len(text) % 3
        return [text[i:i+3] for i in range(0, len(text)-last_string_length, 3)] + [text[-last_string_length:]]


