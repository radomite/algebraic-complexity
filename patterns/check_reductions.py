"""Exact finite checks for ordinary copies, matching reductions, and electrical flows."""
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, permutations, product
from math import prod


def ordinary_matching(edges, k):
    by_left = {}
    for (left, right), weight in edges.items():
        by_left.setdefault(left, []).append((right, weight))
    rows = list(by_left.values())

    @cache
    def visit(i, used, needed):
        if needed == 0:
            return 1
        if len(rows) - i < needed:
            return 0
        total = visit(i + 1, used, needed)
        for right, weight in rows[i]:
            bit = 1 << right
            if not (used & bit):
                total += weight * visit(i + 1, used | bit, needed - 1)
        return total

    return visit(0, 0, k)


def split_choices(degree):
    # Triple agreement is scaled by two to keep this check integral.
    if degree == 1:
        return [(1, (0,))]
    if degree == 2:
        return [(1, (0, 1)), (-1, (0, 0))]
    assert degree == 3
    return [(2, (0, 1, 2)), (-1, (0, 0, 1)), (-1, (0, 1, 0)),
            (-1, (0, 1, 1)), (1, (0, 0, 0))]


def check_split(pattern, labels, padding):
    vertices = sorted({v for edge in pattern for v in edge})
    incident = {v: [i for i, e in enumerate(pattern) if v in e] for v in vertices}
    tables = [{(x, y): ((3*x + 5*y + i*x*y + i) % 7) - 3
               for x, y in product(range(labels), repeat=2)} for i in range(len(pattern))]
    target = sum(prod(tables[i][word[u], word[v]] for i, (u, v) in enumerate(pattern))
                 for word in product(range(labels), repeat=len(vertices)))
    scale = 2**sum(len(indices) == 3 for indices in incident.values())
    k = len(pattern) + padding
    result = 0
    for choices in product(*(split_choices(len(incident[v])) for v in vertices)):
        def copy(v, i, x):
            return (3*v + choices[v][1][incident[v].index(i)])*labels + x
        types = [{(copy(u, i, x), copy(v, i, y)): w for (x, y), w in tables[i].items()}
                 for i, (u, v) in enumerate(pattern)]
        for i in range(padding):
            marker = 3*len(vertices)*labels + i
            types.append({(marker, marker): 1})
        for mask in range(1 << k):
            edges = {}
            for i, table in enumerate(types):
                if (mask >> i) & 1:
                    edges.update(table)
            result += prod(c for c, _ in choices)*(-1)**(k-mask.bit_count())*ordinary_matching(edges, k)
    assert result == scale*target
    for prime in (3, 5, 7):
        assert result*pow(scale, -1, prime) % prime == target % prime


def check_orders(n, k):
    def monomial(edges):
        return tuple(sorted(edges))

    edges = list(product(range(n), repeat=2))
    direct = Counter(monomial(m) for m in combinations(edges, k)
                     if len({u for u, _ in m}) == len({v for _, v in m}) == k)
    ordered = Counter(monomial(zip(x, (y[i] for i in pi)))
                      for x in combinations(range(n), k) for y in combinations(range(n), k)
                      for pi in permutations(range(k)))
    assert direct == ordered and all(c == 1 for c in ordered.values())
    return len(direct)


def check_copy_orders():
    checked = 0
    for k in range(1, 5):
        pairs = list(combinations(range(k), 2))
        orders = list(permutations(range(k)))
        for mask in range(1 << len(pairs)):
            edges = {pair for i, pair in enumerate(pairs) if mask & (1 << i)}
            def image(word):
                return tuple(sorted(tuple(sorted((word[u], word[v]))) for u, v in edges))
            automorphisms = [order for order in orders if set(image(order)) == edges]
            representatives = [order for order in orders if order == min(
                tuple(symmetry[v] for v in order) for symmetry in automorphisms)]
            direct = {(tuple(sorted(word)), image(word)) for word in permutations(range(5), k)}
            ordered = Counter()
            for used in combinations(range(5), k):
                for order in representatives:
                    assignment = dict(zip(order, used))
                    ordered[used, image(assignment)] += 1
            assert set(ordered) == direct and all(count == 1 for count in ordered.values())
            checked += 1
    return checked


def check_four_label_tables():
    # A regular tournament orients K5 with two incoming and two outgoing arcs.
    h = 5
    arcs = [(i, (i + step) % h) for i in range(h) for step in (1, 2)]
    incoming = [[j for j, (_, v) in enumerate(arcs) if v == i] for i in range(h)]
    outgoing = [[j for j, (u, _) in enumerate(arcs) if u == i] for i in range(h)]
    states = list(product(range(2), repeat=2))
    for seed in range(3):
        def weight(i, plus, minus):
            index = 8*plus[0] + 4*plus[1] + 2*minus[0] + minus[1]
            return (index**2 + (seed+2)*index + 3*i + 2) % 11 - 5

        wire = 0
        for labels in product(range(2), repeat=len(arcs)):
            wire += prod(weight(i, tuple(labels[j] for j in outgoing[i]),
                                tuple(labels[j] for j in incoming[i])) for i in range(h))
        split = 0
        for plus in product(states, repeat=h):
            term = 1
            for i in range(h):
                local_sum = 0
                for minus in states:
                    if all(minus[slot] == plus[arcs[j][0]][outgoing[arcs[j][0]].index(j)]
                           for slot, j in enumerate(incoming[i])):
                        local_sum += weight(i, plus[i], minus)
                term *= local_sum
            split += term
        assert wire == split


def check_electrical_flows():
    for edges in (list(combinations(range(5), 2)),
                  list(product(range(4), range(4, 8)))):
        h = 1 + max(max(e) for e in edges)
        neighbors = [[v if u == i else u for u, v in edges if i in (u, v)]
                     for i in range(h)]
        # Invert L + J/h by exact elimination.
        rows = [[Fraction(1, h) + 4*(i == j) - (j in neighbors[i]) for j in range(h)]
                + [Fraction(i == j) for j in range(h)] for i in range(h)]
        for j in range(h):
            pivot = rows[j][j]
            rows[j] = [a/pivot for a in rows[j]]
            for i in range(h):
                if i != j:
                    factor = rows[i][j]
                    rows[i] = [a-factor*b for a, b in zip(rows[i], rows[j])]
        inverse = [row[h:] for row in rows]
        for i in range(h):
            for j in range(h):
                divergence = sum(inverse[j][i]-inverse[j][v] for v in neighbors[i])
                assert divergence == (i == j) - Fraction(1, h)

    for radius in range(1, 11):
        value = [Fraction(1, 4*3**t) for t in range(radius+1)]
        norm = sum(2*3**t*x*x for t, x in enumerate(value))
        assert norm == Fraction(3, 16)*(1-Fraction(1, 3**(radius+1)))
        assert 5*value[0] - 3*value[1] == 1
        assert all(4*value[t] == value[t-1]+3*value[t+1] for t in range(1, radius))
        last_error = 4*value[-1] - value[-2]
        residual_norm = 2*3**radius*(last_error**2+3*value[-1]**2)
        assert residual_norm == Fraction(1, 2*3**radius)


if __name__ == "__main__":
    for labels in (2, 3):
        for padding in (0, 1):
            check_split([(0, 2), (0, 3), (0, 4), (1, 2)], labels, padding)
    total = sum(check_orders(n, k) for n in range(1, 6) for k in range(n + 1))
    print("Four signed graph reductions verified over the integers and at primes 3, 5, 7.")
    print(f"Canonical-order coefficients verified for {total:,} matching monomials.")
    print(f"Canonical-order extraction verified for {check_copy_orders()} general patterns.")
    check_four_label_tables()
    check_electrical_flows()
    print("Three oriented K5 table sums, two exact Laplacians, and ten tree truncations verified.")
