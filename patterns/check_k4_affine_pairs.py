"""Balanced mixed terms in codimension-one affine decompositions of binary K4."""
from functools import lru_cache
from itertools import combinations, permutations

EDGES = tuple(combinations(range(4), 2))
PRICES = set(permutations((15, 10, 10))) | set(permutations((16, 16, 0)))
DENSE = tuple((1 << (1 << u)) | (1 << (1 << v)) for u,v in EDGES)


@lru_cache(None)
def span(mask):
    vectors = {0}
    for v in range(1, 16):
        if mask & (1 << v):
            vectors |= {x ^ v for x in vectors}
    return sum(1 << v for v in vectors)


def dimension(space):
    return space.bit_count().bit_length() - 1


def joins():
    for group in range(1, 32):  # last edge is the root
        left = (group-1) & group
        while left:
            right = left ^ group
            if left < right:
                yield group,left,right,63 ^ group
            left = (left-1) & group


CUTS = tuple(joins())


def geometry(scopes):
    spaces = [1]*64
    for group in range(1,64):
        bit = group & -group
        spaces[group] = span(spaces[group ^ bit] | scopes[bit.bit_length()-1])
    assert dimension(spaces[63]) == 4
    result = []
    for _,left,right,outside in CUTS:
        a,b,c = (spaces[j] for j in (left,right,outside))
        shared = dimension(a & b & c)
        wires = tuple(dimension(pair)-shared for pair in (a&b,a&c,b&c))
        parity = sum(map(dimension,(a,b,c))) - 4 - 2*shared - sum(wires)
        assert parity >= 0
        result.append((shared,wires,parity))
    return result


def branch_scopes(equation, representative, side):
    # Eliminate a pivot using the hyperplane equation. The freed coordinate
    # is the selector between its two affine cosets.
    pivot = equation & -equation
    result = []
    for i,j in EDGES:
        mask = 0
        for vertex,other in ((i,j),(j,i)):
            slot = other - int(other > vertex)
            form = equation ^ pivot if 1 << vertex == pivot else 1 << vertex
            flip = slot > 0 and bool(representative & (1 << (2*vertex+slot-1)))
            if flip ^ (1 << vertex == pivot and side):
                form ^= pivot
            mask |= 1 << form
        result.append(mask)
    return tuple(result)


def lower(shape, weights):
    shared,wires,parity = shape
    return 16*shared + sum(a*b for a,b in zip(wires,weights)) + parity*max(weights)


def check():
    original = geometry(DENSE)
    # Quantifier order matters: keep the same cut AND price for all
    # labelled exchanges, including vertex permutations between digits.
    valid = [{w for w in PRICES if lower(cut,w) >= 50} for cut in original]
    for equation in range(1,16):
        for representative in range(1,256):
            first,second = (geometry(branch_scopes(equation,representative,side)) for side in (0,1))
            for i, choices in enumerate(valid):
                choices.difference_update([w for w in choices
                                           if lower(first[i],w)+lower(second[i],w) < 70])
    feasible = [i.bit_count() == 1 for i in range(32)]
    for i,(group,left,right,_) in enumerate(CUTS):
        if feasible[left] and feasible[right] and not valid[i]:
            feasible[group] = True
    assert not feasible[31]
    print(f"All 3,825 labelled pairs: {sum(map(bool,valid))} of {len(CUTS)} cuts have a uniform witness.")
    print("Every tree meets one; balanced mixed join price is at least 25/8 - 15r/16.")


if __name__ == "__main__":
    check()
