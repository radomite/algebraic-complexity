"""Exact costs for the block threshold and a two-label K4 obstruction."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
import math
from math import comb

def _ln_unit(value):
    """Enclose ln(value), 1 <= value <= 2, by the positive atanh series."""
    z = (value - 1) / (value + 1)
    square = z * z
    term = z
    total = F(0)
    for odd in range(1, 38, 2):
        total += term / odd
        term *= square
    return 2 * total, 2 * (total + term / (39 * (1 - square)))

_LN2_LOW, _LN2_HIGH = _ln_unit(F(2))

@lru_cache(maxsize=4096)
def log2_bounds(value):
    """Outward dyadic bounds, using integer and rational arithmetic only."""
    value = F(value)
    if value < 1:
        raise ValueError("logarithm argument must be at least one")
    e = value.numerator.bit_length() - value.denominator.bit_length()
    if value < 1 << e:
        e -= 1
    unit = value / (1 << e)
    if unit == 1:
        return F(e), F(e)
    lo, hi = _ln_unit(unit)
    scale = 1 << 48
    return (e + F(math.floor(scale * lo / _LN2_HIGH), scale),
            e + F(math.ceil(scale * hi / _LN2_LOW), scale))

def split_representatives():
    # Each split vertex uses both copies. Relabel a/b or c/d, or exchange
    # primed and unprimed globally (which just renames the swap symbols).
    representatives = set()
    for masks in product(range(1, 7), repeat=2):
        orbit = []
        reflected = tuple((m & 1) | ((m & 2) << 1) | ((m & 4) >> 1) for m in masks)
        for pair in (masks, reflected):
            for flip in (0, 7):
                a, b = (m ^ flip for m in pair)
                orbit.extend(((a, b), (b, a)))
        representatives.add(min(orbit))
    return sorted(representatives)

def scopes(k, split, branch):
    result = []
    for edge in combinations(range(k), 2):
        mask = sum(1 << v for v in edge)
        for v, other in (edge, edge[::-1]):
            if v < len(split):
                slot = other - int(other > v)
                primed = (split[v] >> slot) & 1
                digit = primed if branch == "joint" else v ^ primed
                mask |= 1 << (k + digit)
        result.append(mask)
    return result

def join_axes(left, right, outside):
    return (left & right & outside, left & right & ~outside,
            left & outside & ~right, right & outside & ~left)

def axis_counts(k, split_size, mask):
    original = (1 << k) - 1
    residual = (1 << split_size) - 1
    return (mask & original & ~residual).bit_count(), (mask & residual).bit_count(), (mask >> k).bit_count()

def tree_cuts(k, split, branch, tree):
    """Validate an explicit tree independently of the search DP."""
    leaves = scopes(k, split, branch)
    cuts = []

    def walk(node):
        if type(node) is int and 0 <= node < len(leaves) - 1:
            return {node}, leaves[node]
        if not isinstance(node, list) or len(node) != 2:
            raise ValueError("invalid contraction tree node")
        a, left = walk(node[0])
        b, right = walk(node[1])
        if a & b:
            raise ValueError("duplicate edge in contraction tree")
        group = a | b
        outside = 0
        for i, leaf in enumerate(leaves):
            if i not in group:
                outside |= leaf
        cuts.append([axis_counts(k, len(split), mask) for mask in join_axes(left, right, outside)])
        return group, left | right

    used, _ = walk(tree)
    if used != set(range(len(leaves) - 1)):
        raise ValueError("tree does not cover all non-root edges")
    return cuts


@lru_cache(None)
def trees(leaves):
    if len(leaves) == 1:
        return (leaves[0],)
    result = []
    for mask in range(1, 1 << len(leaves), 2):
        left = tuple(v for i, v in enumerate(leaves) if mask >> i & 1)
        right = tuple(v for v in leaves if v not in left)
        if right:
            result.extend([a, b] for a in trees(left) for b in trees(right))
    return tuple(result)


def lines(cuts):
    # Scale both coordinates by 16. Rectangular duals are tangent at
    # (2,1,1) and the three input/output size bounds, plus permutations.
    out = {(32, 0)}
    prices = set(permutations((15, 10, 10))) | set(permutations((16, 16, 0)))
    for cut in cuts:
        for price in prices:
            base = slope = 0
            for w, (plain, residual, symbols) in zip((16, *price), cut):
                base += w*(plain + residual)
                slope += w*(symbols - residual)
            out.add((base, slope))
    return out


def dominates(forms, loss):
    # Find the minimum of the convex piecewise linear envelope minus
    # 25/8-loss*r by ruling out a common strict violation on [0,1].
    lo, hi = F(0), F(1)
    for b, m in forms:
        a = m + 16*loss
        if a == 0:
            if b >= 50:
                return True
        elif a > 0:
            hi = min(hi, F(50-b, a))
        else:
            lo = max(lo, F(50-b, a))
    return lo >= hi


def joint_dominates(cuts, gain):
    """Test T >= 25/8 - 2r + gain*z on the triangle 0 <= z <= r <= 1."""
    # Each of these triples represents a price minus the target, times 16.
    forms = {(-18, 32, -16*gain)}
    prices = set(permutations((15, 10, 10))) | set(permutations((16, 16, 0)))
    for cut in cuts:
        for weights in prices:
            a, b, c = -50, 32, -16*gain
            for w, (plain, residual, symbols) in zip((16, *weights), cut):
                a += w*(plain+residual)
                b -= w*residual
                c += w*symbols
            forms.add((a,b,c))
    polygon = [(F(0),F(0)), (F(1),F(0)), (F(1),F(1))]
    for a,b,c in sorted(forms, reverse=True):
        if (a,b,c) == (0,0,0):
            return True
        clipped = []
        for (x,y),(v,w) in zip(polygon,polygon[1:]+polygon[:1]):
            left, right = a+b*x+c*y, a+b*v+c*w
            if left <= 0:
                clipped.append((x,y))
            if (left < 0 < right) or (right < 0 < left):
                t = left/(left-right)
                clipped.append((x+t*(v-x),y+t*(w-y)))
        polygon = clipped
        if not polygon:
            return True
    return sum(x*w-y*v for (x,y),(v,w) in zip(polygon,polygon[1:]+polygon[:1])) == 0


def k4_barrier():
    assert len(split_representatives()) == 8
    shapes = trees(tuple(range(5)))
    assert len(shapes) == 105
    for split in split_representatives():
        p = [lines(tree_cuts(4, split, 'swap', t)) for t in shapes]
        k = [tree_cuts(4, split, 'joint', t) for t in shapes]
        if all(dominates(f,0) for f in p):
            case = 'swap'
        elif all(joint_dominates(f,2) for f in k):
            case = 'joint'
        elif all(dominates(f,1) for f in p) and all(joint_dominates(f,1) for f in k):
            case = 'cover'
        else:
            case = 'unresolved'
        print(split,case)
        assert case != 'unresolved'


def chord_weight(q, slope):
    """A dyadic upper bound on q**slope, certified with rational logarithms."""
    lo, hi = 0, 2**20
    while hi-lo > 1:
        mid = (lo+hi)//2
        if log2_bounds(F(2**20, mid))[1] <= -slope*log2_bounds(q)[0]:
            hi = mid
        else:
            lo = mid
    return F(hi, 2**20)


def k5_certificate():
    q, b, alpha, t = 39, 7, F(39849,100000), F(68504,100000)
    log_lo, log_hi = log2_bounds(q)
    u_lo, u_hi = 1/log_hi, 1/log_lo
    def swap(r):
        return -r + r*r/(8*(2-r))
    def joint(y):
        return (-y*log2_bounds(F(2*q,q-1))[0]*u_lo
                + ((1+2*u_hi)*y)**2/(4*(1+y*u_lo)))
    def full_interval(start, cost):
        results = []
        for i in range(512):
            lo = start + (1-start)*i/512
            hi = start + (1-start)*(i+1)/512
            hit = log2_bounds(1/lo)[1]
            miss = log2_bounds(1/(1-lo))[1]
            for p in (lo,hi):
                results.append(cost(p) + alpha*u_hi/b*(p*hit+(1-p)*miss))
        return max(results)
    charges = []
    for i in range(8):
        l, h = alpha*i/8, alpha*(i+1)/8
        slope = (swap(h)-swap(l))/(h-l)
        intercept = swap(l)-slope*l
        weight = (1+chord_weight(q,slope))**b-1
        assert 0 < weight < 1
        rate = -log2_bounds(1/weight)[0]*u_lo
        charges.append(full_interval(t, lambda p: intercept+alpha*p*rate/b))
    k = full_interval(1-t, lambda p: joint(alpha*p))
    return max(charges), k


def check_identity():
    # Test the two levels of multilinear expansion on the Boolean cube.
    # Multilinearity lifts equality of the integer evaluations to coefficients.
    from itertools import product, combinations
    from math import prod
    for bits in product((0,1), repeat=6):
        groups = [bits[i:i+2] for i in (0,2,4)]
        swaps = [sum((-1)**(h-1)*sum(prod(s) for s in combinations(g,h))
                     for h in (1,2)) for g in groups]
        joint = [prod(1-x for x in g) for g in groups]
        for threshold in (1,2,3):
            total = 0
            for start, weights in ((threshold,swaps),(4-threshold,joint)):
                for j in range(start,4):
                    total += (-1)**(j-start)*comb(j-1,start-1)*sum(
                        prod(s) for s in combinations(weights,j))
            assert total == 1


if __name__ == '__main__':
    check_identity()
    k4_barrier()
    direct, joint = k5_certificate()
    for name, value in [('swap',direct),('joint',joint)]:
        print(name, float(4+value), flush=True)
    assert 4+direct < F("3.992353409")
    assert 4+joint < F("3.992353870") < 4-F(1,131)
