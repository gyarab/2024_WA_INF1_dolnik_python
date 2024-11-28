
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


def count_vowels_and_consonants(text):
    if not isinstance(text, str):
        raise ValueError("Invalid argument: text must be a string")
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ů', 'ý', 'ě']
    consonants = ['b', 'c', 'č', 'd', 'ď', 'f', 'g', 'h', 'ch', 'j', 'k', 'l', 'm', 'n', 'ň', 'p', 'r', 'ř', 's', 'š', 't', 'ť', 'v', 'z', 'ž']
    vowel_count = 0
    consonant_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
    
    return {'vowels': vowel_count, 'consonants': consonant_count}





