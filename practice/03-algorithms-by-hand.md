# Set 03: Algorithms by hand

**Week 3** · 5 problems · target time 45 min · moves: M1, M6, M10

> The exam gives you each algorithm's definition. Your job is to execute it **exactly**, including ties. Check in `notebooks/03_algorithms.ipynb`.

---

### 3.1 Which distance? [3 pts]

> **Background (k-NN):** To classify a query, find its $k$ nearest labelled points and take the majority label. Euclidean distance is $\sqrt{\Delta x^2+\Delta y^2}$. Manhattan distance is $|\Delta x|+|\Delta y|$.

| Point | (3, 0) | (2, 2) | (0, −3) | (−2, 2) | (5, 5) |
|---|---|---|---|---|---|
| Label | red | blue | red | blue | blue |

**Output:** Classify the query (0, 0) with $k = 3$ using (a) Euclidean distance and (b) Manhattan distance. Is any tie a problem here? Explain.

---

### 3.2 Bad start [3 pts]

> **Background (k-means, 1-D):** (1) Assign each point to its nearest centroid. (2) Move each centroid to the mean of its points. Repeat until nothing changes. SSE = sum of squared distances from each point to its centroid.

Points: `1, 2, 3, 8, 9, 10, 25`, with $k = 2$. A point exactly halfway between two centroids goes to the left one.

**Output:**
(a) Starting centroids 1 and 2: give the final centroids and SSE.
(b) Starting centroids 1 and 25: give the final centroids and SSE.
(c) Which run found the better clustering? What does that tell you about k-means?

---

### 3.3 Best first split [3 pts]

> **Background:** The Gini impurity of a node with class fractions $p_i$ is $1 - \sum p_i^2$. A split's score is the size-weighted average Gini of its children. Lower is better. Gain = parent Gini − split score.

10 samples: 6 *yes*, 4 *no*. Three candidate splits (yes, no):

| Feature | Left | Right |
|---|---|---|
| A | (4, 0) | (2, 4) |
| B | (3, 2) | (3, 2) |
| C | (5, 1) | (1, 3) |

**Output:** Which feature is chosen? Report ⌊1000 × gain⌋ for that split.

---

### 3.4 Single vs complete linkage [3 pts]

> **Background (agglomerative clustering):** Start with every point as its own cluster. Repeatedly merge the two closest clusters. **Single linkage:** cluster distance = *closest* pair of points. **Complete linkage:** cluster distance = *farthest* pair of points.

Points on a line: `0, 1, 4, 5, 11, 13`.

**Output:**
(a) Give the height (distance) of the final merge under single and under complete linkage.
(b) If you cut each dendrogram at height 4, how many clusters do you get under each?

---

### 3.5 PCA in 2-D [3 pts]

> **Background:** For centred data, the first principal component is the eigenvector of the scatter matrix $\begin{bmatrix}\sum x^2 & \sum xy\\ \sum xy & \sum y^2\end{bmatrix}$ with the largest eigenvalue $\lambda_1$. The fraction of variance it explains is $\lambda_1 / (\lambda_1+\lambda_2)$. For a 2×2 matrix, the eigenvalues solve $\lambda^2 - (\text{trace})\lambda + \det = 0$.

Points: (−2, −1), (−1, −1), (0, 0), (1, 1), (2, 1). They are already centred.

**Output:**
(a) What angle, to the nearest degree, does PC1 make with the x-axis? (Options: 0°, 22°, 32°, 45°, 58°, 90°)
(b) Report ⌊100 × fraction of variance explained by PC1⌋.
