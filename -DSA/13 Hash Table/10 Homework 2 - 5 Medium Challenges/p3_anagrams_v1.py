
def count_anagram_substrings(str):  # O(L^3 logL)
    st = set()

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = tuple(sorted(str[start:end+1]))   # Sort in O(L logL)
            st.add(substr)

    return len(st)





if __name__ == '__main__':
    assert count_anagram_substrings("abba") == 6
    assert count_anagram_substrings("aaaaa") == 5
    assert count_anagram_substrings("abcba") == 9
    assert count_anagram_substrings("aabade") == 17

