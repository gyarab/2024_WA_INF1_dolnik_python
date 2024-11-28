

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


class_duration = 45

break_durations = [5, 10, 20, 10, 10, 5, 5, 10, 10, 5, 5]

def class_and_break_time(start_class, end_class):
    if not isinstance(start_class, int) or not isinstance(end_class, int):
        raise ValueError("Invalid arguments: start_class and end_class must be integers")
    if start_class < 0 or start_class > 13 or end_class < 0 or end_class > 13 or start_class > end_class:
        raise ValueError("Invalid arguments: start_class and end_class must be between 1 and 7 and start_class must be smaller or equal to end_class")

    class_time = (end_class - start_class + 1) * class_duration
    break_time = sum(break_durations[start_class:end_class-1])

    return (class_time, break_time)

print(class_and_break_time(0,13))






