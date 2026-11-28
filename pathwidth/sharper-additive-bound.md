# The sharper additive width bound

The rectangular source proves $2^{p-o(p)}$ for bipartite perfect matchings and independent sets. Its explicit error is $O(p^{6/7}(\log(2+p))^{1/14})$. To reduce that error, this note changes the wire capacities during a sweep and charges a circuit cut according to how often it changes parts along the sweep. The same source gives the sharper losses for Hamiltonian cycles. The two papers give the graph constructions, field-specific ranks and upper circuits. [Sharp Width Bounds for Counting Polynomials](sharp-pathwidth-bases.pdf) · [Complexity of Hamiltonian Cycles via Connectivity Rank](matching-connectivity-width.pdf)

## The additive theorem

Write $p$ for minimum pathwidth, $n$ for the number of vertices, $m$ for the number of edges (arcs in a directed graph), $\|G\|=n+m$ for total graph size, and $s$ for the size of an unrestricted binary arithmetic circuit over the indicated field. Set $E(x)=x^{3/4}(\log_2(2+x))^{3/8}$. Each row has graphs with $p\to\infty$ such that

$$
\log_2 s\ge L-O(E(L)),\qquad \log_2 \|G\|=O(E(L)).
$$

| Polynomial | Field or effective palette | Reference exponent $L$ |
|---|---|---|
| Perfect matching on subcubic bipartite graphs | Characteristic other than two | $p$ |
| Independent sets on bipartite graphs | Every field | $p$ |
| Chromatic edge indicators and multivariate Tutte | Every field, $2\le r\le\infty$ | $\log_2 B_r(p+1)$ |
| Directed Hamiltonian cycle | Characteristic other than two | $p\log_2 6$ |
| Directed Hamiltonian cycle | Characteristic two | $p\log_2(2+2\sqrt2)$ |
| Undirected Hamiltonian cycle | Characteristic zero | $p\log_2 6$ |
| Undirected Hamiltonian cycle | Characteristic two | $p\log_2(2+\sqrt2)$ |
| Undirected Hamiltonian cycle | Characteristic three | $p\log_2(3+2\cos(2\pi/9))$ |

Each row admits an upper circuit of size $\|G\|^{O(1)}2^L$. Here $B_r(k)$ counts partitions of $k$ sites into at most $r$ classes. For a scalar integer palette $q$, take $r=q$ in characteristic zero and its least nonnegative residue in positive characteristic. Take $r=\infty$ for a free cluster parameter and $B_\infty(k)=\operatorname{Bell}(k)$. The constants for the partition polynomials are uniform in $r$. For any fixed $C$, these witnesses exclude size $\|G\|^C2^{L-g}$ when $g$ exceeds a sufficiently large constant multiple of $E(L)$. The graph specializations use the border-size conventions and degree extraction of the papers. [Circuit models and rectangle](sharp-pathwidth-bases.pdf#nameddest=section.2) · [Tour pathwidth bases](matching-connectivity-width.pdf#nameddest=theorem.1.3)

For the first three rows the same estimates hold simultaneously at minimum cutwidth and bandwidth on subcubic witnesses, by the layer construction in the pathwidth paper. The [Hamiltonian-cycle transfer](#hamiltonian-cycles) below gives the three cutwidth conventions for tours. [Layout transfer for the first three rows](sharp-pathwidth-bases.pdf#nameddest=appendix.B)

For the ordered source $H$, edge $e$ has a label of $c_e$ bits, and each vertex $v$ has a variable $X_{v,\alpha}$ for each joint label on its incident edges. The polynomial $F_H$ sums the product of the addressed variables over all edge labelings. One may instead label the half-edges separately and multiply each term by the product of the boundary-matrix entries. Each edge matrix must be nonsingular of order $2^{c_e}$. The price argument below covers both polynomials.

## An ordered source for the sharper estimate

**Ordered source.** There are ordered table graphs as defined above, over every field, with parameters $w=4^h$, $t=\lceil w^3(\log_2(2w))^{3/2}\rceil$, and $D=wt$, for which

$$
 A\le D+O(t),\qquad T=O(t),\qquad
 \log_2(\mathsf{size}(F_H)+1)\ge D-O(t).
$$

Here $A$ is the largest total capacity across a prefix and $T$ the largest incident capacity of any table. There are $O(w^2)$ tables of at most six ports and at most $w+1$ wires across each prefix. The size may be degree-component border size. In particular $t=\Theta(E(D))$.

## Keeping the total number of crossing bits small

Use $w$ parallel lanes. Each round injects a mark into each lane and ends with all lanes carrying the same vector. A switch takes two lanes in and returns two lanes. Its table in $F_H$ has arbitrary entries. The vectors below prescribe only the capacities and endpoints for the proof.

Process a dyadic interval of $s$ lanes by processing its left half, then its right half, then merging the results. A singleton injects one marked basis vector. At the end of an interval distribute its accumulated increment equally over $r_s=2^{\lceil(\log_2 s)/2\rceil}$ of its lanes. To merge, pair the $r_{s/2}$ carrying lanes on either side. At each such switch divide the two increments' sum equally between the outputs if $r_s=2r_{s/2}$, and send the sum to one output otherwise. Always retain the round's common starting vector on both outputs. After the entire interval is processed, repeatedly pair a carrying lane with an empty one to broadcast the final increment equally to all $w$ lanes. The number of switches per round is $O(w)$, since the number of merge switches of order $s$ is $(w/s)r_{s/2}$, and the broadcast takes fewer than $w$ further switches.

Give each mark in one round squared weight $\rho$. Choose the weights symmetrically around the middle, using the following prescription on each half. Let $v=\sqrt w$, $\kappa=2^{-8}$, and let $z\in[0,w]$ measure the sum of round weights from the middle outwards. On $[0,v]$ take $\rho=\kappa/v$. On each $[2^jv,2^{j+1}v]$, $0\le j<h$, take $\rho=\min(1,\kappa4^j/v)$. Each interval contains an integral number of rounds. The first interval takes $w/\kappa$ rounds, and the others together take at most $\sum_{j<h}(2^jv+(w/\kappa)2^{-j})$, giving $O(w)$ rounds per half. Write $k=O(w^2)$ for the number of all tables.

In a space with one coordinate per mark put $d_i=\sqrt{\rho_i}$, $S=\|d\|^2=2w^2$, and let $\Pi$ be orthogonal projection off $d$. Inject $\Pi(d_i e_i)$ at mark $i$. The currents $f_e$ so defined are conserved at the switches, and the lanes start and finish at zero. If the injected prefix has squared mass $x$, the current mean on the $w$ lanes is $\bar f=\Pi(d\,\mathbf{1}_{\mathrm{prefix}})/w$.

To estimate variation from the mean, first remove the common vector at the start of the round and divide increments by $\sqrt{\rho}$, before projection. A completed interval of size $s$ now contributes $s/r_s\le\sqrt s$ to the sum of squared norms. In a partial merge bound the two old contributions and the new one by $2\sqrt{s/2}+\sqrt s$. The other completed siblings on the recursion stack, at most one of each dyadic size, contribute a geometric series. Broadcasting can only decrease the sum. Hence this sum is at most $10\sqrt w$, and every single increment has norm at most one. Projection contracts norms and the mean minimizes total squared deviations. It follows that at every prefix

$$
 \sum_e\|f_e\|^2\le w\|\bar f\|^2+10v\rho
 =\frac{S}{4w}-\frac{(x-S/2)^2}{wS}+10v\rho .
$$

In the central interval the last term is $10\kappa$. In interval $j$ the absolute deviation is at least $w\,2^jv$, so the subtracted term is at least $4^j/2$, while $10v\rho\le10\kappa4^j$. In all cases the bound is $S/(4w)+10\kappa$. Each individual current has norm at most $\sqrt{S}/(2w)+1<2$.

Set $\lambda=2D/\sqrt S$ and give wire $e$ capacity $c_e=\lceil\lambda\|f_e\|\rceil$, omitting zero-capacity wires. A cut has at most one wire per lane and, by Cauchy--Schwarz, at most

$$
        w+\lambda\sqrt{S/4+10\kappa w}=D+O(t)
$$

crossing bits. Each incident capacity is $O(t)$. Finally join every consecutive pair of tables by one additional, independent $t$-bit wire. This costs at most $t$ at each cut. Summing over wires gives total capacity $B=O(w^2t)$.

## Charging the changes of part in a circuit product

Complete $\lambda f_e/c_e$ to a unit vector and place the original wire ends at its signed halves as in the rectangle proof. For the additional wires use signed halves of fresh orthonormal vectors, one per wire. The output sites $P$ have Gaussian width $W=O(\sqrt{\log(2w)})$ by the Gaussian maximum bound. The target coefficient tensor has price $B$. This also holds when each edge carries a nonsingular matrix of the prescribed order. An invertible operation on one of its two indices takes it to an equality wire at the very same sites, and prices add across edges.

At each gate retain the components that are linear in each table of a specified subset and constant in every other table. A product distributes its subset disjointly between the two children, giving at most $O(3^k(s+1))$ gates. In each parse follow the child at a sum and the unique child with mark mass greater than $S/2$ at a product, until there is no such child. The stop is a product, since a single mark has mass at most one. Its two input supports and the exterior support form an ordered tripartition with each mass at most $S/2$. For fixed supports the two input polynomials and every eligible exterior context factor, because the choice above the stop uses only the supports. Grouping by tripartition expresses the output as a sum of tensors of three-way rank at most $R=O(3^k(s+1))$ each, where $s$ is the original circuit size. Here three-way rank is the number of products of one tensor on each of the three parts. Thus a single common label in $[R]$ suffices to contract each term.

For one tripartition write $a_1,a_2,a_3$ for its fractions of the total mark mass and $b_i=\lambda\Pi(d\,\mathbf{1}_{I_i})$ for the corresponding divergences in the original mark space. These sum to zero. Draw them as three successive sides of a triangle. We claim there are hubs $q_i$ of half-perimeter one, all at pairwise distances at least $1/2$, such that $\sum_i\langle b_i,q_i\rangle\ge D$.

Indeed, for positive masses the squared side lengths are $\lambda^2 S a_i(1-a_i)$. Consecutive centered vectors have inner product $-\lambda^2 S a_i a_j$, so the triangle is acute and its squared circumdiameter is $\lambda^2S\prod_i(1-a_i)$, by the area formula. The product is at least $1/4$ because its logarithm is concave on $\{0\le a_i\le1/2,\ \sum a_i=1\}$, with that minimum at a permutation of $(1/2,1/2,0)$. To realize the circumdiameter, sum $\sum_i\langle b_i,q_i\rangle$ by parts around the three vertices. Choose the successive hub differences along the radial vectors from the circumcenter, with lengths twice its barycentric weights. Their sum is zero, and the resulting value is twice the radius. In the squared-side formula the barycentric numerator opposite side $i$ is proportional to $a_i(1-a_i)\,2a_j a_k$, giving weight $(1-a_i)/2$. All hub distances are therefore at least $1/2$. For zero mass put the two positive-mass hubs one unit apart in the divergence direction and the remaining hub at their midpoint.

The same argument already gives a simpler intermediate estimate with four ports. Temporarily omit the consecutive-table wires and put $t_0=\lceil w^4\sqrt{\log_2(2w)}\rceil$, $D_0=wt_0$ in the construction. The target price is $B_0=O(w^2t_0)$. With the hubs at displacement $y$, their common rank label costs $y\log_2 R$ because the mean width of a triangle is its half-perimeter. The sum inequality for Euclidean prices charges $O(kW)$ for all tripartitions. The tangent bound of the rectangle proof and the gain $D_0$ give

$$
 \log_2(s+1)\ge D_0-O\bigl(k+B_0y+kW/y\bigr)
              \ge D_0-O(t_0)
$$

on taking $y=\sqrt{kW/B_0}$. Thus an additive error of order $D_0^{4/5}(\log D_0)^{1/10}$ follows already from one common bound on the price of every summand.

Return to $t,D$ of the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate) and the extra consecutive-table wires. Let $j$ count changes of part between successive tables. In the fresh space the added divergences $g_i$ have $\sum_i\|g_i\|^2=H^2=2t^2j$. If $H>0$, adjoin $xg_i/H$ to each old hub. The half-perimeter rises to at most $1+6x^2$ by orthogonality and the distance lower bound, and the gain rises by $xH$. Set $x=H/(12D)$ and rescale to half-perimeter one. The gain is at least

$$
 \frac{D+H^2/(12D)}{1+H^2/(24D^2)}
 \ \ge\ D+\gamma j,\qquad \gamma=c\,t^2/D
$$

for an absolute $c>0$, since $H^2/D^2=O(k/w^2)=O(1)$. This also holds at $j=0$. Translate the hubs so that all their norms are at most one.

We use two more parts of the Euclidean price theorem used in [Section 2 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.2). Sharing an $R$-valued label among sites $Q$ has price $W(Q)\log_2 R$. For three sites $W(Q)$ is their half-perimeter, since for any three real numbers the sum of the pairwise absolute differences is twice their range. On the fixed sites $P$, $2^{\operatorname{price}/W}$ is a spectral point. Its value on an ordinary sum is at most the sum of its values, by restriction from the direct sum. For a term with $j$ changes put its hubs at $yq_i$, $y>0$. The common label costs $y\log_2 R$. Each spoke length is bounded as in the rectangle proof. Its linear gain, summed over spokes, is at least $y(D+\gamma j)$, and all quadratic errors total at most $2By^2$. At most $3\binom{k-1}{j}2^j$ assignments have $j$ changes. Divide the sum of the spectral bounds by the spectral value $2^{B/W}$ of the target to get

$$
 1\le
  2^{[y(\log_2 R-D)+2By^2]/W}
       \,3\bigl(1+2\cdot 2^{-y\gamma/W}\bigr)^{k-1}.
$$

The extraction and reshaping maps are linear on the fixed coefficient space. The spectral sublevel set defined by this single upper bound is closed at the nonzero target, which extends the comparison to degree-component border limits. Take $y=W\log_2(4k)/\gamma$. The last factor is bounded by $3e^{1/2}$, and hence

$$
 \log_2(s+1)\ge D-O(k+By+W/y)=D-O(t).
$$

Here $By=O(w^3(\log(2w))^{3/2})$, $W/y=O(t/(w\log(2w)))$, and $k=O(w^2)$. Finally $t^4/D^3=t/w^3=\Theta((\log D)^{3/2})$, proving the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate).

## The additive transfer and the permanent

**Transfer lemma.** Suppose a nonsingular compatibility minor of order $2^c$ can be selected on

$$
              \mu(c)\le c/\log_2 b+O(\log(2+c))
$$

crossing vertices for a fixed $b>1$. Suppose the at most six incident wires of each table in the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate) can be read with $O(t)$ additional live vertices and graph size $2^{O(t)}$, with total specialization cost polynomial in the graph size. If the target has a general $\|G\|^{O(1)}a^p$ upper bound for some fixed $a>1$, the resulting graphs satisfy

$$
      \log_2 s\ge p\log_2 b-O(E(p)),\qquad \log_2 \|G\|=O(E(p)).
$$

**Proof.** Between tables at most $w+1$ words cross. Their total number of positions is at most $(D+O(t))/\log_2 b+O(w\log(2+t))$. Processing a table costs $O(t)$ further positions. Thus $p\log_2 b\le D+O(t)$ and $\log_2 \|G\|=O(t)$. Specializing to the source gives $\log_2(s+1)\ge D-O(t)$, using the degree extraction in the fixed-block transfer in [Section 3 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.3) for homogeneous border circuits. The general upper bound gives $p=\Omega(D)$, while the constructed decomposition gives $p=O(D)$. Hence $t=\Theta(E(p))$ on these graphs. If $a=b$ the same comparison gives $p\log_2 b=D+O(t)$.

The half-set construction in [Section 4 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.4) uses $c+O(\log(2+c))$ terminals per $c$-bit word. A table of total incident capacity $O(t)$ uses $O(t)$ live vertices and has size $2^{O(t)}$, with maximum degree three. Applying the [transfer lemma](#the-additive-transfer-and-the-permanent) with $b=2$ proves the permanent row of the [additive theorem](#the-additive-theorem).

For independent sets, the [independent-set construction](sharp-pathwidth-bases.pdf#nameddest=section.5) gives $p\le D+O(t)$ and $\log_2 \|G\|=O(t)$ on the source of the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate). The source lower bound and the bag dynamic program give $p\ge D-O(t)$. Since $t=\Theta(E(D))$, this proves the independent-set row.

### Edge boundaries

The same transfer gives a cutwidth bound when each crossing word is carried by edges. Suppose blocks of $\mu$ edges carry at least $\mu\log_2 b-O(\log \mu)$ bits and can be processed serially with $O(t)$ additional crossing edges per table and size $2^{O(t)}$. Use $\mu=\Theta(\sqrt t)$, rounding each word up to a whole number of blocks. Across a prefix the number of edges is at most $D/\log_2 b+O(t+D\log(\mu)/\mu+w\mu)=D/\log_2 b+O(t)$ by the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate). With a general single-exponential upper bound in cutwidth the proof of the [transfer lemma](#the-additive-transfer-and-the-permanent) gives the same additive conclusion for minimum cutwidth. At fixed block size the corresponding fixed-base transfer follows by charging the constant cost of rounding once per crossing word as in the fixed-block transfer in [Section 3 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.3).

## An additive bound at the partition-table scale

Mannens and Nederlof classify numerical Tutte evaluation at integer points. The bounds here count gates for the formal edge-weighted polynomial. [Mannens–Nederlof, Theorem 1.1](https://arxiv.org/abs/2307.01046)

For a bag of $k$ vertices, keep the conditional spin sum for each exact equality partition of the live colors. When forgetting a vertex and fixing the partition of the other vertices with $j$ classes, sum its $j$ possible placements in an existing class and its placement in a new class with multiplicity $q-j$. An edge contributes $1+w_e$ when its ends agree, and one otherwise. At finite effective palette $r$ only partitions with at most $r$ classes occur. With a formal parameter the recurrence is a polynomial identity by evaluation at every sufficiently large integer palette, and so it specializes in every field. This gives $O(\|G\| B_r(p+1))$ gates uniformly in $r$.

The lower bound must account for the entropy lost to unnamed colors. For instance $\log_2\operatorname{Bell}(p+1)$ and $p\log_2 p$ differ by order $p\log\log p$, already larger than the allowed additive error. We encode the equality partition itself.

### Small palettes

Take $D,t,w$ from the [ordered source estimate](#an-ordered-source-for-the-sharper-estimate). For $2\le r\le D^{2/3}$, store each $c_e$-bit word on $\lceil c_e/\log_2 r\rceil$ named sites. Keep the $r$ clique anchors from [Section 6 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.6) throughout. Scan the candidate tuples of the incident sites to realize a table. Each implication uses $O(r)$ constant-length paths, processed in sequence. For $r=2$ use the two-spin corner constructed there. Visiting $r^b$ tuples on $b$ incident sites costs $2^{O(t)}\operatorname{poly}(D)$, because $b\log_2 r=O(t+\log r)$. Thus

$$
    (p+1)\log_2 r\le D+O(t+(r+w)\log(2+r))=D+O(t),
    \qquad \log_2 \|G\|=O(t).
$$

Only the current table's incident positions and $O(1)$ working vertices beyond the anchors are needed. The anchor factor $r!$ is invertible at every finite effective palette. The source bound and the conditional spin sweep give $D-O(t)\le\log_2 B_r(p+1)\le D+O(t)$.

### Encoding a partition in consecutive pieces

For $r>D^{2/3}$ reserve $s_0=3+s'$ distinct colors, where $s'=2^{\lfloor(\log_2 t)/2\rfloor}$. For $r=\infty$ use $r-s_0=\infty$. Choose an integer $A=D+O(t)$ at least the number of bits crossing any cut. On $P$ ordered memory sites name the classes of a partition by first occurrence. Divide the sites into $b=\lceil P/\mu\rceil$ consecutive pieces of length at most $\mu=\lceil\sqrt P\rceil$. A list of integers $h_1,\ldots,h_b$ specifies how many new names first occur in each piece. For this fixed list the words in a piece can use the earlier names and exactly its prescribed new names, in their canonical order. Their choices in different pieces are independent. If their alphabet sizes are $a_i$, summing $\prod_i a_i$ over all lists with $\sum h_i\le r-s_0$ gives $B_{r-s_0}(P)$. There are at most $(\mu+1)^b$ lists. Some list therefore carries at least

$$
         \sum_i\lfloor\log_2 a_i\rfloor
         \ \ge\ \log_2 B_{r-s_0}(P)-b\log_2(\mu+1)-b
$$

independent bits. Fix that list and a power-of-two subalphabet in each piece.

Choose the least $P$ for which $\log_2 B_{r-s_0}(P)-c\sqrt P\log_2(2+P)\ge A$, with a fixed sufficiently large $c$. Then $P=\Theta(D/\log D)$. Indeed $B_{r-s_0}(P)\le P^P$, and at $P=C D/\log D$ one can introduce $\lfloor\sqrt P\rfloor$ distinct names first and then use those names freely. That fits the available palette, and suffices for a large constant $C$. A further site multiplies the partition count by at most $P+1$, so the logarithmic capacity at this $P$ exceeds $A$ by only $O(\sqrt P\log P)$.

Reserving scratch colors also fits the budget. For a partition using $j>r-s_0$ names, erase its $j-(r-s_0)$ smallest blocks by merging them into the first surviving block in canonical order. Their union has at most $Ps_0/(r-s_0)$ sites. Recording those sites and their induced partition suffices to reconstruct the original by removing the recorded sites and restoring their blocks. Thus

$$
 \log_2 B_r(P)-\log_2 B_{r-s_0}(P)
      =O\bigl((1+Ps_0/(r-s_0))\log(2+P)\bigr)=O(t).
$$

For the last bound use $r>D^{2/3}$, $s_0=O(\sqrt t)$, and $t=\Theta(E(D))$. The loss is zero if $r-s_0\ge P$ or $r=\infty$.

### Reading equality into a bit

Reserve three anchors $c_0,c_1,d$ and the $s'$ scratch anchors by a clique of hard disequalities. Data avoid all reserved colors. In an integer palette of size $q$, an edge of weight $u$ contributes $1+u[x=y]$. To list a spin $x$ on a nonempty set $T$ of anchors excluding $d$, require $x\ne d$. Join a fresh center to $x$ and all of $T$ with weight one, and to $d$ with weight $-q-1-|T|$. The constant terms cancel upon summing the center, and a collision with one listed anchor supplies one, giving $\sum_{c\in T}[x=c]$. Unary activities on the list follow by edges to its anchors.

Let $x,y$ avoid $c_0,c_1,d$, and let a listed bit $\beta$ take $c_0,c_1$. Set $J=[x=y]$ and $H=[\beta=c_1]$. A center joined to $x,y,\beta,c_1,d$ with weights $u,1,v,1,s$ sums to $q+u+v+2+s+uJ+vH$. Choose $s$ so the constant is one, and use two centers with $(u,v)=(1,-1),(-1,1)$. The resulting product $(1+J-H)(1-J+H)$ is exactly $[J=H]$ in every characteristic. This works for comparing a data position to another, or a scratch word to a scratch anchor. Comparing a position with itself returns true directly. The two-spin corner in [Section 6 of the pathwidth paper](sharp-pathwidth-bases.pdf#nameddest=section.6) now realizes a listed bit implication. To forbid one tuple of a constant-arity Boolean relation, introduce a switch with activities $1,-1$. When on, implications force all the entries of that tuple. Summing the switch removes exactly the forbidden tuple. This implements deterministic Boolean gates with conditioned weight one.

### Reading and replacing the stored words

Initialize the memory sites to the partition encoding the zero address by testing their required equalities and disequalities. To find the canonical name at site $j$, locate the first equal site and count first occurrences up to it, testing each first occurrence by a scan of preceding sites. The loops use polynomially many comparisons and $O(\log P)$ bits besides the memory. A variable address can be implemented by scanning all positions in a fixed order and selecting the requested one with a Boolean test. A whole piece has at most $\mu$ names. Store its name list in $O(\mu\log P)$ bits and scan its fixed subalphabet, of size at most $P^\mu$, to translate to or from its binary address. To rewrite a piece keep its old sites until its replacements have been installed. Each new site must equal the old representative of its prescribed name. Test this by scanning every candidate representative and imposing the conditional equality just described. The old memory contains every name used by the list. Thus each new site has a unique actual color, and the new partition preserves the association of canonical names to colors even when a first occurrence moves inside the piece.

Use these bits for the crossing labels. At an input table read its incoming labels, guess the outgoing bits, and emit its one addressed variable by a scan of the table. Close exhausted labels and write new bits in the vacated or free slots. The allocation of slots is fixed by the order of the source. All input and output bits of the table fit in $O(t)$ ordinary bits of temporary storage, including the counters and the current piece, since $\mu\log P=O(t)$. The unrolled number of operations is $2^{O(t)}$. With an initial naming fixed, every full wire assignment contributes its table product exactly once.

Pack persistent temporary bits in groups of $\log_2 s'$ per spin, listed on the $s'$ scratch anchors. Read a word's digits by comparing it to each possible anchor in turn. Testing the desired digits uniquely determines a replacement word. One bit instruction can be simulated with a constant number of unpacked words, $O(\log s')$ ordinary Boolean temporaries, and polynomial overhead in $s',t$. The width and size are consequently bounded by

$$
 p\le P+O(\mu+s'+t/\log s'+\log s')=P+O(t/\log t),
 \qquad \log_2 \|G\|=O(t).
$$

A table entry can be attached to the true value of an exact-address test by a unary activity. Parallel factors on one pair, if present, merge into one weight by multiplying their equal-spin factors. The total arithmetic overhead of these substitutions is polynomial in the construction size. One can also keep the tested entries on separate private bits.

If the chosen list uses $a=\sum_i h_i$ names, the specialized cluster polynomial equals $(q)_{s_0+a}F_H$, where $(q)_d=q(q-1)\cdots(q-d+1)$. The factor counts the mutually distinct anchor and initial data colors. All later actual colors are either forced, summed by an exact gadget, or chosen as wire bits. This identity follows for all sufficiently large integers $q$ from the spin sum, hence formally by polynomial identity. One may first work with formal generic constants in the two-spin corner and clear its nonzero normalizations. All coefficient identities then survive reduction to the field, and the corner constants can be chosen in its algebraic closure. The falling factorial is nonzero at every stated scalar. For free $Q$ evaluate at a transcendental element over the ground field, where the same source lower bound applies. Dividing by the scalar gives $\log_2 s\ge D-O(t)$, also for ordinary border size by bounded-degree specialization. Adding $O(t/\log t)$ sites changes $\log_2 B_r(P)$ by $O(t)$. The upper sweep in minimum width now gives

$$
              \log_2 B_r(p+1)=D+O(t),\qquad t=\Theta(E(\log_2 B_r(p+1))).
$$

The change $w_e=-y_e$ costs at most one gate per edge in either direction. This completes the palette row of the [additive theorem](#the-additive-theorem) for both graph polynomials.

## Hamiltonian cycles

The undirected pathwidth bases use the fingerprint rank law of [Curticapean, Lindzey and Nederlof](https://arxiv.org/abs/1709.02311) and the characteristic-two matching basis of [Cygan, Kratsch and Nederlof](https://arxiv.org/abs/1211.1506). Here these ranks enter the additive circuit-size estimate. The tour paper also uses the characteristic-three tilting calculation of [Benson, Etingof and Ostrik](https://arxiv.org/abs/2003.10499), and discusses the undirected cutwidth precedent of [Bojikian, Chekan and Kratsch](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.13).

For a $c$-bit vertex wire use a nonsingular minor of order $2^c$ on $\mu\le c/\log_2 b+O(\log(2+c))$ shared sites. The boundary rank bound $b^\mu/\mu^{O(1)}$ suffices. At each end, a $c$-bit index chooses a physical state from the selected row or column list. The guarded graph in the tour paper tests the resulting pair. For each of the $O(\mu^2)$ candidate connections, read its selection bit from the index, create its guard and finish that bit before reading the next one. The bit paths, relays and private terminals require $O(c)$ live vertices per wire. The complete table has size $2^{O(t)}$. For the degree bound on directed tours use the paper's selectors as combs in incidence order. Each suffix has a leaf and the next suffix as children, and its representative is its first leaf. This takes constantly many additional live ends per active private vertex. The transfer lemma now gives all five tour pathwidth rows. [Directed states and selectors](matching-connectivity-width.pdf#nameddest=section.6) · [Undirected states and graph realization](matching-connectivity-width.pdf#nameddest=section.7)

For a cut measured in edges take even $\mu=\Theta(\sqrt t)$ and split each wire into blocks of $\ell_\mu\ge \mu\log_2 b-O(\log \mu)$ bits. For the last block with $r$ bits select a nonsingular minor of order $2^r$. There are at most $w+1$ crossing words. Between tables the edge count is at most

$$
 D/\log_2 b+O(t+D\log(\mu)/\mu+w\mu)=D/\log_2 b+O(t).
$$

Process the blocks of one table successively. Its incident blocks have $O(t)$ exterior ports altogether. Only the current block needs its private routing graph, with $O(\mu^2)=O(t)$ candidate connections. Generate each selection bit and its guard at its lookup. The address bits and their bounded-degree verifier paths leave $O(t)$ unfinished ends, and the chain of terminals adds $O(1)$ across blocks. This counts antiparallel arcs separately when measuring arc cutwidth. Total size is $2^{O(t)}$. Minimum cutwidth $k$ therefore satisfies $k\log_2 b\le D+O(t)$, and the source gives $\log_2 s\ge D-O(t)$. The single-exponential pathwidth upper bound and $p\le k$ give $k=\Omega(D)$, hence $t=\Theta(E(k))$. [Compatibility ranks for the three edge cuts](matching-connectivity-width.pdf#nameddest=section.8)

| Cut measured | Characteristic | Base $b$ for $L=k\log_2 b$ |
|---|---|---|
| Undirected edges | Zero, two, three, respectively | $5$, $1+\sqrt2$, $2+2\cos(2\pi/9)$ |
| Underlying edges of a directed graph | Other than two / two | $5$ / $1+2\sqrt2$ |
| Directed arcs | Other than two / two | $3$ / $1+\sqrt2$ |

More generally, if the undirected matching connectivity rank satisfies $r_j\ge u^j/j^{O(1)}$ on positive even orders, the two undirected lower bases with this error are $2+u$ at a vertex cut and $1+u$ at an edge cut. This includes every finite-block certificate $u=r_a^{1/(a-2)}$ for even $a\ge4$. An additive estimate at the limiting base uses quantitative control of that rate. [Rank substitution and finite blocks](matching-connectivity-width.pdf#nameddest=section.2)
