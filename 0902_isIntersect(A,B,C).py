import json
def intersect(A, B, C):
    A = json.loads(A)
    B = json.loads(B)
    C = json.loads(C)
    result = []
    for element in A:
        if element in B and element in C:
            result.append(element)
    return True if result != [] else False

print(intersect(input(), input(), input()))
