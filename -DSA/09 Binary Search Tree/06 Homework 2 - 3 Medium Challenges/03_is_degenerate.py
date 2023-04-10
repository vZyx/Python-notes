
def is_degenerate(preorder):
    # We need each child to have 1 node only
    # Assume we have a degenerate of 5 nodes and we want to add another node
    # Then self node must start from root and keep moving tell the leaf node
    # It means at any stage it must respect specific [min, max] range to not create 2 children
    # The idea: for each node, maintain what is the only valid range
    # Assume the last value is 300 and next value is 700
    # it means 700 on its right side and from now on, node must be >= 701 to arrive as a leaf

    # The more of solution: if degenerate is branch, can compute [mn, mx] per node for validation
    if len(preorder) <= 2:
        return True

    mn, mx = float('-inf'), float('inf')

    # Validate the generate branch is always fitting with updated range
    for i in range(1, len(preorder)):
        if not (mn < preorder[i] < mx):	# exclusive
            return False

        if preorder[i] > preorder[i - 1]:	# on its right subtree: so I am smaller than all next
            mn = preorder[i - 1]
        else:
            mx = preorder[i - 1]

    return True
    # Other approaches: https:#www.geeksforgeeks.org/check-if-each-internal-node-of-a-bst-has-exactly-one-child/



if __name__ == '__main__':
    assert is_degenerate([25, 8, 11, 13, 12]) == True
    assert is_degenerate([100, 70, 101]) == False
    assert is_degenerate([100, 70, 60, 75]) == False
    assert is_degenerate([100, 70, 60, 65]) == True
    assert is_degenerate([9, 8, 7, 6, 5, 4, 3]) == True
    assert is_degenerate([500, 400, 300, 200 , 250 , 275, 260]) == True
    assert is_degenerate([500, 400, 300, 200 , 250 , 275, 260, 280]) == False

