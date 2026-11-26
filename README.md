# Algebraic complexity

This repository collects results in algebraic complexity found with the help of AI agents. **The notes strive for simplicity but are not polished.** Each paper includes its LaTeX source and a compiled PDF. Lean formalizations are planned as well.

### VP versus VNP from Euclidean flatness

OpenAI’s flatness theorem assigns each binary tensor wire a cost equal to the Euclidean distance between its endpoints. A 5-page argument shows how this geometry implies a lower bound for the clique polynomial. For cliques of size $k$ on $N$ vertices, the circuit-size exponent in $N$ grows as $\Omega(\sqrt{k})$. This implies $\mathrm{VP}\ne\mathrm{VNP}$ over every field. [Paper](vp-vnp/vp-vnp.pdf) · [Source](vp-vnp/vp-vnp.tex)

### Sharp circuit lower bounds in pathwidth

For support graphs of pathwidth $p$, we prove unconditional arithmetic circuit lower bounds matching the dynamic programs. Up to polynomial factors, the sharp base for the permanent is $2$ outside characteristic two, even on subcubic bipartite graphs. For directed Hamiltonian cycles it is $6$ outside characteristic two and $2+2\sqrt{2}$ in characteristic two. For the multivariate Tutte polynomial, the sharp leading exponent is $p\log_2 p$ over every field. [Paper](pathwidth/sharp-pathwidth-bases.pdf) · [Source](pathwidth/sharp-pathwidth-bases.tex)

### Circuit complexity of small colorful patterns

For the triangular prism and $K_{3,3}$, the colorful homomorphism polynomial has circuit lower exponent at least $4/\sqrt{3}$ over every field. In characteristic zero, an ordinary weighted seven-edge path has the same circuit complexity as the colorful four-clique. At eleven edges the lower exponent is already strictly above the matrix multiplication exponent $9/4$. Whether seven edges suffice for this separation remains open. [Paper](small-patterns/small-patterns.pdf) · [Source](small-patterns/small-patterns.tex)
