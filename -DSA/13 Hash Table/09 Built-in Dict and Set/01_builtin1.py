# immutables: int, float, tuple, string
# be careful from float as it is an approximate - don't

class Employee:
    pass

dict = {
    -1200001 : 'mostafa',
    'ziad' : 25.5,
    (4, 6) : [5, 8, 9],
    'Hey' : Employee(),
    16 : {6:90},     # value is another dict
    int: [6, 9, 10],
    #[1, 2] : 10    TypeError: unhashable type: 'list'
    #([1, 2]) : 10   TypeError: unhashable type: 'list'
}
print(dict[(4, 6)]) # [5, 8, 9]

st = set()
st.add(10)
st.add(10)
st.add(10)

print(len(st))      # 1

