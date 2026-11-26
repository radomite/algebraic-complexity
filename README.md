# Algebraic complexity

This repository collects results in algebraic complexity found with the help of AI agents. **The notes strive for simplicity but are not polished.** Each paper includes its LaTeX source and a compiled PDF. Lean formalizations are planned as well.

### VP versus VNP from Euclidean flatness

OpenAI’s flatness theorem assigns each binary tensor wire a cost equal to the Euclidean distance between its endpoints. This simple 5-page paper shows how this geometry implies a lower bound for the clique polynomial. For cliques of size $k$ on $N$ vertices, the circuit-size exponent in $N$ grows as $\Omega(\sqrt{k})$, which implies $\mathrm{VP}\ne\mathrm{VNP}$ over every field. This is not a new result, merely a self-contained presentation of a part of the OpenAI $\mathrm{VP}\ne\mathrm{VNP}$ result. [Paper](vp-vnp/vp-vnp.pdf) · [Source](vp-vnp/vp-vnp.tex)

### Sharp circuit lower bounds in pathwidth

The perfect-matching polynomial of a graph of size $n$ and pathwidth $p$ has an arithmetic circuit of size $n^{O(1)}2^p$. In characteristic zero, we prove that replacing $2^p$ by $2^{p-p^\alpha}$ fails for every fixed $\alpha>3/4$, even on bipartite graphs of maximum degree three. We also rule out dividing the $6^p$ factor for directed and undirected Hamiltonian cycles by $2^{p^\alpha}$. For the chromatic and multivariate Tutte polynomials, the same lower bound applies to the number of partitions of $p+1$ vertices into at most $r$ classes for $r\ge 2$ colors, or into any number of classes when the color parameter is indeterminate. [Paper](pathwidth/sharp-pathwidth-bases.pdf) · [Source](pathwidth/sharp-pathwidth-bases.tex)

### Circuit complexity of small colorful patterns

For the triangular prism and $K_{3,3}$, the colorful homomorphism polynomial has circuit lower exponent at least $4/\sqrt{3}$ over every field. In characteristic zero, an ordinary weighted seven-edge path has the same circuit complexity as the colorful four-clique. At eleven edges the lower exponent is already strictly above the matrix multiplication exponent $9/4$. Whether seven edges suffice for this separation remains open. [Paper](small-patterns/small-patterns.pdf) · [Source](small-patterns/small-patterns.tex)
