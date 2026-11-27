# Algebraic complexity

This slop dump collects results in algebraic complexity found with the help of AI agents. Lean formalizations are planned. **The notes are AI-written and barely post-processed. Read at your own risk.** 

## Expositions of known results

### VP versus VNP from Euclidean flatness

OpenAI’s flatness theorem assigns each binary tensor wire a cost equal to the Euclidean distance between its endpoints. A 5-page argument shows how this geometry implies a lower bound for the clique polynomial. For cliques of size $k$ on $N$ vertices, the circuit-size exponent in $N$ grows as $\Omega(\sqrt{k})$. This implies $\mathrm{VP}\ne\mathrm{VNP}$ over every field. This is not a new result, merely a self-contained presentation. [Paper](vp-vnp/vp-vnp.pdf)

### Computing Euclidean tensor prices

A single bit shared among rational sites costs the mean width of their convex hull. Moving one site recovers the number of linear extensions of a poset from two price evaluations. High-precision evaluation is therefore $\#\mathrm P$-hard in growing dimension, and one counting-oracle call suffices. The paper also gives deterministic algorithms in fixed dimension and for explicit tensors on three collinear sites. [Paper](vp-vnp/computing-euclidean-tensor-prices.pdf)

### When does a field have ports?

This exposition gives an introduction to OpenAI’s work on the geometry of the asymptotic spectrum of tensors. Then it studies *ports*: A field has them if bounded-degree graphs can control the average squared wire price between all pairs of attachment sites by the average along their edges, with a constant independent of graph size. The paper develops a finite test using a projective plane, and explains why the field classification matters to get tight circuit lower bounds. [Paper](ports/ports.pdf)

## Sharp bounds under width parameters

We consider the complexity of graph-related polynomials parameterized by pathwidth, cutwidth, and bandwidth.

### Permanents, independent sets, and the Tutte polynomial
For the bipartite permanent outside characteristic two and for generating bipartite independent sets over every field, graphs on $n$ vertices of pathwidth $p$ admit arithmetic circuits of size $n^{O(1)}2^p$. For every fixed $\alpha>3/4$ and $C\ge 0$, each polynomial admits graphs of arbitrarily large pathwidth requiring more than $n^C2^{p-p^\alpha}$ gates. For the chromatic and multivariate Tutte polynomials, the corresponding bound uses the number of partitions of a bag of $p+1$ vertices into at most $r$ blocks for an effective palette of $r\ge 2$ colors. A multivariate Tutte polynomial gives the full Bell number. Our constructions also give size bounds in terms of cutwidth and bandwidth. [Paper](pathwidth/sharp-pathwidth-bases.pdf)

### Hamiltonian cycles

For undirected Hamiltonian cycles, let $\rho$ be the exponential rank growth per path end of the matrix that tests whether two perfect matchings join into one cycle. Over every field, we rule out circuit size $n^{O(1)}B^p$ for every fixed pathwidth base $B<2+\rho$, and likewise every cutwidth base below $1+\rho$. Algorithms attain both bases in characteristics zero, two and three, where $\rho$ equals $4$, $\sqrt{2}$ and $1+2\cos(2\pi/9)$, respectively. In characteristic five we prove $\rho>2.7458$. Its exact value and algorithms attaining the corresponding bases remain open. [Paper](pathwidth/matching-connectivity-width.pdf)

## Small patterns

### Fixed-pattern catalogue 

Over every field, the unrestricted circuit exponent for the colorful four-clique lies between $9/4$ and $25/8$. For the colorful five-clique the bounds are $9/4$ and $4-1/300$. For $K_{3,3}$, the colorful homomorphism polynomial has circuit lower exponent at least $4/\sqrt{3}$ over every field. In characteristic zero, an ordinary weighted seven-edge path has the same circuit complexity as the colorful four-clique. At eleven edges the lower exponent is already strictly above the matrix multiplication exponent $9/4$. This is pretty open-ended. [Paper](patterns/small-patterns.pdf)

### Parameterized sparse patterns

For the ordinary weighted count of a fixed $k$-vertex pattern on an $n$-vertex host, explicit bounded-degree expanders have circuit-size exponent at least $(1/\sqrt{2}-\varepsilon)\sqrt{k}$ over every field. For a matching of $m$ edges the lower exponent is $(1/3-o(1))\sqrt{m}$ in characteristic zero and every odd characteristic. The grid contraction from the counting-ETH refutation gives an upper exponent of $O(k/\sqrt{\log k})$ for every pattern with $O(k)$ edges. [Paper](patterns/sparse-patterns.pdf)
