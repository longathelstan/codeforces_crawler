# A. QueryOne

## 📖 Problem

Cho $$$n$$$ phần tử, phần tử thứ $$$i$$$ có giá trị là $$$a_i$$$, cho $$$q$$$ truy vấn, truy vấn thứ $$$i$$$ có dạng là: $$$l_i$$$ và $$$r_i$$$.
Với mỗi truy vấn hãy in ra tổng các phần tử từ $$$l_i$$$ tới $$$r_i$$$.


## 🧩 Input

Input
Dòng đầu gồm số $$$n$$$ $$$(1\leq n \leq 10^5)$$$.
Dòng hai gồm $$$n$$$ số, số thú $$$i$$$ là giá trị của $$$a_i$$$ $$$(1\leq a_i \leq 10^9)$$$.
Dòng ba gồm $$$q$$$ $$$(1\leq q \leq 10^5)$$$ là số truy vấn.
Dòng thứ $$$i$$$ trong $$$q$$$ dòng tiếp theo mỗi dòng gồm $$$2$$$ số là $$$l_i$$$ và $$$r_i$$$ $$$(1\leq l_i\leq r_i\leq n)$$$.


## 💡 Output

Output
Gồm $$$q$$$ dòng, dòng thứ $$$i$$$ là đáp án của truy vấn thứ $$$i$$$.


## 🧠 Example

### Input

```text
5
1 2 3 4 5
5
1 1
1 2
1 3
1 4
1 5
```

### Output

```text
1
3
6
10
15
```


