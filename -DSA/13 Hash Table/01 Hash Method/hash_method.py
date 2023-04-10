

def hash_integer(num, range):
    return num % range


def hash_string1(str, range):
    sum = 0

    for ch in str:
        sum += ord(ch) - ord('a')   # idx from 0-25
    return sum % range

def hash_string2(str, range):
    sum = 0

    for ch in str:
        idx = ord(ch) - ord('a')    # 0-25 range
        sum = sum * 26 + idx
    return sum % range

if __name__ == '__main__':

    #print(hash_integer(100, 1000))      # 100
    #print(hash_integer(100, 19))        # 5

    #print(hash_string1("abc", 7))       # 0+1+2 = 3 % 7 = 3
    #print(hash_string1("abcde", 70))    # 0+1+2+3+4 = 10 % 70 = 10
    #print(hash_string1("abcde", 7))     # 10 % 7 = 3
    #print(hash_string1("bcdea", 7))     # 10 % 7 = 3    SAME chars
    #print(hash_string1("abcwz", 7))     # 50 % 7 = 1

    #print(hash_string2("abc", 7))       # 0+1*26+2 = 28 % 7 = 0
    # 1 * 26 * 26 * 26 + 2 * 26 * 26 + 3 * 26 + 4 = 19010
    #print(hash_string2("abcde", 70))    # 19010 % 70 = 40
    #print(hash_string2("abcde", 7))     # 19010 % 7 = 5
    #print(hash_string2("bcdea", 7))     # 494260 % 7 = 4
    #print(hash_string2("abcwz", 7))     # 19525 % 7 = 2

    print(hash(1234))       # 1234
    print(hash(15 ** 90))   # 700929717616031145
    print(hash("abcde"))    # -2891589161269220084  May change over runs
    print(hash("bcdea"))    # 6676030291114009290
    print(hash("bcdea"))    # 6676030291114009290   MUST be same as previous
    print(hash((90, -10, 50)))  # 2459563228658516423
    #print(hash([90, -10, 50]))  # TypeError: unhashable type: 'list'

    # For secuirty reasons, hash value my change between runs
    # BUT fixed during a single run
    # https://stackoverflow.com/questions/27522626/hash-function-in-python-3-3-returns-different-results-between-sessions






