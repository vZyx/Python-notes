
# id() function returns a unique id for the specified object.
# In CPython impl = It is the object memory address

name = 'mostafa'
another = name

print(id(name))         # 140296414377200
print(id(another))      # 140296414377200

x = 10
print(id(x))            # 94845838730272

