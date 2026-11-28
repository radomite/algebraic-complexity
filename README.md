Since the recent VP versus VNP breakthrough, I've been very curious to understand the results and techniques that have suddenly become available. I've created this repository to collect AI-generated answers to questions I care about and am sharing those explorations so that whatever comes to light doesn’t stay buried in a private conversation with ChatGPT. This is the only purpose. The notes are not research papers and I do not claim authorship or priority for the ideas in them. Once the dust settles, I or others might use these notes to write traditional papers.

While I have asked the questions and tried to ensure a minimum of output quality, some arguments may be wrong (but Lean formalizations are planned) and the notes may blatantly miss or misattribute earlier work. If you recognize an issue, please report it via a GitHub issue or send me a mail, and I will correct it as soon as possible. I am also happy about suggestions what to look into, pull requests on GitHub, and collaborators.

## Tensor prices

### VP versus VNP from Euclidean flatness

OpenAI’s flatness theorem assigns each binary tensor wire a cost equal to the Euclidean distance between its endpoints. A 5-page argument shows how this geometry implies a lower bound for the clique polynomial. For cliques of size $k$ on $N$ vertices, the circuit-size exponent in $N$ grows as $\Omega(\sqrt{k})$. This implies $\mathrm{VP}\ne\mathrm{VNP}$ over every field. This is not a new result, merely a self-contained presentation. [Elementary version](vp-vnp/vp-vnp.pdf)

An additional companion paper uses the same import and obtains the same result, but in GCT language, by constructing a polynomial equation that separates the clique tensor from an orbit closure containing all the balanced decompositions of a small circuit. [GCT version](vp-vnp/vp-vnp-gct.pdf)

### When does a field have ports?

This exposition gives an introduction to OpenAI’s work on the geometry of the asymptotic spectrum of tensors. Then it studies *ports*: A field has them if bounded-degree graphs can control the average squared wire price between all pairs of attachment sites by the average along their edges, with a constant independent of graph size. The paper develops a finite test using a projective plane, and explains why the field classification matters to get tight circuit lower bounds. [Paper](ports/ports.pdf)

### Computing Euclidean tensor prices

A single bit shared among rational sites costs the mean width of their convex hull. Moving one site recovers the number of linear extensions of a poset from two price evaluations. High-precision evaluation is therefore #P-hard in growing dimension, and one counting-oracle call suffices. The paper also gives deterministic algorithms in fixed dimension and for explicit tensors on three collinear sites. [Paper](vp-vnp/computing-euclidean-tensor-prices.pdf)

## Sharp bounds under width parameters

We consider the complexity of graph-related polynomials parameterized by pathwidth, cutwidth, and bandwidth.

### Permanents, independent sets, and the Tutte polynomial
For the bipartite permanent outside characteristic two and for generating bipartite independent sets over every field, graphs on $n$ vertices of pathwidth $p$ admit arithmetic circuits of size $n^{O(1)}2^p$. For every fixed $\alpha>3/4$ and $C\ge 0$, each polynomial admits graphs of arbitrarily large pathwidth requiring more than $n^C2^{p-p^\alpha}$ gates. For the chromatic and multivariate Tutte polynomials, the corresponding bound uses the number of partitions of a bag of $p+1$ vertices into at most $r$ blocks for an effective palette of $r\ge 2$ colors. A multivariate Tutte polynomial gives the full Bell number. Our constructions also give size bounds in terms of cutwidth and bandwidth. [Paper](pathwidth/sharp-pathwidth-bases.pdf)

### Hamiltonian cycles

For undirected Hamiltonian cycles, let $\rho$ be the exponential rank growth per path end of the matrix that tests whether two perfect matchings join into one cycle. [Curticapean, Lindzey and Nederlof](https://arxiv.org/abs/1709.02311) established the pathwidth lower base $2+\rho$ for counting under SETH. Over every field, we rule out circuit size $n^{O(1)}B^p$ for every fixed pathwidth base $B<2+\rho$, and likewise every cutwidth base below $1+\rho$. Algorithms attain both bases in characteristics zero, two and three, where $\rho$ equals $4$, $\sqrt{2}$ and $1+2\cos(2\pi/9)$, respectively. In characteristic five we prove $\rho>2.7458$. Its exact value and algorithms attaining the corresponding bases remain open. [Paper](pathwidth/matching-connectivity-width.pdf)

A [companion note](pathwidth/sharper-additive-bound.md) proves the sharper additive bounds for both papers.

## Small patterns

### Fixed-pattern catalogue

Over every field, the unrestricted circuit exponent for the colorful four-clique lies between $9/4$ and $25/8$. For the colorful five-clique it is between $9/4$ and $3.992353870$. For $K_{3,3}$, the colorful homomorphism polynomial has circuit lower exponent at least $4/\sqrt{3}$ over every field. Many other bounds are shown as well. [Paper](patterns/small-patterns.pdf)

### Parameterized sparse patterns

For the ordinary weighted count of a fixed $k$-vertex pattern on an $n$-vertex host, explicit bounded-degree expanders have circuit-size exponent at least $(1/\sqrt{2}-\varepsilon)\sqrt{k}$ over every field. For a matching of $m$ edges the lower exponent is $(1/3-o(1))\sqrt{m}$ in characteristic zero and every odd characteristic. On bipartite hosts the same coefficient holds for weighted sums of matching polynomials whose highest order $m$ tends to infinity with $m\sqrt{\log(2m)}=o(\log n)$, where $n$ is the number of vertices per shore. The grid contraction from the counting-ETH refutation gives an upper exponent of $O(k/\sqrt{\log k})$ for every pattern with $O(k)$ edges. [Paper](patterns/sparse-patterns.pdf)
