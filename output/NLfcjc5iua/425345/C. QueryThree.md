# C. QueryThree

## 📖 Problem

Cho $$$n$$$ phần tử, phần tử thứ $$$i$$$ có giá trị là $$$a_i$$$. Cho số $$$k$$$.
Với mỗi phần tử $$$i$$$ hãy in ra $$$j$$$ sao cho $$$j$$$ nhỏ nhất, $$$j\leq i$$$ và $$$sum(a_j,a_{j+1},...,a_i)\leq k$$$. Nếu không có số $$$j$$$ nào thỏa mãn thì in ra $$$-1$$$.


## 🧩 Input

Input
Dòng đầu gồm $$$2$$$ số $$$n$$$ và $$$k$$$ $$$(1\leq n \leq 10^5)$$$ $$$(1\leq k\leq 10^9)$$$.
Dòng hai gồm $$$n$$$ số, số thứ $$$i$$$ là giá trị của $$$a_i$$$ $$$(1\leq a_i\leq 10^4)$$$.


## 💡 Output

Output
Gồm $$$n$$$ dòng ứng với $$$n$$$ đáp án cần tìm.


## 🧠 Example

### Input

```text
5 7
1 2 3 4 5
```

### Output

```text
1
1
1
3
5
```


