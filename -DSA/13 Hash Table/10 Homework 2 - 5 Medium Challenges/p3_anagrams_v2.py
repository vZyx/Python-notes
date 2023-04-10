
def count_anagram_substrings(str):  # O(L^3)
    st = set()

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = str[start:end+1]
            # Represent each string in terms of letters frequency - O(1)
            # 2 anagrams have the same letters frequency!
            lst = [0] * 26
            for ch in substr:
                lst[ord(ch) - ord('a')] += 1
            st.add(tuple(lst))

    return len(st)





if __name__ == '__main__':
    assert count_anagram_substrings("abba") == 6
    assert count_anagram_substrings("aaaaa") == 5
    assert count_anagram_substrings("abcba") == 9
    assert count_anagram_substrings("aabade") == 17

