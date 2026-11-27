"""Check the two five-clique contractions on arbitrary signed edge weights."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb
from random import Random


def maps_and_tables(q, digits, seed):
    words = list(product(range(q), repeat=digits))
    random = Random(seed)
    edges = list(combinations(range(5), 2))
    tables = {
        edge: {(a, b): random.randrange(-3, 4) for a in words for b in words}
        for edge in edges
    }
    return words, tables


def swapped_sums(words, tables):
    digits = len(words[0])
    ab, ac, ad, ae, bc, bd, be, cd, ce, de = tables.values()
    totals = [0] * (1 << digits)
    for a, b in product(words, repeat=2):
        for swapped in range(1 << digits):
            ap = tuple((b if swapped >> i & 1 else a)[i] for i in range(digits))
            bp = tuple((a if swapped >> i & 1 else b)[i] for i in range(digits))
            for e in words:
                total = sum(ad[ap, d] * bd[b, d] * de[d, e]
                            * sum(ac[a, c] * bc[bp, c] * cd[c, d] * ce[c, e]
                                  for c in words) for d in words)
                totals[swapped] += ab[a, b] * ae[ap, e] * be[bp, e] * total
    return totals


def orientations(pairs):
    for bits in product(range(2), repeat=len(pairs)):
        yield [(pair[bit], pair[1-bit]) for pair, bit in zip(pairs, bits)], (-1)**sum(bits)


def factored_sum(words, tables, swapped, active, q):
    ab, ac, ad, ae, bc, bd, be, cd, ce, de = tables.values()
    digits = len(words[0])
    correct = [i for i in range(digits) if (active & ~swapped) >> i & 1]
    kept = [i for i in range(digits) if i not in correct]

    def label(initial, orientation, side):
        label = [None] * digits
        for i, symbol in zip(kept, initial):
            label[i] = symbol
        for i, pair in zip(correct, orientation):
            label[i] = pair[side]
        return tuple(label)

    total = 0
    for pairs in product(combinations(range(q), 2), repeat=len(correct)):
        for A, B in product(product(range(q), repeat=len(kept)), repeat=2):
            left_a = tuple(b if swapped >> i & 1 else a for i, a, b in zip(kept, A, B))
            left_b = tuple(a if swapped >> i & 1 else b for i, a, b in zip(kept, A, B))
            lwords = [(label(left_a, o, 0), label(left_b, o, 1), s)
                      for o, s in orientations(pairs)]
            rwords = [(label(A, o, 0), label(B, o, 1), s) for o, s in orientations(pairs)]
            for c, d in product(words, repeat=2):
                left = cd[c, d] * sum(s * ab[a, b] * ac[a, c] * bd[b, d] for a, b, s in lwords)
                for ap, bp, sign in rwords:
                    total += left * sign * ad[ap, d] * bc[bp, c] * sum(
                        ae[ap, e] * be[bp, e] * ce[c, e] * de[d, e] for e in words)
    return total


def best_dense_tree(k):
    """Exact subset DP with one edge leaf fixed as the root."""
    edges = list(combinations(range(k), 2))
    all_edges = (1 << len(edges)) - 1
    incident = [sum(1 << i for i, edge in enumerate(edges) if v in edge) for v in range(k)]

    @lru_cache(None)
    def exponent(shared, x, y, z):
        x, y, z = sorted((x, y, z), reverse=True)
        if z == 0:
            return shared + x + y
        correction = max(0, (x + y)*z - x*y)
        return shared + x + y + Fraction(correction**2, 4*x*y*z)

    @lru_cache(None)
    def best(group):
        if group.bit_count() == 1:
            return 2
        outside = all_edges ^ group
        answer = k
        left = (group - 1) & group
        while left:
            right = group ^ left
            if left < right:
                types = [(bool(row & left), bool(row & right), bool(row & outside))
                         for row in incident]
                charge = exponent(*(types.count(t) for t in
                                    [(1, 1, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]))
                answer = min(answer, max(charge, best(left), best(right)))
            left = (left - 1) & group
        return answer

    return best(all_edges ^ 1)


def threshold_weight(size, threshold):
    if size < threshold:
        return 0
    return (-1)**(size-threshold) * comb(size-1, threshold-1)


def check_operator_coefficients():
    """Check every monomial after substituting K = I - P."""
    for digits in range(1, 13):
        for threshold in range(1, digits+1):
            complementary = digits - threshold + 1
            for size in range(digits+1):
                direct = threshold_weight(size, threshold)
                factored = sum(comb(digits-size, h-size) * threshold_weight(h, complementary)
                               for h in range(size, digits+1))
                assert direct + (-1)**size * factored == int(size == 0)


def check():
    subsets = 0
    thresholds = 0
    check_operator_coefficients()
    for q, digits in ((2, 3), (3, 2)):
        words, tables = maps_and_tables(q, digits, seed=q)
        direct = swapped_sums(words, tables)
        brute = 0
        for labels in product(words, repeat=5):
            weight = 1
            for (i, j), table in tables.items():
                weight *= table[labels[i], labels[j]]
            brute += weight
        assert brute == direct[0]
        corrections = {}
        for active in range(1 << digits):
            recovered = 0
            for swapped in range(1 << digits):
                if swapped & ~active:
                    continue
                signed = sum((-1)**t.bit_count() * direct[swapped | t]
                             for t in range(1 << digits) if not t & ~(active & ~swapped))
                assert signed == factored_sum(words, tables, swapped, active, q)
                if swapped == 0:
                    corrections[active] = signed
                recovered += signed
                subsets += 1
            assert recovered == brute
            for threshold in range(1, active.bit_count()+1):
                complementary = active.bit_count() - threshold + 1
                value = sum(threshold_weight(s.bit_count(), threshold) * direct[s]
                            + threshold_weight(s.bit_count(), complementary) * corrections[s]
                            for s in range(active+1) if not s & ~active)
                assert value == brute
                thresholds += 1
    for k, shape, dual, expected in [
            (4, (2, 1, 1), (Fraction(15, 16), Fraction(5, 8), Fraction(5, 8)), Fraction(25, 8)),
            (5, (2, 2, 1), (1, 1, 0), 4)]:
        assert best_dense_tree(k) == sum(x*y for x, y in zip(shape, dual)) == expected
    assert 12**600 < 2**249 * 11**550
    assert 11**2 < 128
    assert Fraction(comb(128, 2), 128**2) == Fraction(127, 256)
    r, y = Fraction(1, 84), Fraction(11, 84)
    entropy_bound = Fraction(83, 9800)
    direct_excess = entropy_bound - r + r**2 / (8*(2-r))
    factored_excess = (entropy_bound - y*Fraction(129, 896)
                       + 81*y**2 / (196*(1+y/7)))
    assert max(direct_excess, factored_excess) < Fraction(-1, 300)
    print(f"Both evaluations agree for {subsets} active-set and swap-set pairs.")
    print(f"The collected sums agree for {thresholds} active-set and threshold pairs.")
    print("Every operator coefficient agrees through twelve digits.")
    print("Optimal dense trees and the two balanced-cut dual prices agree.")
    print("Both rational exponent bounds are strictly below 4 - 1/300.")


if __name__ == "__main__":
    check()
