# O(L^3)
# Try all possible substrings (L^2) and insert in hashset
# Hashing a string is typically O(L)
def count_unique_substrings(str):
    st = set()  # internally hash-table

    for start in range(len(str)):
        for end in range(start, len(str)):
            substr = str[start:end+1]
            st.add(substr)

    return st, len(st)  # uniqe size
    # Note: Using a trie: we can efficiently solve it in O(L^2)
    # Don't create the string and add to trie
    # For every stating position: let the second loop keep inserting
    # In trie letter by letter and mark as leaf
    # Hence overall only 2 loops


def count_substrings_match(str1, str2):
    # just compute unique of the 2 strings and intersect them
    st1 = count_unique_substrings(str1)[0]
    st2 = count_unique_substrings(str2)[0]

    st = st1.intersection(st2)
    return len(st)


if __name__ == '__main__':
    assert count_unique_substrings("aaab")[1] == 7
    assert count_unique_substrings("aaaaa")[1] == 5
    assert count_unique_substrings("aaaba")[1] == 11
    assert count_unique_substrings("abcdef")[1] == 21

    assert count_substrings_match("aaab", "aa") == 2
    assert count_substrings_match("aaab", "ab") == 3
    assert count_substrings_match("aaaaa", "xy") == 0
    assert count_substrings_match("aaaaa", "aaaaa") == 5

