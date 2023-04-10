

def hash_string(str):
    sum = 0
    base = 2 * 26 + 10; # lower, upper and 10 digits

    for ch in str:
        # lowers from [0-25], upper [26-51] and digits [52-61]
        if ch.islower():
            idx = ord(ch) - ord('a')
        elif ch.isupper():
            idx = ord(ch) - ord('A') + 26
        else:
            idx = ord(ch) - ord('0') + 26 * 2
        sum = sum * base + idx
    return sum


def hash_string_folding(str):
    sum = 0

    for start in range(0, len(str), 4):
        substr = str[start:start+4]
        sum += hash_string(substr)

    return sum


if __name__ == '__main__':
    print(hash_string_folding('01230123012'))
