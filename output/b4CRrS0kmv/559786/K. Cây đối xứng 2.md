# K. Cây đối xứng 2

## 📖 Problem

Just in case somebody missed it: we have wonderful girls in Arpa’s land.
Arpa has a rooted tree (connected acyclic graph) consisting of $$$n$$$ vertices. The vertices are numbered $$$1$$$ through $$$n$$$, the vertex $$$1$$$ is the root. There is a letter written on each edge of this tree. Mehrdad is a fan of
Dokhtar-kosh
things. He call a string Dokhtar-kosh, if we can shuffle the characters in string such that it becomes palindrome.
![](https://espresso.codeforces.com/a7c274b610a81b8f39b3c667a30d97554c35d2f9.png)
He asks Arpa, for each vertex $$$v$$$, what is the length of the longest simple path in subtree of $$$v$$$ that form a Dokhtar-kosh string.


## 🧩 Input

Input
The first line contains integer $$$n$$$ ($$$1 \leq n \leq 5 \cdot 10^5$$$) — the number of vertices in the tree.
$$$(n - 1)$$$ lines follow, the $$$i$$$-th of them contain an integer $$$p_{i+1}$$$ and a letter $$$c_{i+1}$$$ ($$$1 \leq p_{i+1} \leq i$$$, $$$c_{i+1}$$$ is lowercase English letter, between
a
and
v
, inclusively), that mean that there is an edge between nodes $$$p_{i+1}$$$ and $$$i+1$$$ and there is a letter $$$c_{i+1}$$$ written on this edge.


## 💡 Output

Output
Print $$$n$$$ integers. The $$$i$$$-th of them should be the length of the longest simple path in subtree of the $$$i$$$-th vertex that form a Dokhtar-kosh string.


## 🧠 Example

### Input

```text
41 s2 a3 s
```

### Output

```text
3 1 1 0
```


