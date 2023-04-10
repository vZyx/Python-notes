
if __name__ == '__main__':

    print(hash(1234))       # 1234
    print(hash(15 ** 90))   # 700929717616031145
    print(hash(1.8))        # 1844674407370955265
    print(hash("abcde"))    # -2891589161269220084      Can be negative
    print(hash("bcdea"))    # 6676030291114009290       May change over runs
    print(hash("bcdea"))    # 6676030291114009290       MUST be same as previous
    print(hash((90, -10, 50)))  # 2459563228658516423
    #print(hash([90, -10, 50]))  # TypeError: unhashable type: 'list'

    # For security reasons, hash value my change between runs
    # BUT fixed during a single run

    # https://stackoverflow.com/questions/27522626/hash-function-in-python-3-3-returns-different-results-between-sessions

