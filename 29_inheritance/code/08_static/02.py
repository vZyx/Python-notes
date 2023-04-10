

class A:
    shared = 1

class B(A):
    pass

class C(A):
    pass


if __name__ == '__main__':
    print(A.shared, B.shared, C.shared)  # 1 1 1
    A.shared = 3
    print(A.shared, B.shared, C.shared)  # 3 3 3
    # With MRO: B and C, use A.shared

    B.shared = 5    # Now B has its own shared
    print(A.shared, B.shared, C.shared)  # 3 5 3
    # Still C with MRO use A.shared

    A.shared = 7
    print(A.shared, B.shared, C.shared)  # 7 5 7
    # B has its own one. MRO stops directly

