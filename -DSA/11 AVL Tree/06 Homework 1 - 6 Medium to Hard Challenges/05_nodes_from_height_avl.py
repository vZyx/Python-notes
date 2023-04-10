def avl_nodes_rec(height):
	if height == 0:
		return 1
	if height == 1:
		return 2

	return 1 + avl_nodes_rec(height - 1) + avl_nodes_rec(height - 2)


def avl_nodes_iter(height):
	if height == 0:
		return 1
	if height == 1:
		return 2

	height -= 1
	a, b = 1, 2
	c = None

	while height:
		c = a + b + 1
		a, b = b, c
		height -= 1

	return c

if __name__ == '__main__':
	for i in range(20):
		print(i, avl_nodes_iter(i), avl_nodes_rec(i))

'''
0 1 1
1 2 2
2 4 4
3 7 7
4 12 12
5 20 20
6 33 33
7 54 54
8 88 88
9 143 143
10 232 232
11 376 376
12 609 609
13 986 986
14 1596 1596
15 2583 2583
16 4180 4180
17 6764 6764
18 10945 10945
19 17710 17710

'''