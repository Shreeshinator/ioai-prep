# PCA: from 2-D to k-D

**A standalone guide to principal component analysis (PCA), extracted and expanded from `notebooks/03_algorithms.ipynb` §7.**

This document contains the complete PCA concept-learning section from the notebook. It also pulls together the PCA material that appears elsewhere in the repository: the reasoning note in `RESOURCES.md`, practice problem 3.5, the Connect question, and the requested companion animation. Everything needed to follow the argument is written here, including the numerical results that the notebook's code produces. You do not need to open or run the notebook to read this guide.

> **What PCA is for.** Your robot records a gesture as two numbers: peak acceleration and duration. The microcontroller can afford to store only one number per gesture. Which one number loses the least information? PCA answers that question by finding the direction along which the data is most spread out, then storing each point's position along that direction.

---

## What you will be able to do

After working through this guide you should be able to:

- centre a cloud of points and explain why centring is required;
- project points onto a direction and compute the spread of the shadows;
- build a scatter matrix and a covariance matrix from three sums;
- explain why the best direction is an eigenvector of that matrix;
- solve the 2×2 eigenproblem by hand with a quadratic;
- find the PC1 angle and the fraction of spread it keeps;
- generalize from one component to $k$ components: projection, retained variance, and reconstruction error;
- recognize the assumptions and failure modes of PCA.

## Before you start

You need coordinates, Pythagoras' theorem, averages, and the quadratic formula. The quadratic formula is stated where it is used. Calculus appears once, in an optional derivation of why the best direction is an eigenvector; the result is also proved without calculus in the Going further section at the end. Technical terms are defined as they are needed, and there is a [glossary](#glossary) at the end.

**Running example.** The same four centred points are used throughout:

| Point | $x$ | $y$ | $x^2$ | $y^2$ | $xy$ |
|---|---:|---:|---:|---:|---:|
| $p_1$ | −2 | −1 | 4 | 1 | 2 |
| $p_2$ | −1 | 0 | 1 | 0 | 0 |
| $p_3$ | 1 | 1 | 1 | 1 | 1 |
| $p_4$ | 2 | 0 | 4 | 0 | 0 |
| **Sum** | **0** | **0** | **10** | **2** | **3** |

The means are $0$, so the points are already centred. The three sums are

$$
a=\sum x^2=10,\qquad b=\sum y^2=2,\qquad c=\sum xy=3.
$$

These three numbers will decide the spread in every direction. The resulting scatter matrix is

$$
S=\begin{bmatrix} a & c \\ c & b \end{bmatrix}
 =\begin{bmatrix} 10 & 3 \\ 3 & 2 \end{bmatrix}.
$$

## Notation at a glance

| Symbol | Meaning |
|---|---|
| $x,y$ | Coordinates of a point after centring. |
| $n$ | Number of points. |
| $\theta$ | Angle of a direction, measured from the positive $x$-axis. |
| $u=(\cos\theta,\sin\theta)$ | Unit vector in direction $\theta$. |
| $t=u\cdot p$ | Shadow (projection) of point $p$ on direction $u$. |
| $\sum t^2$ | Spread along $u$ for centred data. |
| $S$ | Scatter matrix, entries $\sum x^2,\sum xy,\sum y^2$. |
| $C=S/n$ | Covariance matrix (population convention). |
| $\lambda$ | Eigenvalue: the stretch factor of an eigenvector, and the spread along it. |
| $U_k$ | Matrix whose columns are the top $k$ principal directions. |
| $p$ | A point (column vector) in $d$ dimensions. |
| $t=U_k^\top p$ | The $k$ new coordinates of $p$. |
| $\hat p=U_kU_k^\top p$ | Best rank-$k$ reconstruction of $p$. |

## Contents

- [7a. Shadows and the spread along a direction](#7a-shadows-and-the-spread-along-a-direction)
- [7b. The scatter matrix and covariance](#7b-the-scatter-matrix-and-why-covariance-is-the-right-object)
- [7c. Eigenvectors and eigenvalues](#7c-eigenvectors-directions-the-matrix-only-stretches)
- [7d. The constrained-optimization derivation](#7d-where-the-eigenvector-equation-comes-from-maximizing-variance-under-a-constraint)
- [7e. Solving the 2×2 quadratic](#7e-finding-eigenvalues-with-a-quadratic)
- [BUILD 7: `pca_2d`](#build-7-pca_2d)
- [EXPLORE: numpy comparison and stretching](#explore-check-against-numpy-then-stretch-the-data)
- [7f. From 2-D to k-D](#7f-from-2-d-to-k-d-projection-retained-variance-and-reconstruction)
- [Practice check: problem 3.5](#practice-check-problem-35-pca-in-2-d)
- [Connect: PCA and the linear classifier](#connect-pca-and-the-linear-classifier)
- [Going further](#going-further)
- [What to remember](#what-to-remember)
- [Glossary](#glossary)

---

## 7. PCA: from 2-D to k-D

Suppose the microcontroller can only afford to keep **one** number per gesture instead of two. Which single number keeps the most information? **PCA** (principal component analysis) answers that: it finds the direction along which the data is most spread out.

The whole section is one idea followed through: pick a direction, measure how much the data spreads along it, and choose the direction that maximizes that spread. We first do this geometrically (7a), then discover that three sums decide the answer for *every* direction (7b), then interpret the special directions where the matrix only stretches (7c), derive them as the solution of a constrained optimization problem (7d), and solve the resulting quadratic by hand (7e). Section 7f generalizes from keeping one number to keeping $k$.

### 7a. Shadows, and the spread along a direction

**The goal in one sentence.** Keep the smallest number of numbers per point while losing as little of the cloud's shape as possible. The trick is to choose a good *direction* first, then store each point's coordinate along that direction.

- **Centred data:** subtract the mean $x$ from every $x$, and the mean $y$ from every $y$. The cloud's centre is then at $(0,0)$. Centring matters because PCA studies how points differ *from their average*, not where the cloud happens to sit. Shifting every point by the same vector must not change the answer, and centring is exactly the shift that removes the mean.
- **Direction:** a direction at angle $\theta$ from the $x$-axis is the arrow $u=(\cos\theta,\sin\theta)$. If you have not met $\cos$ and $\sin$: they are the coordinates of the point at angle $\theta$ on the circle of radius 1. For example $\theta=0^\circ$ gives $(1,0)$, $\theta=90^\circ$ gives $(0,1)$, and $\theta=45^\circ$ gives $(0.707,0.707)$.
- **Unit length:** because $\cos^2\theta+\sin^2\theta=1$, $u$ always has length 1. PCA always compares unit directions. If we allowed longer arrows, every shadow would grow and "spread" would increase just by scaling the arrow, which says nothing about the data. The unit-length requirement is the **normalization constraint** that will reappear in 7d.
- **Shadow (projection):** the shadow of a point $(x,y)$ on the line through the origin in direction $u$ is

  $$
  t=x\cos\theta+y\sin\theta.
  $$

  This "multiply matching parts and add" is called the **dot product** of the point with $u$. The result $t$ is a single **signed number**: positive if the shadow falls in the direction of $u$, negative if it falls behind the origin. Example: the shadow of $(2,1)$ on the $x$-axis ($\theta=0$) is just $2$.
- **Spread along $u$:** $\sum t^2$, the sum of the squared shadows. For centred data this is $n$ times the variance of the shadows.

**Variance, spread, and why we square.** Let $\bar t=(1/n)\sum t$ be the mean shadow. The population variance of the shadows is $(1/n)\sum(t-\bar t)^2$, and the sample variance is $(1/(n-1))\sum(t-\bar t)^2$. For centred points the shadows also have mean $0$, so these become $(1/n)\sum t^2$ and $(1/(n-1))\sum t^2$. Since $n$ is fixed, maximizing the spread, the population variance, or the sample variance is the *same* optimization problem. The reported "fraction of spread" is a ratio, so the factors $n$ and $n-1$ cancel anyway.

Squaring rather than taking absolute values matters for three reasons:

- It matches variance, the standard measure of spread.
- It decomposes cleanly: $\sum(t_1+t_2)^2=\sum t_1^2+2\sum t_1t_2+\sum t_2^2$. That cross term is the covariance, which is why the next subsection is about covariance.
- Squared error is exactly what an orthogonal projection minimizes, which gives the reconstruction interpretation below.

**Every projection loses something.** A point $p$ in the plane splits uniquely into a part along $u$ and a part perpendicular to $u$:

$$
p=(u\cdot p)\,u+r,
$$

where $r$ is perpendicular to $u$. By Pythagoras,

$$
|p|^2=(u\cdot p)^2+|r|^2.
$$

Summing over all centred points:

$$
\sum |p|^2=\text{spread along }u+\text{squared reconstruction error}.
$$

The left side is fixed by the data. Therefore **maximizing the spread is exactly the same as minimizing the squared reconstruction error** — the amount of each point left "off the line". This is the trade-off that section 7f quantifies. It is also the reason PCA can be described either as "keep the most variance" or as "lose the least squared distance".

**PC1**, the first principal component, is the direction with the largest spread. Keeping each point's shadow on PC1 loses the least information.

#### Smallest example: four points

The running example has $P=\{(-2,-1),(-1,0),(1,1),(2,0)\}$. Its means are $0$, so it is already centred. The shadows at three obvious angles are:

| Point | Shadow at $0^\circ$ | Shadow at $45^\circ$ | Shadow at $90^\circ$ |
|---|---:|---:|---:|
| $(-2,-1)$ | −2.000 | −2.121 | −1.000 |
| $(-1,0)$ | −1.000 | −0.707 | 0.000 |
| $(1,1)$ | 1.000 | 1.414 | 1.000 |
| $(2,0)$ | 2.000 | 1.414 | 0.000 |
| **Spread $\sum t^2$** | **10.000** | **9.000** | **2.000** |

> **PREDICT:** square and add each column. Which of $0^\circ$, $45^\circ$, and $90^\circ$ has the biggest spread? Is some other angle better still?

The $0^\circ$ direction wins among these three, with spread $10$. But it is not the best possible direction. The spread as a function of angle is:

| $\theta$ | $0^\circ$ | $15^\circ$ | $18.43^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $75^\circ$ | $90^\circ$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Spread $\sum t^2$ | 10.000 | 10.964 | **11.000** | 10.598 | 9.000 | 6.598 | 4.036 | 2.000 |

The maximum is $11.000$ at about $18.43^\circ$. (Other values: at $105^\circ$ the spread is $1.036$, at $120^\circ$ it is $1.402$, at $135^\circ$ it is $3.000$, and at $150^\circ$ it is $5.402$. A direction and its opposite describe the same line, so $180^\circ$ repeats $0^\circ$.)

**Why the answer is not obvious.** The $0^\circ$ and $90^\circ$ directions measure one feature at a time; $45^\circ$ mixes the features. A direction can beat both by following the diagonal along which the cloud is elongated. If the data were a perfect circle (equal spread in every direction), no direction would beat any other. If it were a thin cigar, the best direction would be the cigar's long axis. Real clouds lie between those extremes, so we need a calculation rather than a guess.

If you run the notebook, the code that produces the table also plots the full spread curve. The curve is a smooth hump with its peak near $18.43^\circ$; the exact value comes from the quadratic in 7e.

---

### 7b. The scatter matrix, and why covariance is the right object

Expand one squared shadow:

$$
(x\cos\theta+y\sin\theta)^2
=x^2\cos^2\theta+2xy\sin\theta\cos\theta+y^2\sin^2\theta.
$$

Add over all points:

$$
\text{spread}(\theta)=\cos^2\theta\sum x^2
+2\sin\theta\cos\theta\sum xy
+\sin^2\theta\sum y^2
$$

So just **three sums** decide the spread in *every* direction:

- $a=\sum x^2$ — how much $x$ alone varies;
- $b=\sum y^2$ — how much $y$ alone varies;
- $c=\sum xy$ — how $x$ and $y$ vary *together*.

Arrange them in a square table of numbers, a **matrix**, called the **scatter matrix**:

$$
S=\begin{bmatrix}\sum x^2 & \sum xy\\ \sum xy & \sum y^2\end{bmatrix}
=\begin{bmatrix}a & c\\ c & b\end{bmatrix}.
$$

For the running example,

$$
S=\begin{bmatrix}10 & 3\\ 3 & 2\end{bmatrix}.
$$

It is **symmetric**: the top-right and bottom-left entries are both $c$. Symmetry is not cosmetic. It guarantees that the eigenvalues are real and that eigenvectors belonging to different eigenvalues are perpendicular, which is precisely what lets PCA produce uncorrelated coordinates.

**Matrix times vector.** Each row of the matrix takes a dot product with the vector. So

$$
\begin{bmatrix}a & c\\ c & b\end{bmatrix}
\begin{bmatrix}u_1\\ u_2\end{bmatrix}
=
\begin{bmatrix}a u_1+c u_2\\ c u_1+b u_2\end{bmatrix}.
$$

Tiny example:

$$
\begin{bmatrix}2 & 1\\ 1 & 3\end{bmatrix}
\begin{bmatrix}1\\ 0\end{bmatrix}
=
\begin{bmatrix}2\\ 1\end{bmatrix}.
$$

With this notation,

$$
\text{spread}(\theta)=u\cdot(Su)=u^\top S u.
$$

Multiply it out and you get the formula above.

#### What the three sums mean

- $a$ and $b$ are the **unnormalized variances** of the individual features: $a/n$ is the variance of $x$, and $b/n$ is the variance of $y$. Use $n-1$ instead of $n$ for the sample variance. They measure spread *within* one feature.
- $c$ is the **unnormalized covariance** of $x$ and $y$: $c/n$ is the covariance, or $c/(n-1)$ for the sample version. Its sign tells you how the features move together:
  - $c>0$: above-average $x$ tends to come with above-average $y$ (an upward-sloping cloud);
  - $c<0$: above-average $x$ tends to come with below-average $y$ (a downward-sloping cloud);
  - $c\approx0$: little linear co-movement; the cloud is roughly axis-aligned.
- The *size* of $c$ is hard to read on its own because it depends on the units and on how large $a$ and $b$ are. Dividing by the standard deviations (the square roots of the variances) gives the **correlation**

  $$
  r=\frac{c}{\sqrt{ab}},
  $$

  which is unit-free and always lies in $[-1,1]$. $|r|=1$ means the points lie exactly on a line; $r=0$ means no linear relationship.
- If $c=0$, $S$ is diagonal. Then $S\cdot(1,0)=(a,0)$ and $S\cdot(0,1)=(0,b)$, so the coordinate axes are already the natural directions.

**Covariance matrix.** Statisticians usually divide the scatter matrix by the number of points: $C=S/n$ (population convention) or $C=S/(n-1)$ (sample convention). Both are called the **covariance matrix**. Its diagonal holds the variances and its off-diagonal holds the covariances, which is exactly why it carries both kinds of information:

- **variance** — how much a single feature spreads out (diagonal);
- **relationship** — how two features move together (off-diagonal).

$C$ has exactly the same eigenvectors as $S$, and every eigenvalue is divided by the same constant $n$ or $n-1$. Therefore **the principal directions and the retained-variance fractions are identical under either convention**; only the numerical scale of the eigenvalues changes. If you standardize each feature first (subtract its mean, divide by its standard deviation), $C$ becomes the **correlation matrix**, whose diagonal is all 1s.

**Why the covariance matrix captures variance in any direction.** For a unit direction $u$, the variance of the shadows is

$$
\operatorname{Var}(t)=\frac{1}{n}\sum t^2=u^\top C u.
$$

Read that formula slowly. The diagonal of $C$ contributes each feature's own variance; the off-diagonal contributes the "do they move together" term. A direction that lines up with a high-variance feature and with the direction of co-movement gets a large value. PCA's entire job is to choose $u$ to maximize this quantity. The covariance matrix is therefore not an arbitrary container: it is the object that turns "variance along $u$" into a matrix expression, so that the search over directions becomes an eigenproblem.

**Two useful facts.**

- $\operatorname{trace}(S)=a+b=\sum x^2+\sum y^2$ is the **total spread**.
- $\det(S)=ab-c^2$ measures how genuinely two-dimensional the cloud is. If one feature were an exact linear function of the other, $\det(S)=0$ and all points would lie on a line.

Both quantities reappear when we solve for the eigenvalues in 7e.

**Check the matrix against the direct sum.** For the running example, $a=10$, $b=2$, and $c=3$. The identity $u\cdot(Su)=\sum t^2$ gives:

| $\theta$ | $u$ | $Su$ | $u\cdot(Su)$ | Direct $\sum t^2$ |
|---|---:|---:|---:|---:|
| $0^\circ$ | $(1,0)$ | $(10,3)$ | 10.000 | 10.000 |
| $30^\circ$ | $(0.866,0.500)$ | $(10.160,3.598)$ | 10.598 | 10.598 |
| $45^\circ$ | $(0.707,0.707)$ | $(9.192,3.536)$ | 9.000 | 9.000 |
| $90^\circ$ | $(0,1)$ | $(3,2)$ | 2.000 | 2.000 |

The two computations agree, as they must. This is a useful numerical check: if they disagree, the matrix was assembled wrongly or the angle was interpreted in the wrong units.

**Limits.** Covariance detects *linear* co-movement only. If $y=x^2$, the covariance can be near $0$ even though $y$ is perfectly predictable from $x$, and PCA will miss the curved structure. PCA is also sensitive to units: metres versus millimetres can make one feature dominate. Standardizing features is the usual remedy.

---

### 7c. Eigenvectors: directions the matrix only stretches

Multiply $S$ by a direction $u$ and you usually get an arrow pointing somewhere *else*: the matrix turns it as well as stretching it. The table below applies $S$ to arrows at several angles.

> **PREDICT:** is there a direction that $S$ does not turn at all? Use the spread curve from 7a to guess where it might be. (Hint: at the peak of the spread curve the slope is momentarily zero, so the best direction is also the direction in which the spread is not changing.)

| $\theta$ of $u$ | $u$ | $Su$ | Angle of $Su$ (mod $180^\circ$) | Length of $Su$ |
|---|---:|---:|---:|---:|
| $0^\circ$ | $(1.000,0.000)$ | $(10.000,3.000)$ | $16.70^\circ$ | 10.440 |
| $18.43^\circ$ | $(0.949,0.316)$ | $(10.436,3.479)$ | $18.43^\circ$ | 11.000 |
| $45^\circ$ | $(0.707,0.707)$ | $(9.192,3.536)$ | $21.04^\circ$ | 9.849 |
| $90^\circ$ | $(0.000,1.000)$ | $(3.000,2.000)$ | $33.69^\circ$ | 3.606 |
| $108.43^\circ$ | $(-0.316,0.949)$ | $(-0.316,0.949)$ | $108.43^\circ$ | 1.000 |
| $135^\circ$ | $(-0.707,0.707)$ | $(-4.950,-0.707)$ | $8.13^\circ$ | 5.000 |

At about $18.43^\circ$ the arrow comes out pointing the same way, just $11$ times longer. At $108.43^\circ$ (the perpendicular direction) it comes out the same way, with stretch factor $1$. Everywhere else it gets turned.

An **eigenvector** of $S$ is a direction that $S$ only stretches:

$$
Su=\lambda u
$$

for some number $\lambda$. That number $\lambda$ (the Greek letter lambda) is the **eigenvalue**, the stretch factor.

**How to read the two numbers.**

- **Direction.** The eigenvector is a *line*, not an arrow: $u$ and $-u$ describe the same line, so we report the angle in $[0^\circ,180^\circ)$. Geometrically it is an axis along which the cloud is stretched.
- **Magnitude.** For a unit vector, $\lambda$ is the spread of the shadows:

  $$
  \lambda=u\cdot(Su)=\sum(u\cdot p)^2.
  $$

  A large $\lambda$ means the cloud is long in that direction. $\lambda=0$ would mean every point lies on the perpendicular line (the direction carries no spread at all). For a scatter or covariance matrix, $\lambda$ is never negative because it is a sum of squares; for a general matrix, a negative eigenvalue would mean the matrix also reverses the direction.
- **Products and sums.** The eigenvalues satisfy

  $$
  \lambda_1+\lambda_2=\operatorname{trace}(S),\qquad
  \lambda_1\lambda_2=\det(S).
  $$

  Here $\operatorname{trace}(S)=a+b$ is the sum of the diagonal entries, and $\det(S)=ab-c^2$ is the determinant; both are defined formally in 7e. Together they remember the total spread and how two-dimensional the cloud is. Checking these identities is a fast way to catch arithmetic mistakes.

**The aha: PC1 is the eigenvector with the largest eigenvalue, and the spread along it equals that eigenvalue.** Compare the table with the 7a curve: the peak of the spread curve is at the "not turned" direction, and the peak height is the stretch factor.

**Why the peak must be an eigenvector.** Let $\text{spread}(\theta)=u(\theta)\cdot(Su(\theta))$, where $u(\theta)=(\cos\theta,\sin\theta)$. As $\theta$ increases, the tip of $u$ moves in the perpendicular direction $u_\perp=(-\sin\theta,\cos\theta)$, which is the derivative $du/d\theta$. Differentiating with the product rule (and using symmetry of $S$):

$$
\frac{d}{d\theta}\text{spread}=2\,(u_\perp\cdot Su).
$$

At a maximum the derivative is $0$, so $Su$ has no component along $u_\perp$. In two dimensions the only remaining possibility is that $Su$ points along $u$, which is exactly $Su=\lambda u$. This is the same "set the derivative to zero" idea as in calculus; 7d turns it into a fully general constrained-optimization argument.

**The two eigenvectors are perpendicular.** Suppose $Su_1=\lambda_1u_1$ and $Su_2=\lambda_2u_2$ with $\lambda_1\ne\lambda_2$. Then

$$
\lambda_1(u_1\cdot u_2)
=(Su_1)\cdot u_2
=u_1\cdot(Su_2)
=\lambda_2(u_1\cdot u_2),
$$

where the middle equality uses symmetry of $S$. Hence $(\lambda_1-\lambda_2)(u_1\cdot u_2)=0$. Since the eigenvalues differ, $u_1\cdot u_2=0$. This is why the principal components are **uncorrelated**: the new coordinates are measured along perpendicular axes, so they cannot contain overlapping information. If $\lambda_1=\lambda_2$, the cloud is circular in that subspace and *any* perpendicular pair of directions is equally good; that repeated-eigenvalue case is the only ambiguity.

**Total spread is preserved.** The **total spread** is $\sum x^2+\sum y^2$, whichever pair of perpendicular directions you measure along. Each point's shadows on two perpendicular directions are just its coordinates in a rotated grid, so by Pythagoras $t_1^2+t_2^2=x^2+y^2$. Add over the points:

$$
\text{spread along PC1}+\text{spread along the perpendicular direction}
=\sum x^2+\sum y^2.
$$

So **the fraction of the spread that PC1 keeps is**

$$
\frac{\lambda_1}{\sum x^2+\sum y^2}
=\frac{\lambda_1}{\lambda_1+\lambda_2},
$$

because the two eigenvalues add to the total spread. For the running example, $11+1=12=10+2$, so PC1 keeps $11/12\approx91.7\%$.

---

### 7d. Where the eigenvector equation comes from: maximizing variance under a constraint

Sections 7b and 7c gave two views of the same object. Here is the derivation that ties them together and generalizes to any number of dimensions.

We want the unit direction $u$ that maximizes the spread:

$$
\text{maximize } u^\top S u
\quad\text{subject to}\quad u^\top u=1.
$$

The constraint is essential. Without it, replacing $u$ by $10u$ multiplies the spread by $100$, so no maximum would exist. **Orthonormality** is the requirement that the directions have length 1 (**normal**) and are perpendicular to each other (**orthogonal**). In matrix form, for the chosen directions collected as columns of $U$, this is $U^\top U=I$.

Introduce a **Lagrange multiplier** $\lambda$ for the constraint and form the Lagrangian

$$
L(u,\lambda)=u^\top S u-\lambda(u^\top u-1).
$$

Setting the gradient with respect to $u$ to zero:

$$
\frac{\partial L}{\partial u}=2Su-2\lambda u=0
\quad\Longrightarrow\quad
Su=\lambda u.
$$

So the maximizing direction is automatically an **eigenvector**, and the multiplier $\lambda$ is its **eigenvalue**. Dotting $Su=\lambda u$ with $u$ gives $u^\top Su=\lambda u^\top u=\lambda$: the spread in the optimal direction is exactly the eigenvalue. Of the two eigenvectors, choose the one with the larger $\lambda$, because it gives the larger spread.

**The second component.** After choosing $u_1$, the next direction $u_2$ must (i) have length 1 and (ii) be orthogonal to $u_1$. Orthogonality matters because otherwise the second number would partly repeat the first: the two coordinates would be correlated and we would be paying twice for the same information. With two constraints and two multipliers,

$$
L=u_2^\top S u_2-\lambda(u_2^\top u_2-1)-\mu(u_2^\top u_1).
$$

Differentiating gives

$$
Su_2=\lambda u_2+\frac{\mu}{2}u_1.
$$

Dotting with $u_1$ and using

$$
u_1^\top S u_2=(Su_1)^\top u_2=\lambda_1u_1^\top u_2=0
$$

shows $\mu=0$. Hence $Su_2=\lambda u_2$: the second component is the other eigenvector, and its eigenvalue is the spread that remains. In two dimensions that is the end of the story. In $d$ dimensions the same argument repeats, producing $d$ orthonormal eigenvectors with eigenvalues $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d$.

**Why the largest eigenvalue wins.** Write any unit vector in the eigenvector basis:

$$
u=\alpha u_1+\beta u_2,\qquad \alpha^2+\beta^2=1.
$$

This is just Pythagoras, since $u_1$ and $u_2$ are perpendicular unit vectors. Then

$$
u^\top S u=\alpha^2\lambda_1+\beta^2\lambda_2.
$$

This is a weighted average of $\lambda_1$ and $\lambda_2$ with non-negative weights that sum to 1, so it can never exceed $\lambda_1$. Equality holds exactly when $\alpha^2=1$, i.e. $u=\pm u_1$. The same idea works in $d$ dimensions: write $u$ in the full eigenvector basis, and all cross terms vanish because the eigenvectors are orthogonal, leaving a weighted average of all the eigenvalues. The best $k$-dimensional subspace is therefore spanned by the $k$ eigenvectors with the largest eigenvalues, and no other $k$ directions can capture more spread.

**Rayleigh quotient (the general statement).** For any nonzero $u$, the quantity

$$
R(u)=\frac{u^\top S u}{u^\top u}
$$

is called the **Rayleigh quotient**. Its maximum over all directions is $\lambda_{\max}$, attained at the top eigenvector; its minimum is $\lambda_{\min}$; and its stationary values are exactly the eigenvalues. Normalizing $u$ to length 1 is what turns $R(u)$ into "variance along $u$", so the constraint $u^\top u=1$ is natural rather than artificial.

**Connection to the data matrix (optional).** Stack the centred points as the rows of an $n\times2$ matrix $X$. Then $S=X^\top X$. The eigenvectors of $X^\top X$ are the **right singular vectors** of $X$, and its eigenvalues are the **squared singular values** of $X$. So PCA is the first half of the singular value decomposition (SVD) of the centred data. If you have met SVD, this is the fastest way to recognize or compute PCA.

---

### 7e. Finding eigenvalues with a quadratic

Write $Su=\lambda u$ row by row:

$$
(a-\lambda)u_1+c u_2=0
\qquad\text{and}\qquad
c u_1+(b-\lambda)u_2=0.
$$

When $c\ne0$, each equation is a straight line through the origin in the $(u_1,u_2)$ plane. A non-zero $u$ can satisfy both only if they are **the same line**, which means their coefficients are in proportion:

$$
\frac{a-\lambda}{c}=\frac{c}{b-\lambda}.
$$

(If $c=0$ the matrix is already diagonal; that special case is handled in Hint 2 of BUILD 7.) Cross-multiply:

$$
(a-\lambda)(b-\lambda)-c^2=0,
$$

which expands to

$$
\lambda^2-(a+b)\lambda+(ab-c^2)=0.
$$

**The determinant view.** The same condition is usually written $\det(S-\lambda I)=0$:

$$
\det\begin{bmatrix}a-\lambda & c\\ c & b-\lambda\end{bmatrix}
=(a-\lambda)(b-\lambda)-c^2=0.
$$

A nonzero vector $u$ can solve $(S-\lambda I)u=0$ only when the matrix $S-\lambda I$ is **singular**, i.e. when its determinant is zero. This recipe works for any square matrix; the $2\times2$ case simply reduces to a quadratic.

Here $a+b$ is called the **trace** (the sum of the diagonal), and $ab-c^2$ is the **determinant**, written $\det$. So:

$$
\lambda^2-\operatorname{trace}\cdot\lambda+\det=0.
$$

The **quadratic formula** solves it:

$$
\lambda=\frac{\operatorname{trace}\pm\sqrt{\operatorname{trace}^2-4\det}}{2}.
$$

The two roots always add up to the trace. (Multiply out $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$ and compare it with the equation.) Since the trace is $\sum x^2+\sum y^2$, the fraction PC1 keeps can also be written $\lambda_1/(\lambda_1+\lambda_2)$. That is the form practice problem 3.5 uses.

**Reading the roots.** For a symmetric $2\times2$ matrix the discriminant simplifies:

$$
\operatorname{trace}^2-4\det
=(a+b)^2-4(ab-c^2)
=(a-b)^2+4c^2\ge0,
$$

so the eigenvalues are always real. If the discriminant is $0$, then $\lambda_1=\lambda_2$: the cloud is circular in its plane, every direction is a principal direction, and any perpendicular pair is an acceptable answer. The roots also satisfy $\lambda_1\lambda_2=\det$, another quick sanity check.

Then the direction comes from the first equation:

$$
\frac{u_2}{u_1}=\frac{\lambda-a}{c}.
$$

That ratio is the slope (rise over run) of the eigenvector, and its angle is $\arctan(\text{slope})$. Here $\arctan$, the inverse tangent, means "the angle whose slope is this number". For example, $\arctan(1)=45^\circ$. Because a line and its opposite are the same direction, the code reduces the angle modulo $180^\circ$ to land in $[0^\circ,180^\circ)$.

> **PREDICT:** solve the quadratic for our $S=\begin{bmatrix}10&3\\3&2\end{bmatrix}$ on paper. Then find the PC1 angle and the fraction of spread it keeps.

**Worked numbers.** For $S=\begin{bmatrix}10&3\\3&2\end{bmatrix}$:

- trace $=10+2=12$;
- determinant $=10\cdot2-3^2=11$;
- discriminant $=12^2-4\cdot11=100$, whose square root is $10$;
- eigenvalues $\lambda_1=(12+10)/2=11$ and $\lambda_2=(12-10)/2=1$;
- check: $11+1=12=\text{trace}$, and $11\cdot1=11=\det$;
- PC1 slope $=(\lambda_1-a)/c=(11-10)/3=1/3$;
- PC1 angle $=\arctan(1/3)\approx18.43^\circ$;
- fraction kept $=11/12\approx0.9167$, i.e. about $91.7\%$.

The notebook prints exactly these values:

```text
trace = 10 + 2 = 12,   det = 10·2 − 3² = 11
λ² − 12λ + 11 = 0  ->  discriminant = 12² − 4·11 = 100,  √ = 10.0
λ1 = 11.0,  λ2 = 1.0    (check: λ1 + λ2 = 12.0 = trace)
eigenvector slope = (λ1 − a) / c = (11.0 − 10) / 3 = 0.3333  ->  angle = atan(0.3333) = 18.43°
fraction of spread kept by PC1 = 11.0 / 12 = 0.9167
```

**Common traps.**

- **Slope upside down.** The slope is $u_2/u_1$, not $u_1/u_2$. For this example, the reciprocal $3$ gives $\arctan(3)\approx71.57^\circ$, which is not a principal direction; the perpendicular direction has slope $-3$, i.e. angle $108.43^\circ$.
- **Forgetting to centre.** The formula assumes the means are zero. Subtracting the means first is not optional.
- **Using a non-unit direction.** $Su=\lambda u$ defines a line; scaling $u$ does not change the eigenvalue, but the shadow formula $t=u\cdot p$ assumes $u$ is a unit vector.
- **Confusing scatter and covariance.** The eigenvalues differ by a factor of $n$ or $n-1$, but the eigenvectors and the retained fraction do not.

---

### BUILD 7: `pca_2d`

Return `(angle, fraction)`: the PC1 angle in degrees, in the range $[0,180)$, and the fraction of spread it keeps. **Centre the points first.** Use the quadratic, not `np.linalg`.

```python
def pca_2d(points):
    # your code here
    raise NotImplementedError
```

<details><summary>Hint 1: angles</summary>

A direction and its opposite are the same line, so $200^\circ$ and $20^\circ$ describe the same component. `math.degrees(math.atan2(rise, run)) % 180` lands in $[0,180)$ and handles a negative slope correctly.

</details>

<details><summary>Hint 2: the special case</summary>

If $c=0$, the formula $(\lambda-a)/c$ divides by zero. But then $S$ is already **diagonal**: $S\cdot(1,0)=(a,0)$ and $S\cdot(0,1)=(0,b)$, so the axes themselves are the eigenvectors. PC1 is the $x$-axis if $a\ge b$, otherwise the $y$-axis.

</details>

**Test cases.** These are the values the notebook's test harness checks:

| `points` | Expected `(angle, fraction)` |
|---|---|
| $P=\{(-2,-1),(-1,0),(1,1),(2,0)\}$ | $(\arctan(1/3),\ 11/12)\approx(18.43^\circ,0.9167)$ |
| $\{(1,1),(-1,-1)\}$ | $(45^\circ,\ 1.0)$ |
| $\{(1,0),(-1,0),(0,0.5),(0,-0.5)\}$ | $(0^\circ,\ 0.8)$ |
| $\{(0,3),(0,-3),(1,0),(-1,0)\}$ | $(90^\circ,\ 0.9)$ |
| $\{(1,-1),(-1,1),(0.5,0.5),(-0.5,-0.5)\}$ | $(135^\circ,\ 0.8)$ |
| $\{(1,2),(3,4)\}$ | $(45^\circ,\ 1.0)$ |

**What the tests are checking.**

- **Centring:** the test cases include symmetric and asymmetric clouds, but a correct implementation must always subtract the mean.
- **Angle range:** the $135^\circ$ case checks the modulo-180 convention; the same line could be reported as $-45^\circ$.
- **Zero covariance:** the third and fourth cases are axis-aligned, so $c=0$ and the $a\ge b$ branch matters.
- **Degenerate cloud:** the second and sixth cases lie exactly on a line, so one eigenvalue is $0$ and PC1 keeps $100\%$ of the spread.
- **Fraction:** the fifth case keeps $0.8$, so the fraction is not always $1$.

<details><summary>Reference implementation (spoiler)</summary>

```python
import math

def pca_2d(points):
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n
    centred = [(x - mean_x, y - mean_y) for x, y in points]

    a = sum(x * x for x, y in centred)
    b = sum(y * y for x, y in centred)
    c = sum(x * y for x, y in centred)

    trace = a + b
    det = a * b - c * c
    disc = trace * trace - 4 * det
    lam1 = (trace + math.sqrt(disc)) / 2

    if c == 0:
        angle = 0.0 if a >= b else 90.0
    else:
        slope = (lam1 - a) / c
        angle = math.degrees(math.atan(slope)) % 180

    return angle, lam1 / trace
```

</details>

---

### EXPLORE: check against numpy, then stretch the data

First, compare your `pca_2d` with numpy's eigenvalue routine on random clouds. This is a valuable habit: two independent computations of the same quantity catch sign errors, branch errors in `atan2`, and mistakes in the centring step. With numpy's `eigh`, the eigenvalues are returned in ascending order, so the top eigenvector is the **last** column.

For the fixed random seed used in the notebook, the comparison is:

| Cloud | Your `pca_2d` | numpy `eigh` |
|---|---:|---:|
| 0 | $163.93^\circ,\ 0.8685$ | $163.93^\circ,\ 0.8685$ |
| 1 | $176.82^\circ,\ 0.9928$ | $176.82^\circ,\ 0.9928$ |
| 2 | $99.92^\circ,\ 0.9325$ | $99.92^\circ,\ 0.9325$ |

The two methods agree to the printed precision. If they do not agree, check the angle convention first: `eigh` returns a direction, and the code converts it to a line in $[0,180)$ with `atan2(...) % 180`.

Then a prediction:

> **PREDICT:** double every $y$-value of our four points. Does the PC1 angle go up or down? Does PC1 keep more or less of the spread?

Think in terms of the covariance matrix before you compute. Doubling $y$ multiplies the $y$-variance $b$ by $4$ and the covariance $c$ by $2$, while leaving the $x$-variance $a$ unchanged:

$$
S=\begin{bmatrix}10 & 3\\ 3 & 2\end{bmatrix}
\quad\longrightarrow\quad
S'=\begin{bmatrix}10 & 6\\ 6 & 8\end{bmatrix}.
$$

The new trace is $18$, the new determinant is $80-36=44$, and the discriminant is $18^2-4\cdot44=148$. Hence

$$
\lambda_1=\frac{18+\sqrt{148}}{2}\approx15.083,
\qquad
\lambda_2=\frac{18-\sqrt{148}}{2}\approx2.917.
$$

The new PC1 slope is $(15.083-10)/6\approx0.847$, so the angle is about $40.27^\circ$. The retained fraction is $15.083/18\approx0.838$.

| Data | PC1 angle | Fraction kept |
|---|---:|---:|
| original | $18.43^\circ$ | $0.917$ |
| $y$ doubled | $40.27^\circ$ | $0.838$ |

Stretching $y$ makes the vertical direction matter more, so PC1 tilts toward it: the angle goes **up**, from about $18^\circ$ to about $40^\circ$. The cloud becomes less "one-dimensional", so the fraction kept goes **down**, from about $92\%$ to about $84\%$. PCA depends on the units of your features. That is why people often rescale features before running it.

**Now do practice problem 3.5 on paper.** Estimate first: should the angle be above or below $45^\circ$? Then solve the quadratic. The full problem and a worked solution are included below.

---

### 7f. From 2-D to k-D: projection, retained variance, and reconstruction

The 2-D recipe generalizes without any new ideas. Suppose each example has $d$ features, so a point is a vector $p$ in $d$-dimensional space. Centre the data, form the $d\times d$ scatter matrix $S$ (equivalently, the covariance matrix $C=S/n$), and find its eigenvectors $u_1,\dots,u_d$ with eigenvalues $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d\ge0$. The eigenvectors are orthonormal and form a rotated coordinate system: the **principal axes**.

#### Step 1 — choose $k$

Sort the eigenvalues from largest to smallest and keep the top $k$. Three common rules:

- **Elbow:** plot $\lambda_i$ against $i$ and stop where the curve flattens.
- **Variance target:** choose the smallest $k$ with

  $$
  \frac{\lambda_1+\cdots+\lambda_k}{\lambda_1+\cdots+\lambda_d}\ge0.90
  \quad\text{or}\quad0.95.
  $$

- **Budget:** choose the largest $k$ that fits the storage or compute limit of the device.

#### Step 2 — project

Form the $d\times k$ matrix $U_k$ whose columns are $u_1,\dots,u_k$. Its columns are orthonormal, so $U_k^\top U_k=I_k$; note that $U_kU_k^\top$ is *not* the identity unless $k=d$. The new coordinates of a point $p$ are

$$
t=U_k^\top p,
$$

a vector of $k$ numbers. Each coordinate $t_i=u_i\cdot p$ is the shadow on the $i$-th principal axis. This is the compression step: $d$ numbers per example become $k$.

#### Step 3 — reconstruct (if needed)

The best approximation of $p$ that uses only the chosen $k$-dimensional subspace is

$$
\hat p=U_k t=U_kU_k^\top p.
$$

The leftover $r=p-\hat p$ is perpendicular to the chosen subspace, and Pythagoras gives

$$
|p|^2=|\hat p|^2+|r|^2.
$$

Summing over all points:

| Quantity | Formula |
|---|---|
| Total spread | $\lambda_1+\cdots+\lambda_d$ |
| Captured spread | $\lambda_1+\cdots+\lambda_k$ |
| Retained fraction | $(\lambda_1+\cdots+\lambda_k)/(\lambda_1+\cdots+\lambda_d)$ |
| Lost fraction | $(\lambda_{k+1}+\cdots+\lambda_d)/(\lambda_1+\cdots+\lambda_d)$ |
| Mean squared reconstruction error | $(\lambda_{k+1}+\cdots+\lambda_d)/n$ |

The last line divides the lost spread by $n$ because spread is a sum of squared errors; with the sample convention, divide by $n-1$ instead. These identities are exact for the centred data — not approximations. The statement that keeping the top $k$ components gives the best approximation in squared error among all $k$-dimensional subspaces is the **Eckart–Young theorem**.

These formulas use the scatter-matrix eigenvalues. If you use the covariance matrix instead, every eigenvalue is divided by $n$ (or $n-1$), so the retained fraction is unchanged and the mean squared error becomes the sum of the discarded covariance eigenvalues.

**Worked 2-D example.** Our cloud has $\lambda_1=11$, $\lambda_2=1$, total $12$.

- Keeping $k=2$ components retains $12/12=100\%$ and reconstructs every point exactly.
- Keeping $k=1$ (PC1) retains $11/12\approx91.7\%$ and loses $1/12\approx8.3\%$. The sum of squared residuals over the four points is exactly $\lambda_2=1$, so the mean squared residual per point is $1/4=0.25$. Each point is now stored as one number instead of two.
- If $\lambda_2$ had been $0$, all points would lie exactly on PC1 and 1-D storage would be lossless.

**The trade-offs.**

- **More components** → more variance retained, smaller reconstruction error, but more storage, more computation, and more noise passed through.
- **Fewer components** → compression, denoising, and a lower-dimensional picture you can plot, but structure in the discarded directions is gone forever. PCA cannot tell "signal" from "noise"; it only sees which directions have large variance.
- **Unsupervised:** PCA never looks at labels. A low-variance direction can still separate two classes perfectly (imagine two tight clusters whose centres differ along that direction). Dropping it may hurt classification even while reconstruction looks fine. Supervised methods such as **LDA** (linear discriminant analysis) use the labels.
- **Scaling:** PCA is not scale-invariant. If features have different units, standardize them first, or the feature with the largest numerical range will dominate the covariance matrix. After standardization, the covariance matrix becomes the correlation matrix.

---

## Practice check: problem 3.5 (PCA in 2-D)

**Problem.** For centred data, the first principal component is the eigenvector of the scatter matrix

$$
\begin{bmatrix}\sum x^2 & \sum xy\\ \sum xy & \sum y^2\end{bmatrix}
$$

with the largest eigenvalue $\lambda_1$. The fraction of variance it explains is $\lambda_1/(\lambda_1+\lambda_2)$. For a $2\times2$ matrix, the eigenvalues solve $\lambda^2-(\operatorname{trace})\lambda+\det=0$.

The points are $(-2,-1),(-1,-1),(0,0),(1,1),(2,1)$. They are already centred.

**(a)** What angle, to the nearest degree, does PC1 make with the $x$-axis? Options: $0^\circ,22^\circ,32^\circ,45^\circ,58^\circ,90^\circ$.

**(b)** Report $\lfloor100\times\text{fraction of variance explained by PC1}\rfloor$.

<details><summary>Hint 1: understand the question</summary>

Several terms may be new. None of them is the puzzle.

- **Centred:** the $x$-values average to 0, and so do the $y$-values.
- **First principal component (PC1):** the direction through the origin along which the points are most spread out.
- **Scatter matrix:** the $2\times2$ table of sums $\begin{bmatrix}\sum x^2 & \sum xy\\ \sum xy & \sum y^2\end{bmatrix}$. $\sum x^2$ measures the spread along $x$, $\sum y^2$ the spread along $y$. $\sum xy$ is positive when $x$ and $y$ tend to have the same sign, i.e. the cloud tilts up to the right.
- **Matrix times a direction:** $\begin{bmatrix}a & b\\ c & d\end{bmatrix}$ times $(v_1,v_2)$ gives $(av_1+bv_2,\ cv_1+dv_2)$.
- **Eigenvector:** a direction that the matrix only *stretches*, without turning it. The output points the same way as the input, just $\lambda$ times as long. That stretch factor $\lambda$ is the **eigenvalue**. Tiny example with $M=\begin{bmatrix}2&0\\0&3\end{bmatrix}$: $(1,0)$ becomes $(2,0)=2(1,0)$, so $(1,0)$ is an eigenvector with eigenvalue 2. But $(1,1)$ becomes $(2,3)$, which points a different way, so $(1,1)$ is not an eigenvector.
- **Trace** $=a+d$, the sum of the diagonal. **Determinant** (det) $=ad-bc$. For the tiny $M$: trace $5$, det $6$, and $\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)$ gives eigenvalues $2$ and $3$.

Now sketch the five points. Which way does the cloud stretch? Is that direction steeper or flatter than the line $y=x$?

</details>

<details><summary>Hint 2: the key idea</summary>

Move **M10 (Kill options with counterexamples)**: use your sketch to rule out options before computing anything. Is the cloud tilted? Is it steeper or flatter than $45^\circ$? ($x$ runs from $-2$ to $2$, but $y$ only from $-1$ to $1$.)

To decide between the options that survive: compute the scatter matrix, solve the quadratic for $\lambda_1$, and find the eigenvector's slope $v_2/v_1$. A line through the origin with slope $m$ makes an angle $\theta$ with the $x$-axis where $\tan\theta=m$ ($\tan$ is "rise over run" for that angle). Useful values: $\tan30^\circ=1/\sqrt3\approx0.577$, and $\tan45^\circ=1$.

</details>

<details><summary>Hint 3: set it up</summary>

$\sum x^2=4+1+0+1+4=10$, $\sum y^2=4$, $\sum xy=6$. So the matrix is $\begin{bmatrix}10&6\\6&4\end{bmatrix}$, with trace $14$ and det $=10\cdot4-6\cdot6=4$. Solve $\lambda^2-14\lambda+4=0$.

For the eigenvector, write out "matrix times $(v_1,v_2)$ = $\lambda_1$ times $(v_1,v_2)$" and use the first row: $10v_1+6v_2=\lambda_1v_1$.

</details>

<details><summary>Answer</summary>

(a) **$32^\circ$** (b) **97**

</details>

<details><summary>Full solution: the thinking, step by step</summary>

**Step 1: check it is centred, and sketch.** $x$: $(-2-1+0+1+2)/5=0$. $y$: $(-1-1+0+1+1)/5=0$. Centred, as stated. The points rise from bottom-left to top-right, but $x$ runs from $-2$ to $2$ while $y$ only runs from $-1$ to $1$.

**Step 2: kill options first (M10).**

- **$0^\circ$ and $90^\circ$:** the cloud clearly tilts up to the right ($\sum xy=6>0$), so the best direction is neither axis. Killed.
- **$45^\circ$ and $58^\circ$:** the near points $(1,1)$ and $(-1,-1)$ lie on $y=x$, but the far points $(2,1)$ and $(-2,-1)$ lie on the flatter line $y=x/2$, at about $27^\circ$. The far points are farther out, so they pull harder on the direction of greatest spread. The best line should be flatter than $y=x$, below $45^\circ$. That kills $45^\circ$, and $58^\circ$ (steeper still) with it.

Two survivors: $22^\circ$ and $32^\circ$. Your intuition says "somewhere between $27^\circ$ and $45^\circ$", which points to $32^\circ$. Now confirm it.

**Step 3: build the scatter matrix.**

| Point | $x^2$ | $y^2$ | $xy$ |
|---|---:|---:|---:|
| $(-2,-1)$ | 4 | 1 | 2 |
| $(-1,-1)$ | 1 | 1 | 1 |
| $(0,0)$ | 0 | 0 | 0 |
| $(1,1)$ | 1 | 1 | 1 |
| $(2,1)$ | 4 | 1 | 2 |
| **Sum** | **10** | **4** | **6** |

So

$$
S=\begin{bmatrix}10&6\\6&4\end{bmatrix}.
$$

**Step 4: the eigenvalues.** Trace $=10+4=14$. Det $=10\cdot4-6\cdot6=4$. So $\lambda^2-14\lambda+4=0$.

Quadratic formula:

$$
\lambda=\frac{14\pm\sqrt{196-16}}{2}
=\frac{14\pm\sqrt{180}}{2}
=7\pm3\sqrt5.
$$

Since $\sqrt{180}=6\sqrt5\approx13.416$, the roots are $\lambda_1=7+3\sqrt5\approx13.708$ and $\lambda_2=7-3\sqrt5\approx0.292$.

Why does that quadratic hold? "$S$ times $v=\lambda$ times $v$" means two equations:

$$
(10-\lambda)v_1+6v_2=0,
\qquad
6v_1+(4-\lambda)v_2=0.
$$

Each one is a line through the origin in the $(v_1,v_2)$ plane. Two such lines share a point other than $(0,0)$ only if they are the same line, which means their coefficients are in proportion: $(10-\lambda)(4-\lambda)=6\cdot6$. Expanding gives $\lambda^2-14\lambda+40-36=0$, which is $\lambda^2-(\text{trace})\lambda+\det=0$.

**Step 5: the eigenvector for $\lambda_1$.** Use the first equation:

$$
(10-13.708)v_1+6v_2=0
\quad\Longrightarrow\quad
\frac{v_2}{v_1}=\frac{3.708}{6}=0.618.
$$

PC1 is the line through the origin with slope $0.618$.

Check that $S$ only stretches this direction:

$$
S\begin{bmatrix}1\\0.618\end{bmatrix}
=\begin{bmatrix}10+6\cdot0.618\\6+4\cdot0.618\end{bmatrix}
=\begin{bmatrix}13.708\\8.472\end{bmatrix}
=13.708\begin{bmatrix}1\\0.618\end{bmatrix}.
$$

Same direction, $13.708$ times longer. (As it happens, $0.618=(\sqrt5-1)/2$, related to the golden ratio.)

**Step 6: turn the slope into an angle.** The angle $\theta$ satisfies $\tan\theta=0.618$. Without a calculator: $\tan30^\circ=1/\sqrt3\approx0.577$, and $\tan45^\circ=1$. The slope $0.618$ is a little more than $0.577$ and less than $1$, so $\theta$ is a little more than $30^\circ$ and less than $45^\circ$. Of the survivors, only **$32^\circ$** fits. With a calculator: $\theta\approx31.7^\circ$.

**Step 7: fraction of variance.** **Variance** is the average squared distance from the mean. Variance would divide every sum by $5$, but that scales both $\lambda$'s by the same amount and cancels in the fraction, so you can use the scatter matrix directly:

$$
\frac{\lambda_1}{\lambda_1+\lambda_2}
=\frac{13.708}{14}
=0.979,
$$

so $\lfloor100\times0.979\rfloor=97$.

Why is $\lambda_1+\lambda_2$ exactly $14$? Any quadratic with roots $\lambda_1$ and $\lambda_2$ can be written

$$
(\lambda-\lambda_1)(\lambda-\lambda_2)
=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2.
$$

Compare with $\lambda^2-14\lambda+4$: the roots add up to the trace, $14$. And the trace is $\sum x^2+\sum y^2=\sum(x^2+y^2)$, the total of the squared distances from the centre: the total spread in all directions. So PC1 captures $13.708$ of the $14$ units of spread, and PC2 only $0.292$. That fits the sketch: the five points lie almost on a line.

**What to remember:** PC1 is the direction of greatest spread. For a $2\times2$ scatter matrix, get $\lambda$ from $\lambda^2-(\operatorname{trace})\lambda+\det=0$, then the slope $v_2/v_1$ from one row of "$Sv=\lambda v$". Fraction explained $=\lambda_1/\operatorname{trace}$. Sketch first and kill options: the answer leans toward the axis with more spread.

**Common trap:** writing the slope upside down. $v_1/v_2=1/0.618=1.618$ gives about $58^\circ$, which is exactly the distractor in the options. Slope is rise over run, $v_2/v_1$. The kill step catches this mistake: $58^\circ$ is steeper than $45^\circ$, which the sketch already ruled out.

</details>

---

## Connect: PCA and the linear classifier

The notebook's Connect section asks:

> A PCA shadow is $t=x\cos\theta+y\sin\theta$. A linear classifier's score is $s=Xw+b$. Both are the same operation: a dot product with a vector. What would "thresholding the PC1 shadow at $0$" do to the 20 gestures, and why might it, or might it not, separate waves from punches?

Think about what PCA optimizes (total spread, ignoring labels) and what a classifier needs (separation between labelled classes). A direction with the largest spread is not necessarily the direction that separates the two labels. This is the same warning as the "unsupervised" trade-off in 7f.

---

## Going further

### Why eigenvectors, without calculus

`RESOURCES.md` suggests a second proof that the best direction is an eigenvector, using only the eigenvector grid. It is a good follow-up after 7c:

> The two eigenvectors of $S$ are perpendicular. Write any direction in that eigenvector grid:
>
> $u=\cos\varphi\,e_1+\sin\varphi\,e_2.$
>
> What does $u\cdot(Su)$ become? Why does that make it obvious that the best $\varphi$ is $0$?

**Answer sketch.** Because $e_1$ and $e_2$ are perpendicular unit eigenvectors with eigenvalues $\lambda_1$ and $\lambda_2$,

$$
u\cdot(Su)
=\cos^2\varphi\,\lambda_1+\sin^2\varphi\,\lambda_2.
$$

This is a weighted average of $\lambda_1$ and $\lambda_2$ with weights $\cos^2\varphi$ and $\sin^2\varphi$, which are non-negative and sum to $1$. It is largest when $\cos^2\varphi=1$, i.e. $\varphi=0$, and then it equals $\lambda_1$. This is the same argument as "why the largest eigenvalue wins" in 7d, written without derivatives.

### Requested visual

The first item in the `viz/README.md` queue is an animation for the question:

> Why is PC1 an eigenvector of the covariance matrix? Rotate a line through the cloud: the shadows slide, the spread rises and falls, and at the peak $S\cdot u$ lines up with $u$.

It is tracked as [Issue #1](https://github.com/Shreeshinator/ioai-prep/issues/1) and supports notebook 03 §7 and practice 3.5. The animation would make the derivative argument in 7c visual: the peak of the spread curve is exactly where the matrix stops turning the direction.

### Where PCA appears in this repository

- **Notebook:** `notebooks/03_algorithms.ipynb` §7 (the source of this document), plus the exam walkthrough in §11 (Jan 18, Section B4, Model Compression).
- **Practice:** problem 3.5 in `practice/03-algorithms-by-hand.md`; full solution in `practice/solutions/03-algorithms-by-hand.md`.
- **Schedule:** `PLAN.md` week 3 pairs §7 with practice 3.5; the listed struggle is "PCA's eigenvector (3.5)".
- **Resources:** the note "PCA: why eigenvectors, why the covariance matrix?" in `RESOURCES.md`, and StatQuest video #30 ("PCA, Step-by-Step") as a follow-up.
- **Connections:** `toolkit/CONNECTIONS.md` groups the PCA scatter matrix with the linear-classifier score $s=Xw$ and PageRank as examples of matrix-times-vector reasoning.
- **International paper:** `papers/international/README.md` notes a PCA projection in USAAIO 2026 Round 1.
- **Open visual request:** `viz/README.md`, first row of the requested table; tracked as Issue #1.

---

## What to remember

- PCA chooses the unit direction $u$ that maximizes the spread $\sum(u\cdot p)^2$ of the centred data.
- The spread in every direction is controlled by three sums: $\sum x^2$, $\sum y^2$, and $\sum xy$. Arranged as the scatter matrix $S$, they give $\text{spread}(u)=u^\top Su$.
- The maximizing direction is an eigenvector of $S$, and the maximum spread is its eigenvalue. The top eigenvector is PC1.
- For a $2\times2$ matrix, solve $\lambda^2-(\operatorname{trace})\lambda+\det=0$, then get the slope from $u_2/u_1=(\lambda-a)/c$. The fraction PC1 keeps is $\lambda_1/(\lambda_1+\lambda_2)$.
- In $d$ dimensions, keep the top $k$ eigenvectors, project with $t=U_k^\top p$, and reconstruct with $\hat p=U_kU_k^\top p$. The retained fraction is the sum of the top $k$ eigenvalues divided by the total.
- PCA is unsupervised, linear, and scale-sensitive. Standardize features when their units differ, and do not assume a low-variance direction is useless for classification.

## Glossary

| Term | Definition |
|---|---|
| **Centred data** | Data whose mean has been subtracted, so the cloud's centre is at the origin. |
| **Covariance** | A measure of how two features vary together. Positive means they tend to rise together; negative means one tends to rise as the other falls. |
| **Covariance matrix** | The scatter matrix divided by $n$ (population) or $n-1$ (sample). Diagonal entries are variances; off-diagonal entries are covariances. |
| **Determinant** | For a $2\times2$ matrix $\begin{bmatrix}a&c\\c&b\end{bmatrix}$, $\det=ab-c^2$. Zero means the matrix squashes the plane onto a line. |
| **Dot product** | $p\cdot u=p_1u_1+p_2u_2$. It measures how much of $p$ lies along $u$. |
| **Eigenvalue** | The stretch factor $\lambda$ in $Su=\lambda u$. For a scatter matrix, it equals the spread along the eigenvector. |
| **Eigenvector** | A direction that a matrix only stretches, not turns: $Su=\lambda u$. |
| **Eckart–Young theorem** | The best rank-$k$ approximation of a matrix (in squared error) is obtained by keeping its top $k$ singular values and vectors. |
| **Lagrange multiplier** | A scalar introduced to turn a constrained optimization problem into an unconstrained one. Here it becomes the eigenvalue. |
| **LDA** | Linear discriminant analysis: a supervised method that uses labels to find separating directions, unlike PCA. |
| **Orthonormal** | Mutually perpendicular unit vectors. |
| **PC1** | The first principal component: the unit direction with the largest spread. |
| **Principal axes** | The orthonormal eigenvector directions of the scatter or covariance matrix. |
| **Projection** | The shadow $t=u\cdot p$ of a point on a direction, or the vector $(u\cdot p)u$ along that direction. |
| **Rank** | The number of independent directions in a matrix or dataset; rank $k$ means a $k$-dimensional subspace. |
| **Rayleigh quotient** | $R(u)=(u^\top Su)/(u^\top u)$. Its stationary values are the eigenvalues and its maximum is the top eigenvalue. |
| **Reconstruction error** | The part of a point not captured by the chosen components: $\lVert p-\hat p\rVert^2$. |
| **Scatter matrix** | The unnormalized covariance matrix $S=\begin{bmatrix}\sum x^2&\sum xy\\ \sum xy&\sum y^2\end{bmatrix}$. |
| **Singular value decomposition (SVD)** | A factorization $X=U\Sigma V^\top$. The right singular vectors are the eigenvectors of $X^\top X$, and the squared singular values are its eigenvalues. |
| **Spread** | $\sum t^2$, the sum of squared projections on a direction. For centred data it is proportional to variance. |
| **Standard deviation** | The square root of the variance; it measures spread in the same units as the feature. |
| **Standardization** | Subtracting the mean and dividing by the standard deviation, so each feature has mean 0 and variance 1. |
| **Trace** | The sum of the diagonal entries. For a $2\times2$ scatter matrix, $\operatorname{trace}=\sum x^2+\sum y^2$, the total spread. |
| **Variance** | The average squared deviation from the mean. Population variance divides by $n$; sample variance divides by $n-1$. |
